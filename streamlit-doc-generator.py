#!/usr/bin/env python3
"""
Streamlit Project Documentation Generator

This script analyzes a Streamlit project's structure and code to generate
comprehensive technical documentation in Markdown format.
"""

import os
import ast
import re
import sys
import importlib.util
from collections import defaultdict
from typing import Dict, List, Set, Tuple, Any, Optional
import argparse
import logging
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class StreamlitComponentExtractor(ast.NodeVisitor):
    """Extract Streamlit components and other relevant information from AST."""
    
    def __init__(self):
        self.streamlit_calls = []
        self.functions = []
        self.classes = []
        self.imports = []
        self.variables = []
        self.current_function = None
        self.current_class = None
        
    def visit_Import(self, node):
        """Extract import statements."""
        for name in node.names:
            self.imports.append({
                'type': 'import',
                'name': name.name,
                'alias': name.asname
            })
        self.generic_visit(node)
        
    def visit_ImportFrom(self, node):
        """Extract from import statements."""
        module = node.module
        for name in node.names:
            self.imports.append({
                'type': 'from_import',
                'module': module,
                'name': name.name,
                'alias': name.asname
            })
        self.generic_visit(node)
    
    def visit_Assign(self, node):
        """Extract variable assignments."""
        for target in node.targets:
            if isinstance(target, ast.Name):
                try:
                    value = ast.unparse(node.value)
                    self.variables.append({
                        'name': target.id,
                        'value': value
                    })
                except:
                    # ast.unparse is only available in Python 3.9+
                    self.variables.append({
                        'name': target.id,
                        'value': "Unable to unparse value"
                    })
        self.generic_visit(node)
    
    def visit_FunctionDef(self, node):
        """Extract function definitions and docstrings."""
        docstring = ast.get_docstring(node)
        params = [
            {
                'name': arg.arg,
                'annotation': arg.annotation.id if arg.annotation and hasattr(arg.annotation, 'id') else None
            } for arg in node.args.args
        ]
        
        function_info = {
            'name': node.name,
            'docstring': docstring,
            'params': params,
            'returns': None,
            'decorators': [d.id if isinstance(d, ast.Name) else d.func.id if isinstance(d, ast.Call) else None for d in node.decorator_list],
            'lineno': node.lineno
        }
        
        # Check for return annotation
        if node.returns:
            try:
                function_info['returns'] = ast.unparse(node.returns)
            except:
                if hasattr(node.returns, 'id'):
                    function_info['returns'] = node.returns.id
        
        self.functions.append(function_info)
        
        # Save current function for context
        previous_function = self.current_function
        self.current_function = node.name
        
        # Visit children
        self.generic_visit(node)
        
        # Restore context
        self.current_function = previous_function
    
    def visit_ClassDef(self, node):
        """Extract class definitions and docstrings."""
        docstring = ast.get_docstring(node)
        
        class_info = {
            'name': node.name,
            'docstring': docstring,
            'bases': [base.id if isinstance(base, ast.Name) else ast.unparse(base) for base in node.bases],
            'methods': [],
            'lineno': node.lineno
        }
        
        # Save current class for context
        previous_class = self.current_class
        self.current_class = node.name
        
        # Visit all nodes in the class
        self.generic_visit(node)
        
        # Find methods (functions inside this class)
        class_methods = [f for f in self.functions if f['lineno'] > node.lineno]
        for method in class_methods:
            if method not in class_info['methods']:
                class_info['methods'].append(method)
        
        # Add class to the list
        self.classes.append(class_info)
        
        # Restore context
        self.current_class = previous_class
    
    def visit_Call(self, node):
        """Extract function/method calls, focusing on Streamlit components."""
        if isinstance(node.func, ast.Attribute):
            # Handle method calls like st.write()
            if hasattr(node.func.value, 'id') and node.func.value.id == 'st':
                try:
                    args_str = [ast.unparse(arg) for arg in node.args]
                    kwargs_str = [f"{kw.arg}={ast.unparse(kw.value)}" for kw in node.keywords]
                except:
                    args_str = [f"arg_{i}" for i in range(len(node.args))]
                    kwargs_str = [f"{kw.arg}=value" for kw in node.keywords]
                
                streamlit_call = {
                    'component': node.func.attr,
                    'args': args_str,
                    'kwargs': kwargs_str,
                    'in_function': self.current_function,
                    'in_class': self.current_class,
                    'lineno': node.lineno
                }
                self.streamlit_calls.append(streamlit_call)
        
        self.generic_visit(node)

class DocumentationGenerator:
    """Generate Markdown documentation from analyzed project files."""
    
    def __init__(self, project_path: str, output_file: str, ignore_dirs: List[str] = None):
        """
        Initialize the documentation generator.
        
        Args:
            project_path: Root directory of the Streamlit project
            output_file: Path where the documentation will be written
            ignore_dirs: List of directory names to ignore
        """
        self.project_path = os.path.abspath(project_path)
        self.output_file = output_file
        self.ignore_dirs = ignore_dirs or ['.git', '.github', '__pycache__', '.venv', 'venv', 'env', 'node_modules']
        self.files_data = {}
        self.project_structure = {}
        self.requirements = set()
    
    def _is_ignored(self, path: str) -> bool:
        """Check if a path should be ignored."""
        path_parts = path.split(os.sep)
        return any(part in self.ignore_dirs for part in path_parts)
    
    def _extract_file_info(self, file_path: str) -> Dict:
        """Extract information from a file based on its extension."""
        _, ext = os.path.splitext(file_path)
        
        # Handle Python files
        if ext.lower() == '.py':
            return self._extract_python_file_info(file_path)
        
        # Handle requirements files
        elif os.path.basename(file_path) == 'requirements.txt':
            return self._extract_requirements_info(file_path)
        
        # Handle README files
        elif os.path.basename(file_path).lower() == 'readme.md':
            return self._extract_readme_info(file_path)
        
        # Handle other files
        else:
            return {
                'type': 'other',
                'extension': ext,
                'size': os.path.getsize(file_path)
            }
    
    def _extract_python_file_info(self, file_path: str) -> Dict:
        """Extract information from a Python file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            # Parse the code into an AST
            tree = ast.parse(code)
            
            # Extract module docstring
            module_docstring = ast.get_docstring(tree)
            
            # Extract components, functions, classes, etc.
            extractor = StreamlitComponentExtractor()
            extractor.visit(tree)
            
            return {
                'type': 'python',
                'docstring': module_docstring,
                'streamlit_calls': extractor.streamlit_calls,
                'functions': extractor.functions,
                'classes': extractor.classes,
                'imports': extractor.imports,
                'variables': extractor.variables
            }
        except Exception as e:
            logger.error(f"Error parsing {file_path}: {str(e)}")
            return {
                'type': 'python',
                'error': str(e)
            }
    
    def _extract_requirements_info(self, file_path: str) -> Dict:
        """Extract information from a requirements.txt file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                requirements = []
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        # Extract package and version
                        match = re.match(r'^([^=<>~!]+)([=<>~!]+.+)?$', line)
                        if match:
                            package, version = match.groups()
                            requirements.append({
                                'package': package.strip(),
                                'version': version.strip() if version else None
                            })
                            # Add to global requirements set
                            self.requirements.add(line)
            
            return {
                'type': 'requirements',
                'dependencies': requirements
            }
        except Exception as e:
            logger.error(f"Error parsing {file_path}: {str(e)}")
            return {
                'type': 'requirements',
                'error': str(e)
            }
    
    def _extract_readme_info(self, file_path: str) -> Dict:
        """Extract information from a README.md file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract title
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else None
            
            return {
                'type': 'readme',
                'title': title,
                'content': content
            }
        except Exception as e:
            logger.error(f"Error parsing {file_path}: {str(e)}")
            return {
                'type': 'readme',
                'error': str(e)
            }
    
    def collect_project_info(self) -> None:
        """Walk through the project and collect information about all files."""
        logger.info(f"Analyzing project at {self.project_path}...")
        
        for root, dirs, files in os.walk(self.project_path):
            # Skip ignored directories
            dirs[:] = [d for d in dirs if d not in self.ignore_dirs]
            
            rel_path = os.path.relpath(root, self.project_path)
            if rel_path == '.':
                rel_path = ''
            
            # Initialize this directory in the structure
            current_level = self.project_structure
            if rel_path:
                for part in rel_path.split(os.sep):
                    if part not in current_level:
                        current_level[part] = {}
                    current_level = current_level[part]
            
            # Process files in this directory
            for file in files:
                file_path = os.path.join(root, file)
                rel_file_path = os.path.relpath(file_path, self.project_path)
                
                # Skip files in ignored directories
                if self._is_ignored(rel_file_path):
                    continue
                
                logger.info(f"Processing {rel_file_path}")
                
                # Extract information from the file
                file_info = self._extract_file_info(file_path)
                
                # Store the information
                self.files_data[rel_file_path] = {
                    'path': rel_file_path,
                    'info': file_info
                }
                
                # Add to project structure
                current_level[file] = "file"
    
    def _generate_project_structure_md(self) -> str:
        """Generate Markdown representation of the project structure."""
        md_lines = ["## Project Structure\n"]
        
        def _add_structure(structure, level=0):
            items = sorted(structure.items())
            for name, content in items:
                indent = "    " * level
                if content == "file":
                    md_lines.append(f"{indent}- 📄 {name}")
                else:
                    md_lines.append(f"{indent}- 📁 {name}")
                    _add_structure(content, level + 1)
        
        _add_structure(self.project_structure)
        return "\n".join(md_lines)
    
    def _generate_python_file_md(self, file_path: str, file_data: Dict) -> str:
        """Generate Markdown documentation for a Python file."""
        info = file_data['info']
        md_lines = [f"### 📄 {file_path}\n"]
        
        # Add module docstring
        if info.get('docstring'):
            md_lines.append("**Description:**")
            md_lines.append(f"{info['docstring'].strip()}\n")
        
        # Add imports
        if info.get('imports'):
            md_lines.append("**Imports:**")
            for imp in info['imports']:
                if imp['type'] == 'import':
                    line = f"- `import {imp['name']}"
                    if imp['alias']:
                        line += f" as {imp['alias']}"
                    line += "`"
                else:  # from_import
                    line = f"- `from {imp['module']} import {imp['name']}"
                    if imp['alias']:
                        line += f" as {imp['alias']}"
                    line += "`"
                md_lines.append(line)
            md_lines.append("")
        
        # Add classes
        if info.get('classes'):
            md_lines.append("**Classes:**")
            for cls in info['classes']:
                bases = f"({', '.join(cls['bases'])})" if cls['bases'] else ""
                md_lines.append(f"- `class {cls['name']}{bases}`")
                
                if cls.get('docstring'):
                    md_lines.append(f"  - **Description:** {cls['docstring'].strip()}")
                
                if cls.get('methods'):
                    md_lines.append("  - **Methods:**")
                    for method in cls['methods']:
                        params = ", ".join([p['name'] for p in method['params']])
                        md_lines.append(f"    - `{method['name']}({params})`")
                        if method.get('docstring'):
                            md_lines.append(f"      - {method['docstring'].strip()}")
            md_lines.append("")
        
        # Add functions
        if info.get('functions'):
            md_lines.append("**Functions:**")
            for func in info['functions']:
                # Skip methods already documented in classes
                if any(func in cls.get('methods', []) for cls in info.get('classes', [])):
                    continue
                
                params = ", ".join([p['name'] for p in func['params']])
                md_lines.append(f"- `{func['name']}({params})`")
                
                if func.get('docstring'):
                    md_lines.append(f"  - **Description:** {func['docstring'].strip()}")
                
                if func.get('params'):
                    md_lines.append("  - **Parameters:**")
                    for param in func['params']:
                        param_type = f": {param['annotation']}" if param.get('annotation') else ""
                        md_lines.append(f"    - `{param['name']}{param_type}`")
                
                if func.get('returns'):
                    md_lines.append(f"  - **Returns:** `{func['returns']}`")
            md_lines.append("")
        
        # Add Streamlit components
        if info.get('streamlit_calls'):
            md_lines.append("**Streamlit Components:**")
            for call in info['streamlit_calls']:
                component = call['component']
                args_str = ", ".join(call['args']) if call['args'] else ""
                kwargs_str = ", ".join(call['kwargs']) if call['kwargs'] else ""
                params_str = ", ".join(filter(None, [args_str, kwargs_str]))
                
                context = ""
                if call['in_function']:
                    context = f" (in function `{call['in_function']}`)"
                elif call['in_class']:
                    context = f" (in class `{call['in_class']}`)"
                
                md_lines.append(f"- `st.{component}({params_str})`{context}")
            md_lines.append("")
        
        # Add important variables
        if info.get('variables'):
            md_lines.append("**Key Variables:**")
            for var in info['variables']:
                # Filter out variables that seem to be constants or important configurations
                name = var['name']
                if name.isupper() or name.startswith('config_') or name.endswith('_config'):
                    md_lines.append(f"- `{name} = {var['value']}`")
            md_lines.append("")
        
        return "\n".join(md_lines)
    
    def _generate_requirements_md(self) -> str:
        """Generate Markdown documentation for requirements."""
        if not self.requirements:
            return ""
        
        md_lines = ["## Dependencies\n"]
        md_lines.append("This project depends on the following packages:\n")
        
        for req in sorted(self.requirements):
            md_lines.append(f"- `{req}`")
        
        return "\n".join(md_lines)
    
    def _generate_streamlit_components_summary(self) -> str:
        """Generate a summary of all Streamlit components used in the project."""
        streamlit_components = defaultdict(list)
        
        for file_path, file_data in self.files_data.items():
            info = file_data['info']
            if info.get('type') == 'python' and info.get('streamlit_calls'):
                for call in info['streamlit_calls']:
                    streamlit_components[call['component']].append({
                        'file': file_path,
                        'in_function': call['in_function'],
                        'in_class': call['in_class'],
                        'params': (
                            ", ".join(call['args']) if call['args'] else ""
                        ) + (
                            (", " if call['args'] and call['kwargs'] else "") + 
                            ", ".join(call['kwargs']) if call['kwargs'] else ""
                        )
                    })
        
        if not streamlit_components:
            return ""
        
        md_lines = ["## Streamlit Components Usage\n"]
        md_lines.append("This project uses the following Streamlit components:\n")
        
        for component, usages in sorted(streamlit_components.items()):
            md_lines.append(f"### st.{component}")
            md_lines.append(f"**Used {len(usages)} times in the project.**\n")
            md_lines.append("**Examples:**")
            
            # Show up to 5 usage examples
            for usage in usages[:5]:
                context = ""
                if usage['in_function']:
                    context = f" in function `{usage['in_function']}`"
                elif usage['in_class']:
                    context = f" in class `{usage['in_class']}`"
                
                md_lines.append(f"- In `{usage['file']}`{context}:")
                md_lines.append(f"  ```python\n  st.{component}({usage['params']})\n  ```")
            
            md_lines.append("")
        
        return "\n".join(md_lines)
    
    def generate_documentation(self) -> None:
        """Generate the full documentation and write it to the output file."""
        logger.info("Generating documentation...")
        
        md_lines = ["# Technical Documentation\n"]
        
        # Find README content if available
        readme_content = None
        for file_path, file_data in self.files_data.items():
            if file_data['info'].get('type') == 'readme':
                readme_content = file_data['info'].get('content')
                break
        
        # Add project description from README if available
        if readme_content:
            # Extract sections after the title but before any ## heading
            sections = re.split(r'^##\s+', readme_content, flags=re.MULTILINE)
            if len(sections) > 1:
                intro = sections[0].split('\n', 1)[1]  # Skip the title
                md_lines.append("## Project Overview\n")
                md_lines.append(intro.strip())
                md_lines.append("\n")
        
        # Add project structure
        md_lines.append(self._generate_project_structure_md())
        md_lines.append("\n")
        
        # Add dependencies
        dependencies_md = self._generate_requirements_md()
        if dependencies_md:
            md_lines.append(dependencies_md)
            md_lines.append("\n")
        
        # Add Streamlit components summary
        streamlit_summary_md = self._generate_streamlit_components_summary()
        if streamlit_summary_md:
            md_lines.append(streamlit_summary_md)
            md_lines.append("\n")
        
        # Add detailed file documentation
        md_lines.append("## File Details\n")
        
        # First document Python files
        python_files = {path: data for path, data in self.files_data.items() 
                       if data['info'].get('type') == 'python'}
        
        # Look for main application file (app.py, main.py, streamlit_app.py)
        main_file_candidates = ['app.py', 'main.py', 'streamlit_app.py']
        main_files = [path for path in python_files if os.path.basename(path) in main_file_candidates]
        
        # Document main files first
        for file_path in main_files:
            md_lines.append(self._generate_python_file_md(file_path, python_files[file_path]))
            # Remove from the dictionary to avoid duplication
            del python_files[file_path]
        
        # Document remaining Python files
        for file_path, file_data in sorted(python_files.items()):
            md_lines.append(self._generate_python_file_md(file_path, file_data))
        
        # Write to output file
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(md_lines))
        
        logger.info(f"Documentation generated successfully at {self.output_file}")

def main():
    """Main entry point for the documentation generator."""
    parser = argparse.ArgumentParser(description='Generate technical documentation for a Streamlit project.')
    parser.add_argument('project_path', help='Path to the Streamlit project root directory')
    parser.add_argument('-o', '--output', default='technical_documentation.md',
                        help='Output file path (default: technical_documentation.md)')
    parser.add_argument('-i', '--ignore', nargs='+', default=None,
                        help='Directories to ignore (in addition to defaults)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Combine default and custom ignored directories
    ignore_dirs = ['.git', '.github', '__pycache__', '.venv', 'venv', 'env', 'node_modules']
    if args.ignore:
        ignore_dirs.extend(args.ignore)
    
    # Create and run documentation generator
    doc_generator = DocumentationGenerator(
        project_path=args.project_path,
        output_file=args.output,
        ignore_dirs=ignore_dirs
    )
    
    try:
        doc_generator.collect_project_info()
        doc_generator.generate_documentation()
        print(f"✅ Documentation generated successfully at: {args.output}")
    except Exception as e:
        logger.error(f"Error generating documentation: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

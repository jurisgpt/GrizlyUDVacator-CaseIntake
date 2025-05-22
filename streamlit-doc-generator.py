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
# import argparse # No longer directly used for parser creation here
import logging
# import json # Not used directly anymore, ast.unparse might be an alternative if needed for specific values

from analysis_utils import (
    parse_common_script_args,
    discover_python_files,
    is_path_ignored,
    DEFAULT_IGNORE_DIRS, # Using the default from analysis_utils
    DEFAULT_IGNORE_FILES # Using the default from analysis_utils
)

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
    
    def __init__(self, project_path: str, output_file: str, ignore_dirs_list: List[str], ignore_files_list: List[str]):
        """
        Initialize the documentation generator.
        
        Args:
            project_path: Root directory of the Streamlit project
            output_file: Path where the documentation will be written
            ignore_dirs_list: List of directory names/patterns to ignore
            ignore_files_list: List of file names/patterns to ignore
        """
        self.project_path = os.path.abspath(project_path)
        self.output_file = output_file
        # Convert lists to sets for efficient lookup in is_path_ignored
        self.ignore_dirs_set = set(ignore_dirs_list) if ignore_dirs_list else set(DEFAULT_IGNORE_DIRS)
        self.ignore_files_set = set(ignore_files_list) if ignore_files_list else set(DEFAULT_IGNORE_FILES)
        self.files_data = {}
        self.project_structure = {} # For directory structure visualization
        self.requirements = set()
    
    # _is_ignored is now replaced by the utility function is_path_ignored from analysis_utils.py
    
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

        # Use discover_python_files for Python files
        python_files_to_analyze = discover_python_files(
            self.project_path, self.ignore_dirs_set, self.ignore_files_set
        )

        all_files_in_project = []
        for root, _, files in os.walk(self.project_path, topdown=True):
            # Filter out ignored directories from os.walk itself
            # dirs[:] = [d for d in dirs if not is_path_ignored(os.path.join(root, d), self.ignore_dirs_set, self.ignore_files_set)]
            # The above line was removed because discover_python_files already handles this for .py files.
            # For non-Python files, we will check them individually.
            for file in files:
                all_files_in_project.append(os.path.join(root, file))
        
        # Build project structure for visualization (including non-Python files)
        # And process requirements.txt, README.md specifically
        for abs_file_path in all_files_in_project:
            if is_path_ignored(abs_file_path, self.ignore_dirs_set, self.ignore_files_set):
                continue # Skip explicitly ignored files/dirs

            rel_file_path = os.path.relpath(abs_file_path, self.project_path)
            
            # Update project_structure for visualization
            path_parts = rel_file_path.split(os.sep)
            current_level = self.project_structure
            for part in path_parts[:-1]: # Iterate through directory parts
                if part not in current_level:
                    current_level[part] = {}
                current_level = current_level[part]
            current_level[path_parts[-1]] = "file" # Mark the file

            # Process specific non-Python files like requirements.txt, README.md
            if os.path.basename(abs_file_path).lower() == 'requirements.txt' or \
               os.path.basename(abs_file_path).lower() == 'readme.md':
                if rel_file_path not in self.files_data: # Avoid reprocessing if somehow already added
                    logger.info(f"Processing special file: {rel_file_path}")
                    file_info = self._extract_file_info(abs_file_path)
                    self.files_data[rel_file_path] = {'path': rel_file_path, 'info': file_info}
            # Python files are handled next using the pre-filtered list
        
        # Process Python files discovered by the utility function
        for abs_py_file_path in python_files_to_analyze:
            rel_py_file_path = os.path.relpath(abs_py_file_path, self.project_path)
            if rel_py_file_path in self.files_data: # Already processed (e.g. if project_path was a single file)
                continue

            logger.info(f"Processing Python file: {rel_py_file_path}")
            file_info = self._extract_python_file_info(abs_py_file_path) # _extract_python_file_info expects absolute path
            self.files_data[rel_py_file_path] = {
                'path': rel_py_file_path,
                'info': file_info
            }
            # Project structure for Python files is also handled by the all_files_in_project loop

        if not self.files_data:
            logger.warning(f"No files processed. Check project_path and ignore patterns. Project path: {self.project_path}")
            if os.path.isfile(self.project_path) and not self.project_path.endswith(".py"):
                 logger.warning("If project_path is a single file, it must be a Python file to be processed by discover_python_files.")
    
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
    # Use the common argument parser from analysis_utils
    parser = parse_common_script_args("Generate technical documentation for a Streamlit project.")
    
    # Add script-specific arguments for streamlit-doc-generator
    parser.add_argument(
        '-o', '--output', 
        default='technical_documentation.md',
        help='Output file path for the Markdown documentation (default: technical_documentation.md)'
    )
    parser.add_argument(
        '-v', '--verbose', 
        action='store_true',
        help='Enable verbose logging'
    )
    # Note: --ignore-dirs and --ignore-files are already handled by parse_common_script_args
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # Check if project path exists
    if not os.path.exists(args.project_path):
        logger.error(f"Error: Project path '{args.project_path}' does not exist.")
        sys.exit(1)
        
    # Create and run documentation generator
    # Pass the ignore_dirs and ignore_files from args to the constructor
    doc_generator = DocumentationGenerator(
        project_path=args.project_path,
        output_file=args.output,
        ignore_dirs_list=args.ignore_dirs, # from common args
        ignore_files_list=args.ignore_files # from common args
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

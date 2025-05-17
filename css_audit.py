#!/usr/bin/env python3
import os
import re
import json
import requests
import argparse
import datetime
from pathlib import Path
from dataclasses import dataclass, asdict, field
from typing import List, Dict, Optional
import cssutils

# Initialize cssutils
from cssutils.css import CSSStyleSheet
from cssutils.css import CSSStyleRule
from cssutils.css import CSSStyleDeclaration

cssutils.ser.prefs.useDefaults()

# =========================
# 🔧 Project-Specific Paths
# =========================
PROJECT_ROOT = Path("/Users/pradeepkumar/github/GrizlyUDVacator-CaseIntake")
APP_DIR = PROJECT_ROOT / "grizly_app"
LOGS_DIR = PROJECT_ROOT / "logs/css-audit"

@dataclass
class CSSBlock:
    file: str
    line_number: int
    content: str
    context: str = ""
    type: str = "inline"  # inline, external, or file
    validation_errors: List[Dict] = field(default_factory=list)
    
@dataclass
class CSSInventory:
    blocks: List[CSSBlock] = field(default_factory=list)
    stats: Dict = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    
    def add_block(self, block: CSSBlock):
        self.blocks.append(block)
    
    def generate_stats(self):
        self.stats = {
            "total_blocks": len(self.blocks),
            "by_type": {
                "inline": sum(1 for b in self.blocks if b.type == "inline"),
                "external": sum(1 for b in self.blocks if b.type == "external"),
                "file": sum(1 for b in self.blocks if b.type == "file")
            },
            "by_file_extension": {},
            "total_lines": sum(len(b.content.split('\n')) for b in self.blocks),
            "validation_status": {
                "valid": sum(1 for b in self.blocks if not b.validation_errors),
                "invalid": sum(1 for b in self.blocks if b.validation_errors)
            }
        }
        
        # Count by file extension
        for block in self.blocks:
            ext = os.path.splitext(block.file)[1]
            if ext in self.stats["by_file_extension"]:
                self.stats["by_file_extension"][ext] += 1
            else:
                self.stats["by_file_extension"][ext] = 1
                
    def to_json(self, path: Path):
        with open(path, 'w') as f:
            json.dump(asdict(self), f, indent=2)
            
    def to_markdown(self, path: Path):
        with open(path, 'w') as f:
            f.write(f"# CSS Inventory Report\n\n")
            f.write(f"Generated: {self.timestamp}\n\n")
            
            f.write("## Summary\n\n")
            f.write(f"- Total CSS blocks: {self.stats['total_blocks']}\n")
            f.write(f"- Total CSS lines: {self.stats['total_lines']}\n")
            f.write(f"- Inline styles: {self.stats['by_type']['inline']}\n")
            f.write(f"- External references: {self.stats['by_type']['external']}\n")
            f.write(f"- CSS files: {self.stats['by_type']['file']}\n")
            f.write(f"- Valid CSS blocks: {self.stats['validation_status']['valid']}\n")
            f.write(f"- Invalid CSS blocks: {self.stats['validation_status']['invalid']}\n\n")
            
            f.write("## CSS Blocks\n\n")
            for i, block in enumerate(self.blocks, 1):
                rel_path = os.path.relpath(block.file, PROJECT_ROOT)
                f.write(f"### Block {i}: {rel_path} (line {block.line_number})\n\n")
                f.write(f"**Type:** {block.type}\n\n")
                f.write("```css\n")
                f.write(block.content)
                f.write("\n```\n\n")
                
                if block.validation_errors:
                    f.write("**Validation Errors:**\n\n")
                    for error in block.validation_errors:
                        f.write(f"- Line {error.get('line', 'N/A')}: {error.get('message', 'Unknown error')}\n")
                    f.write("\n")
                else:
                    f.write("**Validation:** ✅ Passed\n\n")
                    
                if block.context:
                    f.write("**Context:**\n\n")
                    f.write("```python\n")
                    f.write(block.context)
                    f.write("\n```\n\n")
                f.write("---\n\n")
    
    def to_text(self, path: Path):
        with open(path, 'w') as f:
            f.write(f"📁 CSS Inventory Audit Report\n")
            f.write(f"📅 {self.timestamp}\n")
            f.write(f"🔍 Total Blocks: {self.stats['total_blocks']}\n\n")
            
            for i, block in enumerate(self.blocks, 1):
                rel_path = os.path.relpath(block.file, PROJECT_ROOT)
                f.write(f"--- Block #{i} ---\n")
                f.write(f"File: {rel_path}\n")
                f.write(f"Line: {block.line_number}\n")
                f.write(f"Type: {block.type}\n")
                
                if block.validation_errors:
                    f.write(f"Validation: ❌ {len(block.validation_errors)} error(s)\n")
                    for error in block.validation_errors:
                        f.write(f"  • Line {error.get('line', 'N/A')}: {error.get('message', 'Unknown error')}\n")
                else:
                    f.write("Validation: ✅ Passed\n")
                    
                f.write("CSS:\n" + block.content + "\n\n")

def find_css_in_file(file_path: str, inventory: CSSInventory):
    """Find CSS within Python files"""
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            content = file.read()
            lines = content.split('\n')
            
            # Pattern 1: Streamlit-specific st.markdown CSS pattern
            streamlit_pattern = re.compile(r"st\.markdown\(\s*r?['\"]{1,3}.*?<style.*?>(.*?)</style>.*?['\"]{1,3}", re.DOTALL)
            for match in streamlit_pattern.finditer(content):
                css_content = match.group(1)
                position = match.start()
                line_number = content[:position].count('\n') + 1
                
                # Get context (a few lines before and after)
                start_line = max(0, line_number - 3)
                end_line = min(len(lines), line_number + 3)
                context = '\n'.join(lines[start_line:end_line])
                
                inventory.add_block(CSSBlock(
                    file=file_path,
                    line_number=line_number,
                    content=css_content.strip(),
                    context=context,
                    type="inline"
                ))
            
            # Pattern 2: Generic style tags
            style_pattern = re.compile(r'<style>(.*?)</style>', re.DOTALL)
            for match in style_pattern.finditer(content):
                # Check if this isn't already captured by the streamlit pattern
                is_duplicate = False
                for st_match in streamlit_pattern.finditer(content):
                    if match.start() >= st_match.start() and match.end() <= st_match.end():
                        is_duplicate = True
                        break
                
                if not is_duplicate:
                    css_content = match.group(1)
                    position = match.start()
                    line_number = content[:position].count('\n') + 1
                    
                    start_line = max(0, line_number - 3)
                    end_line = min(len(lines), line_number + 3)
                    context = '\n'.join(lines[start_line:end_line])
                    
                    inventory.add_block(CSSBlock(
                        file=file_path,
                        line_number=line_number,
                        content=css_content.strip(),
                        context=context,
                        type="inline"
                    ))
                
            # Pattern 3: Find references to external CSS files
            css_ref_pattern = re.compile(r'(?:st\.markdown|st\.write)\s*\(\s*[\'"].*?\.css[\'"]')
            for match in css_ref_pattern.finditer(content):
                position = match.start()
                line_number = content[:position].count('\n') + 1
                
                start_line = max(0, line_number - 2)
                end_line = min(len(lines), line_number + 2)
                context = '\n'.join(lines[start_line:end_line])
                
                css_filename = re.search(r'[\'"](.+?\.css)[\'"]', match.group(0))
                if css_filename:
                    filename = css_filename.group(1)
                    dir_path = os.path.dirname(file_path)
                    potential_css_path = os.path.join(dir_path, filename)
                    
                    inventory.add_block(CSSBlock(
                        file=file_path,
                        line_number=line_number,
                        content=f"Reference to: {filename}",
                        context=context,
                        type="external"
                    ))
                    
                    # Try to find and include the referenced CSS file
                    if os.path.exists(potential_css_path):
                        with open(potential_css_path, 'r') as css_file:
                            css_content = css_file.read()
                            inventory.add_block(CSSBlock(
                                file=potential_css_path,
                                line_number=1,
                                content=css_content.strip(),
                                type="file"
                            ))
        except UnicodeDecodeError:
            # Skip binary files
            pass

def scan_directory(directory: Path, inventory: CSSInventory, extensions: List[str]):
    """Recursively scan the directory for files"""
    print(f"[INFO] Scanning directory: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1].lower()
            
            if file_ext == '.css':
                # Direct CSS file
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        content = f.read()
                        inventory.add_block(CSSBlock(
                            file=file_path,
                            line_number=1,
                            content=content.strip(),
                            type="file"
                        ))
                    except UnicodeDecodeError:
                        # Skip binary files
                        pass
            elif file_ext in extensions:
                # Python files (and potentially other files that might contain CSS)
                find_css_in_file(file_path, inventory)

import subprocess
import json
import tempfile

def validate_css(css_text):
    """Validate CSS using stylelint."""
    try:
        print(f"[INFO] Validating CSS block ({len(css_text)} chars)...")
        
        # Write CSS to temporary file
        with tempfile.NamedTemporaryFile('w', suffix='.css', delete=False) as temp_file:
            temp_file.write(css_text)
            temp_file.flush()
            
            # Run stylelint
            result = subprocess.run(
                ['stylelint', temp_file.name, '--format', 'json'],
                capture_output=True,
                text=True
            )
            
            # Clean up temporary file
            temp_file.close()
            os.unlink(temp_file.name)
            
            # Parse stylelint output
            if result.returncode == 0:
                return []  # No errors
                
            # Parse JSON output
            try:
                lint_results = json.loads(result.stdout)
                if not lint_results:
                    return [{"message": "Failed to parse CSS"}]
                    
                errors = []
                for result in lint_results:
                    if 'warnings' in result:
                        for warning in result['warnings']:
                            errors.append({
                                "message": warning['text'],
                                "line": warning['line'],
                                "column": warning['column'],
                                "severity": warning['severity']
                            })
                
                return errors
                
            except json.JSONDecodeError:
                return [{"message": "Failed to parse stylelint output"}]
                
    except Exception as e:
        print(f"[WARNING] CSS validation failed: {e}")
        return [{"message": f"Validation failed: {str(e)}"}]

def main():
    # Create logs directory if it doesn't exist
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    
    parser = argparse.ArgumentParser(description='Inventory CSS in the Grizly Streamlit app')
    parser.add_argument('--validate', action='store_true', help='Validate CSS with W3C validator')
    parser.add_argument('--formats', type=str, default='json,markdown,text', 
                        help='Output formats (default: json,markdown,text)')
    parser.add_argument('--extensions', type=str, default='.py,.streamlit', 
                        help='File extensions to scan (default: .py,.streamlit)')
    
    args = parser.parse_args()
    
    # Create inventory
    inventory = CSSInventory()
    
    # Parse extensions
    extensions = [ext.strip() for ext in args.extensions.split(',')]
    
    # Scan app directory
    scan_directory(APP_DIR, inventory, extensions)
    print(f"[INFO] Found {len(inventory.blocks)} CSS blocks in the Grizly app.")
    
    # Validate if requested
    if args.validate:
        print("[INFO] Starting CSS validation...")
        for block in inventory.blocks:
            if block.type != "external":  # Don't validate external references
                block.validation_errors = validate_css(block.content)
                if block.validation_errors:
                    print(f"[WARNING] Block in {os.path.relpath(block.file, PROJECT_ROOT)} (line {block.line_number}) has {len(block.validation_errors)} validation errors")
                else:
                    print(f"[INFO] Block in {os.path.relpath(block.file, PROJECT_ROOT)} (line {block.line_number}) passed validation")
    
    # Generate stats
    inventory.generate_stats()
    
    # Output results based on requested formats
    formats = [fmt.strip() for fmt in args.formats.split(',')]
    
    # Create timestamped folder for this run
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = LOGS_DIR / f"run_{timestamp}"
    run_dir.mkdir(exist_ok=True)
    
    if 'json' in formats:
        json_path = run_dir / "css_inventory.json"
        inventory.to_json(json_path)
        print(f"[INFO] JSON inventory written to: {json_path}")
        
    if 'markdown' in formats:
        md_path = run_dir / "css_inventory.md"
        inventory.to_markdown(md_path)
        print(f"[INFO] Markdown inventory written to: {md_path}")
        
    if 'text' in formats:
        txt_path = run_dir / "css_inventory.txt"
        inventory.to_text(txt_path)
        print(f"[INFO] Text report written to: {txt_path}")
    
    # Print summary
    print("\n=== Inventory Summary ===")
    print(f"Total CSS blocks found: {inventory.stats['total_blocks']}")
    print(f"- Inline styles: {inventory.stats['by_type']['inline']}")
    print(f"- External references: {inventory.stats['by_type']['external']}")
    print(f"- CSS files: {inventory.stats['by_type']['file']}")
    if args.validate:
        print(f"- Valid CSS blocks: {inventory.stats['validation_status']['valid']}")
        print(f"- Invalid CSS blocks: {inventory.stats['validation_status']['invalid']}")
    print(f"Total CSS lines: {inventory.stats['total_lines']}")
    print(f"Reports saved to: {run_dir}")
    
if __name__ == "__main__":
    main()


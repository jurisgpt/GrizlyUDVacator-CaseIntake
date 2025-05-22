import argparse
import os
from typing import List, Set

# Common directories and files to ignore
DEFAULT_IGNORE_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    "docs", # Often contains generated or non-primary source files
    "tests", # Usually not part of the core application to analyze/document by these tools
    "site-packages",
    ".vscode",
    ".idea",
    "migrations", # Common in Django/Flask
    "static", # Often contains non-Python assets
    "templates", # Often contains non-Python assets
}
DEFAULT_IGNORE_FILES = {
    ".DS_Store",
    "*.pyc",
    "*.log",
    "*.tmp",
    "*.swp",
    "*.swo",
    "*.bak",
    "*.egg-info",
    "requirements.txt", # Or similar dependency files
    "setup.py",
    "README.md",
    "LICENSE",
}

def parse_common_script_args(description: str) -> argparse.ArgumentParser:
    """
    Creates an ArgumentParser with common arguments for analysis/documentation scripts.

    Args:
        description: The description of the script to be shown in help messages.

    Returns:
        An argparse.ArgumentParser instance with common arguments added.
        The calling script can then add its own specific arguments.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "project_path",
        help="Path to the Python project (directory or specific file) to analyze/document."
    )
    parser.add_argument(
        "--ignore-dirs",
        nargs="*",
        default=list(DEFAULT_IGNORE_DIRS),
        help="List of directory names to ignore. Supports simple glob patterns (e.g., 'test*')."
    )
    parser.add_argument(
        "--ignore-files",
        nargs="*",
        default=list(DEFAULT_IGNORE_FILES),
        help="List of file names to ignore. Supports simple glob patterns (e.g., '*.test.py')."
    )
    # Scripts should add their own --output arguments as they are specific.
    return parser

def is_path_ignored(path: str, ignore_dirs: Set[str], ignore_files: Set[str]) -> bool:
    """
    Checks if a given path (file or directory) should be ignored based on ignore lists.
    Simple glob-like matching for names is supported (e.g., "test*").
    """
    import fnmatch # Use fnmatch for simple glob pattern matching

    name = os.path.basename(path)

    # Check against directory ignore patterns
    if os.path.isdir(path):
        for pattern in ignore_dirs:
            if fnmatch.fnmatch(name, pattern):
                return True
    # Check against file ignore patterns
    else: # It's a file
        for pattern in ignore_files:
            if fnmatch.fnmatch(name, pattern):
                return True
    
    # Also check if any part of the path matches an ignored directory name
    # This helps ignore files within ignored directories like .venv/lib/site-packages/some_file.py
    path_parts = path.split(os.sep)
    for part in path_parts:
        for pattern in ignore_dirs: # Check against dir patterns
            if fnmatch.fnmatch(part, pattern):
                return True
                
    return False

def discover_python_files(project_path: str, ignore_dirs: Set[str], ignore_files: Set[str]) -> List[str]:
    """
    Discovers all Python files in a project directory, respecting ignore lists.
    
    Args:
        project_path: The root directory of the project.
        ignore_dirs: A set of directory names to ignore.
        ignore_files: A set of file names to ignore.

    Returns:
        A list of paths to Python files.
    """
    python_files = []
    if os.path.isfile(project_path) and project_path.endswith(".py"):
        if not is_path_ignored(project_path, ignore_dirs, ignore_files):
            python_files.append(project_path)
        return python_files
        
    if not os.path.isdir(project_path):
        print(f"Warning: Project path {project_path} is not a valid directory or Python file.")
        return []

    for root, dirs, files in os.walk(project_path, topdown=True):
        # Filter out ignored directories before further traversal
        dirs[:] = [d for d in dirs if not is_path_ignored(os.path.join(root, d), ignore_dirs, ignore_files)]
        
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                if not is_path_ignored(file_path, ignore_dirs, ignore_files):
                    python_files.append(file_path)
    return python_files

if __name__ == '__main__':
    # Example usage:
    parser = parse_common_script_args("Test script for analysis_utils.py")
    parser.add_argument("--specific_arg", help="A specific argument for this test script.")
    args = parser.parse_args()

    print(f"Project Path: {args.project_path}")
    print(f"Ignore Dirs: {args.ignore_dirs}")
    print(f"Ignore Files: {args.ignore_files}")
    if args.specific_arg:
        print(f"Specific Arg: {args.specific_arg}")

    if os.path.exists(args.project_path):
        print(f"\nTesting is_path_ignored for 'test_dir/.venv/some_file.py':")
        print(is_path_ignored("test_dir/.venv/some_file.py", set(args.ignore_dirs), set(args.ignore_files)))
        
        print(f"\nTesting is_path_ignored for 'app/main.py':")
        print(is_path_ignored("app/main.py", set(args.ignore_dirs), set(args.ignore_files)))

        print(f"\nTesting is_path_ignored for 'app/tests/test_main.py':")
        print(is_path_ignored("app/tests/test_main.py", set(args.ignore_dirs), set(args.ignore_files)))
        
        print(f"\nDiscovering Python files in '{args.project_path}':")
        py_files = discover_python_files(args.project_path, set(args.ignore_dirs), set(args.ignore_files))
        for f in py_files:
            print(f"  - {f}")
    else:
        print(f"Project path '{args.project_path}' does not exist. Skipping file discovery tests.")

# To run this example, save as analysis_utils.py and run:
# python analysis_utils.py . --specific_arg test_value --ignore-dirs .git .venv my_custom_ignore --ignore-files *.tmp
# python analysis_utils.py your_project_path --specific_arg test_value
# python analysis_utils.py streamlit-analyzer-fixed.py
# (The last one will treat the file itself as the project_path)

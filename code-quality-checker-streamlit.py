#!/usr/bin/env python3
"""
Streamlit Static Analysis Tool

This script runs multiple static analysis tools on a Streamlit project and generates
a consolidated summary report without making any changes to the codebase.

Tools used:
- pylint: Detects misuse of widgets, naming issues, improper conditionals
- mypy: Ensures Streamlit inputs are properly typed
- bandit: Warns about unsafe use of secrets and security issues
- vulture: Finds unused UI elements or logic blocks
- flake8: Helps with code style readability
"""

import os
import sys
import subprocess
import argparse
import json
from datetime import datetime
from typing import Dict, List, Any, Tuple

# ANSI color codes for terminal output
COLORS = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
    "BOLD": "\033[1m",
}

# Tool configurations with importance ratings
TOOLS = {
    "pylint": {
        "cmd": "pylint",
        "args": ["--output-format=json"],
        "importance": "🔥 Essential",
        "description": "Detects misuse of widgets, naming issues, improper conditionals, repeated widget declarations",
        "parse_func": "parse_pylint"
    },
    "mypy": {
        "cmd": "mypy",
        "args": ["--json-report", "-"],
        "importance": "✅ Very helpful",
        "description": "Ensures Streamlit inputs (e.g. `st.date_input()`) are properly typed and used downstream",
        "parse_func": "parse_mypy"
    },
    "bandit": {
        "cmd": "bandit",
        "args": ["-f", "json", "-r"],
        "importance": "✅ Important",
        "description": "Warns about unsafe use of secrets, unsafe file I/O, and injection risks",
        "parse_func": "parse_bandit"
    },
    "vulture": {
        "cmd": "vulture",
        "args": [],
        "importance": "⚠️ Nice to have",
        "description": "Finds unused UI elements or logic blocks (but may flag false positives due to Streamlit reactivity)",
        "parse_func": "parse_vulture"
    },
    "flake8": {
        "cmd": "flake8",
        "args": ["--format=json"],
        "importance": "✅ Helps with readability",
        "description": "Keeps formatting, line breaks, and indentations clean",
        "parse_func": "parse_flake8"
    }
}

# Streamlit specific issue messages to highlight
STREAMLIT_KEYWORDS = [
    "st.", "streamlit", "session_state", "widget", "duplicate", 
    "key", "input", "form", "sidebar", "container"
]

def parse_pylint(output: str) -> List[Dict[str, Any]]:
    """Parse pylint JSON output"""
    try:
        results = json.loads(output)
        issues = []
        for item in results:
            issues.append({
                "file": item.get("path", ""),
                "line": item.get("line", 0),
                "severity": item.get("type", ""),
                "message": item.get("message", ""),
                "code": item.get("symbol", "")
            })
        return issues
    except json.JSONDecodeError:
        # Handle case where pylint doesn't output valid JSON
        return []

def parse_mypy(output: str) -> List[Dict[str, Any]]:
    """Parse mypy JSON output"""
    try:
        results = json.loads(output)
        issues = []
        if "data" in results and "errors" in results["data"]:
            for error in results["data"]["errors"]:
                issues.append({
                    "file": error.get("file", ""),
                    "line": error.get("line", 0),
                    "severity": "error",
                    "message": error.get("message", ""),
                    "code": ""
                })
        return issues
    except json.JSONDecodeError:
        return []

def parse_bandit(output: str) -> List[Dict[str, Any]]:
    """Parse bandit JSON output"""
    try:
        results = json.loads(output)
        issues = []
        if "results" in results:
            for result in results["results"]:
                issues.append({
                    "file": result.get("filename", ""),
                    "line": result.get("line_number", 0),
                    "severity": result.get("issue_severity", ""),
                    "message": result.get("issue_text", ""),
                    "code": result.get("test_id", "")
                })
        return issues
    except json.JSONDecodeError:
        return []

def parse_flake8(output: str) -> List[Dict[str, Any]]:
    """Parse flake8 JSON output"""
    try:
        results = json.loads(output)
        issues = []
        for file_path, file_errors in results.items():
            for error in file_errors:
                issues.append({
                    "file": file_path,
                    "line": error.get("line_number", 0),
                    "severity": "style",
                    "message": error.get("text", ""),
                    "code": error.get("code", "")
                })
        return issues
    except json.JSONDecodeError:
        return []

def parse_vulture(output: str) -> List[Dict[str, Any]]:
    """Parse vulture text output"""
    issues = []
    for line in output.splitlines():
        parts = line.split(":", 2)
        if len(parts) >= 3:
            file_path = parts[0]
            try:
                line_num = int(parts[1])
                message = parts[2].strip()
                issues.append({
                    "file": file_path,
                    "line": line_num,
                    "severity": "unused",
                    "message": message,
                    "code": ""
                })
            except ValueError:
                continue
    return issues

def run_tool(tool_name: str, target_path: str) -> Tuple[List[Dict[str, Any]], bool]:
    """Run a tool and return parsed results and success status"""
    tool_config = TOOLS[tool_name]
    cmd = [tool_config["cmd"]] + tool_config["args"] + [target_path]
    
    print(f"Running {COLORS['BOLD']}{tool_name}{COLORS['ENDC']}...")
    
    try:
        # Use subprocess to run the command with shell=False for security
        process = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            check=False,
            shell=False
        )
        
        # Check if the tool was installed and ran successfully
        if process.returncode != 0 and "not found" in process.stderr:
            print(f"{COLORS['RED']}Error: {tool_name} is not installed.{COLORS['ENDC']}")
            print(f"Install with: pip install {tool_name}")
            return [], False
            
        # Parse the output using the appropriate function
        parse_function = globals()[tool_config["parse_func"]]
        return parse_function(process.stdout), True
        
    except Exception as e:
        print(f"{COLORS['RED']}Error running {tool_name}: {str(e)}{COLORS['ENDC']}")
        return [], False

def is_streamlit_related(issue: Dict[str, Any]) -> bool:
    """Check if an issue is Streamlit-related based on keywords"""
    message = issue.get("message", "").lower()
    return any(keyword.lower() in message for keyword in STREAMLIT_KEYWORDS)

def generate_summary(results: Dict[str, List[Dict[str, Any]]]) -> str:
    """Generate a summary report from all tool results"""
    report = []
    
    # Add header
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report.append("# Streamlit Static Analysis Report")
    report.append(f"Generated: {timestamp}\n")
    
    # Add tool overview
    report.append("## Tools Summary")
    for tool_name, tool_config in TOOLS.items():
        tool_ran = tool_name in results
        tool_status = "✓ Ran successfully" if tool_ran else "✗ Failed to run"
        report.append(f"- **{tool_name}** ({tool_config['importance']}): {tool_status}")
    report.append("")
    
    # Add issue highlights section
    streamlit_issues = []
    for tool_name, issues in results.items():
        for issue in issues:
            if is_streamlit_related(issue):
                streamlit_issues.append({
                    "tool": tool_name,
                    **issue
                })
    
    # Highlight Streamlit-specific issues first
    if streamlit_issues:
        report.append("## 🔥 Streamlit-Specific Issues")
        for issue in streamlit_issues:
            file_loc = f"{issue['file']}:{issue['line']}"
            report.append(f"- **{issue['tool']}** ({file_loc}): {issue['message']}")
        report.append("")
    
    # Add detailed results for each tool
    report.append("## Detailed Results")
    for tool_name, issues in results.items():
        tool_config = TOOLS[tool_name]
        
        report.append(f"### {tool_name} ({tool_config['importance']})")
        report.append(f"{tool_config['description']}")
        
        if not issues:
            report.append("\n*No issues found.*\n")
            continue
            
        report.append("")
        
        # Group issues by file
        files = {}
        for issue in issues:
            file_path = issue.get("file", "unknown")
            if file_path not in files:
                files[file_path] = []
            files[file_path].append(issue)
        
        # Report issues by file
        for file_path, file_issues in files.items():
            report.append(f"#### {os.path.basename(file_path)}")
            for issue in file_issues:
                line_num = issue.get("line", 0)
                code = issue.get("code", "")
                message = issue.get("message", "")
                severity = issue.get("severity", "").upper()
                
                code_str = f"[{code}] " if code else ""
                report.append(f"- Line {line_num}: {code_str}{message} ({severity})")
            report.append("")
    
    # Add recommendations section
    report.append("## Recommendations")
    report.append("Based on the analysis, consider these Streamlit-specific best practices:")
    report.append("")
    report.append("1. **Widget Duplication**: Always use unique `key` parameters for interactive elements")
    report.append("2. **State Management**: Properly initialize `session_state` variables before use")
    report.append("3. **Form Handling**: Keep form widgets and submission handling together")
    report.append("4. **Execution Flow**: Remember Streamlit reruns the entire script on each interaction")
    report.append("5. **Type Safety**: Add type hints to improve readability and catch errors early")
    
    return "\n".join(report)

def save_report(report: str, output_path: str) -> None:
    """Save the report to a file"""
    with open(output_path, "w") as f:
        f.write(report)
    print(f"{COLORS['GREEN']}Report saved to: {output_path}{COLORS['ENDC']}")

def main():
    """Main function to run the tools and generate the report"""
    parser = argparse.ArgumentParser(
        description="Run static analysis tools on a Streamlit project"
    )
    parser.add_argument(
        "project_path", 
        help="Path to the Streamlit project to analyze"
    )
    parser.add_argument(
        "--output", "-o",
        default="streamlit_analysis_report.md",
        help="Output path for the report (default: streamlit_analysis_report.md)"
    )
    parser.add_argument(
        "--tools",
        default="all",
        help="Comma-separated list of tools to run (default: all)"
    )
    
    args = parser.parse_args()
    
    # Check if project path exists
    if not os.path.exists(args.project_path):
        print(f"{COLORS['RED']}Error: Project path does not exist: {args.project_path}{COLORS['ENDC']}")
        sys.exit(1)
    
    # Determine which tools to run
    tools_to_run = list(TOOLS.keys()) if args.tools == "all" else args.tools.split(",")
    
    # Run each tool and collect results
    results = {}
    for tool_name in tools_to_run:
        if tool_name not in TOOLS:
            print(f"{COLORS['YELLOW']}Warning: Unknown tool: {tool_name}{COLORS['ENDC']}")
            continue
            
        tool_results, success = run_tool(tool_name, args.project_path)
        if success:
            results[tool_name] = tool_results
            issue_count = len(tool_results)
            if issue_count > 0:
                print(f"  {COLORS['YELLOW']}Found {issue_count} issues{COLORS['ENDC']}")
            else:
                print(f"  {COLORS['GREEN']}No issues found{COLORS['ENDC']}")
    
    # Generate and save the report
    report = generate_summary(results)
    save_report(report, args.output)
    
    # Print summary
    total_issues = sum(len(issues) for issues in results.values())
    streamlit_issues = sum(
        1 for tool, issues in results.items() 
        for issue in issues 
        if is_streamlit_related(issue)
    )
    
    print(f"\n{COLORS['BOLD']}Analysis Complete:{COLORS['ENDC']}")
    print(f"- Total issues found: {total_issues}")
    print(f"- Streamlit-specific issues: {streamlit_issues}")
    print(f"- Report saved to: {args.output}")

if __name__ == "__main__":
    main()


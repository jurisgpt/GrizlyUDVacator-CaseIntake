#!/usr/bin/env python3
"""
Streamlit Static Analysis Tool

This script runs multiple static analysis tools on a Streamlit project and generates
a comprehensive report without making any changes to the codebase.

Fixed version that avoids multiprocessing pickling issues.
"""

import os
import sys
import subprocess
# import argparse # No longer directly used for parser creation here
import json
import time
from datetime import datetime
from typing import Dict, List, Any, Tuple, Optional
import concurrent.futures

from analysis_utils import parse_common_script_args, discover_python_files, is_path_ignored, DEFAULT_IGNORE_DIRS, DEFAULT_IGNORE_FILES # Import discover_python_files and is_path_ignored

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
        "parse_func": "parse_pylint",
        "raw_cmd": "pylint",
        "timeout": 60
    },
    "mypy": {
        "cmd": "mypy",
        "args": ["--json-report", "-"],
        "importance": "✅ Very helpful",
        "description": "Ensures Streamlit inputs (e.g. `st.date_input()`) are properly typed and used downstream",
        "parse_func": "parse_mypy",
        "raw_cmd": "mypy",
        "timeout": 60
    },
    "bandit": {
        "cmd": "bandit",
        "args": ["-f", "json", "-r", "--exclude", ".venv,venv,node_modules,__pycache__,dist,build"],
        "importance": "✅ Important",
        "description": "Warns about unsafe use of secrets, unsafe file I/O, and injection risks",
        "parse_func": "parse_bandit",
        "raw_cmd": "bandit -r --exclude .venv,venv,node_modules,__pycache__,dist,build",
        "timeout": 180
    },
    "vulture": {
        "cmd": "vulture",
        "args": [],
        "importance": "⚠️ Nice to have",
        "description": "Finds unused UI elements or logic blocks (but may flag false positives due to Streamlit reactivity)",
        "parse_func": "parse_vulture",
        "raw_cmd": "vulture",
        "timeout": 60
    },
    "flake8": {
        "cmd": "flake8",
        "args": ["--format=json"],
        "importance": "✅ Helps with readability",
        "description": "Keeps formatting, line breaks, and indentations clean",
        "parse_func": "parse_flake8",
        "raw_cmd": "flake8",
        "timeout": 60
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

def run_tool(tool_name: str, target_path: str) -> Tuple[str, List[Dict[str, Any]], bool, Optional[str], float]:
    """Run a tool and return name, parsed results, success status, raw output, and execution time"""
    tool_config = TOOLS[tool_name]
    cmd = [tool_config["cmd"]] + tool_config["args"] + [target_path]
    raw_cmd = tool_config["raw_cmd"].split() + [target_path]
    timeout = tool_config["timeout"]
    
    print(f"Running {COLORS['BOLD']}{tool_name}{COLORS['ENDC']}...")
    
    start_time = time.time()
    try:
        # Use subprocess with timeout and shell=False for security
        process = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            check=False,
            timeout=timeout,
            shell=False
        )
        
        # Get raw output
        try:
            raw_process = subprocess.run(
                raw_cmd,
                capture_output=True,
                text=True,
                check=False,
                timeout=timeout,
                shell=False
            )
            raw_output = raw_process.stdout
        except Exception as e:
            print(f"{COLORS['YELLOW']}Warning: Failed to get raw output for {tool_name}: {str(e)}{COLORS['ENDC']}")
            raw_output = ""
        
        execution_time = time.time() - start_time
        
        # Check if the tool was installed and ran successfully
        if process.returncode != 0 and "not found" in process.stderr:
            print(f"{COLORS['RED']}Error: {tool_name} is not installed.{COLORS['ENDC']}")
            print(f"Install with: pip install {tool_name}")
            return tool_name, [], False, f"ERROR: {tool_name} is not installed. Run: pip install {tool_name}", execution_time
            
        # Parse the output using the appropriate function
        try:
            parse_function = globals()[tool_config["parse_func"]]
            issues = parse_function(process.stdout)
        except Exception as e:
            print(f"{COLORS['RED']}Error parsing {tool_name} output: {str(e)}{COLORS['ENDC']}")
            return tool_name, [], False, raw_output, execution_time
        
        issue_count = len(issues)
        if issue_count > 0:
            print(f"  {COLORS['YELLOW']}{tool_name}: Found {issue_count} issues{COLORS['ENDC']} ({execution_time:.2f}s)")
        else:
            print(f"  {COLORS['GREEN']}{tool_name}: No issues found{COLORS['ENDC']} ({execution_time:.2f}s)")
            
        return tool_name, issues, True, raw_output, execution_time
        
    except subprocess.TimeoutExpired:
        execution_time = time.time() - start_time
        print(f"{COLORS['YELLOW']}Warning: {tool_name} timed out after {timeout} seconds.{COLORS['ENDC']}")
        return tool_name, [], False, f"TIMEOUT: {tool_name} analysis timed out after {timeout} seconds.", execution_time
    
    except Exception as e:
        execution_time = time.time() - start_time
        print(f"{COLORS['RED']}Error running {tool_name}: {str(e)}{COLORS['ENDC']}")
        return tool_name, [], False, f"ERROR: {str(e)}", execution_time

def is_streamlit_related(issue: Dict[str, Any]) -> bool:
    """Check if an issue is Streamlit-related based on keywords"""
    message = issue.get("message", "").lower()
    return any(keyword.lower() in message for keyword in STREAMLIT_KEYWORDS)

def generate_text_report(results: Dict[str, List[Dict[str, Any]]], raw_outputs: Dict[str, str], 
                         execution_times: Dict[str, float]) -> str:
    """Generate a text report from all tool results"""
    report = []
    
    # Add header
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report.append("STREAMLIT STATIC ANALYSIS REPORT")
    report.append("=" * 40)
    report.append(f"Generated: {timestamp}")
    report.append("")
    
    # Add tool overview
    report.append("TOOLS SUMMARY")
    report.append("-" * 40)
    for tool_name, tool_config in TOOLS.items():
        if tool_name in results:
            issue_count = len(results[tool_name])
            exec_time = execution_times.get(tool_name, 0)
            report.append(f"{tool_name} ({tool_config['importance']}): {issue_count} issues found in {exec_time:.2f}s")
        else:
            report.append(f"{tool_name} ({tool_config['importance']}): Not run")
    report.append("")
    
    # Add streamlit-specific issues section
    streamlit_issues = []
    for tool_name, issues in results.items():
        for issue in issues:
            if is_streamlit_related(issue):
                streamlit_issues.append({
                    "tool": tool_name,
                    **issue
                })
    
    if streamlit_issues:
        report.append("STREAMLIT-SPECIFIC ISSUES")
        report.append("-" * 40)
        for issue in streamlit_issues:
            file_loc = f"{issue['file']}:{issue['line']}"
            report.append(f"[{issue['tool']}] {file_loc}: {issue['message']}")
        report.append("")
    
    # Add detailed results for each tool
    report.append("DETAILED RESULTS")
    report.append("=" * 40)
    
    for tool_name in sorted(results.keys()):
        raw_output = raw_outputs.get(tool_name, "")
        tool_issues = results.get(tool_name, [])
        
        report.append("")
        report.append(f"{tool_name.upper()} OUTPUT")
        report.append("-" * 40)
        
        if raw_output:
            report.append(raw_output)
        elif not tool_issues:
            report.append("No issues found.")
        else:
            for issue in tool_issues:
                file_path = issue.get("file", "unknown")
                line_num = issue.get("line", 0)
                severity = issue.get("severity", "")
                message = issue.get("message", "")
                code = issue.get("code", "")
                
                code_str = f"[{code}] " if code else ""
                report.append(f"{file_path}:{line_num}: {code_str}{message} ({severity})")
        
        report.append("")
    
    # Add recommendations section
    report.append("")
    report.append("STREAMLIT RECOMMENDATIONS")
    report.append("=" * 40)
    report.append("Based on the analysis, consider these Streamlit-specific best practices:")
    report.append("")
    report.append("1. Widget Duplication: Always use unique 'key' parameters for interactive elements")
    report.append("2. State Management: Properly initialize session_state variables before use")
    report.append("3. Form Handling: Keep form widgets and submission handling together")
    report.append("4. Execution Flow: Remember Streamlit reruns the entire script on each interaction")
    report.append("5. Type Safety: Add type hints to improve readability and catch errors early")
    
    return "\n".join(report)

def generate_markdown_report(results: Dict[str, List[Dict[str, Any]]], 
                             execution_times: Dict[str, float]) -> str:
    """Generate a Markdown report from all tool results"""
    report = []
    
    # Add header
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report.append("# Streamlit Static Analysis Report")
    report.append(f"Generated: {timestamp}\n")
    
    # Add tool overview
    report.append("## Tools Summary")
    for tool_name, tool_config in TOOLS.items():
        tool_ran = tool_name in results and results[tool_name] is not None # Check if results exist for the tool
        exec_time_str = f" ({execution_times.get(tool_name, 0):.2f}s)" if tool_name in execution_times else ""
        
        # Determine status message
        status_message = ""
        if tool_name in execution_times and execution_times[tool_name] is not None: # Tool was attempted
            if tool_ran and results[tool_name]:
                issue_count = len(results[tool_name])
                status_message = f"{issue_count} issues found"
            elif tool_ran and not results[tool_name]: # Ran successfully, no issues
                 status_message = "No issues found"
            else: # Attempted but failed to produce results (e.g. not installed, error during run)
                status_message = "✗ Failed to run or no output"
        else: # Tool was not selected to run or not even attempted
            status_message = "Not run"
            
        report.append(f"- **{tool_name}** ({tool_config['importance']}): {status_message}{exec_time_str}")
    report.append("")
    
    # Add Streamlit-specific issues section
    streamlit_issues_list = []
    for tool_name, issues_list in results.items():
        if issues_list is None: continue # Skip if tool failed to produce results
        for issue in issues_list:
            if is_streamlit_related(issue):
                streamlit_issues_list.append({
                    "tool": tool_name,
                    **issue
                })
    
    if streamlit_issues_list:
        report.append("## 🔥 Streamlit-Specific Issues")
        for issue in streamlit_issues_list:
            file_loc = f"{issue['file']}:{issue['line']}"
            report.append(f"- **{issue['tool']}** ({file_loc}): {issue['message']}")
        report.append("")
    
    # Add detailed results for each tool
    report.append("## Detailed Results")
    
    sorted_tool_names = sorted(
        TOOLS.keys(),
        # Sort by: 1. Not attempted/failed early, 2. Attempted but no issues, 3. Attempted with issues, then alphabetically
        key=lambda t: (t not in execution_times, t not in results or not results.get(t), t)
    )

    for tool_name in sorted_tool_names:
        tool_config = TOOLS[tool_name]
        report.append(f"### {tool_name} ({tool_config['importance']})")
        report.append(f"*{tool_config['description']}*")
        
        if tool_name not in execution_times: # Tool was not even attempted
            report.append("\n*Tool not selected to run.*\n")
            continue
        if tool_name not in results or results[tool_name] is None: # Tool attempted but failed or no output
            report.append("\n*Tool did not produce results (e.g., not installed, error during execution, or timed out).*\n")
            continue
        if not results[tool_name]: # Tool ran successfully, no issues found
            report.append("\n*No issues found.*\n")
            continue
            
        report.append("")
        
        issues = results[tool_name]
        files = {}
        for issue in issues:
            file_path = issue.get("file", "unknown_file")
            if file_path.startswith("./"):
                file_path = file_path[2:]
            if file_path not in files:
                files[file_path] = []
            files[file_path].append(issue)
        
        for file_path, file_issues in sorted(files.items()):
            # Using os.path.basename for cleaner display, assuming file_path is a valid path string
            report.append(f"#### `{os.path.basename(file_path)}`") 
            for issue in sorted(file_issues, key=lambda x: x.get("line", 0)):
                line_num = issue.get("line", 0)
                code = issue.get("code", "")
                message = issue.get("message", "")
                severity = issue.get("severity", "").upper()
                severity_marker = ""
                if severity == "ERROR" or "HIGH" in severity:
                    severity_marker = "🔴 "
                elif severity == "WARNING" or "MEDIUM" in severity:
                    severity_marker = "🟡 "
                elif "LOW" in severity or severity == "STYLE" or severity == "CONVENTION" or severity == "REFACTOR":
                    severity_marker = "🟢 "
                elif severity == "UNUSED":
                    severity_marker = "⚪ "


                code_str = f" `{code}`" if code else ""
                report.append(f"- Line {line_num}:{code_str} {severity_marker}{message} *({severity.lower()})*")
            report.append("")
    
    # Add recommendations section
    report.append("## Recommendations")
    report.append("Based on the analysis, consider these Streamlit-specific best practices:")
    report.append("")
    report.append("1. **Widget Duplication**: Always use unique `key` parameters for interactive elements.")
    report.append("2. **State Management**: Properly initialize `session_state` variables before use.")
    report.append("3. **Form Handling**: Keep form widgets and submission handling together.")
    report.append("4. **Execution Flow**: Remember Streamlit reruns the entire script on each interaction.")
    report.append("5. **Type Safety**: Add type hints to improve readability and catch errors early.")
    
    return "\n".join(report)

def save_report(report: str, output_path: str) -> None:
    """Save the report to a file with UTF-8 encoding"""
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"{COLORS['GREEN']}Report saved to: {output_path}{COLORS['ENDC']}")
    except Exception as e:
        print(f"{COLORS['RED']}Error saving report: {str(e)}{COLORS['ENDC']}")

def main():
    """Main function"""
    # Use the common argument parser
    parser = parse_common_script_args("Streamlit Static Analysis Tool")

    # Add script-specific arguments
    parser.add_argument(
        "--output", "-o",
        default="Code-Quality-Report.txt",
        help="Output path for the report (default: Code-Quality-Report.txt)"
    )
    parser.add_argument(
        "--tools",
        default="all",
        help="Comma-separated list of tools to run (default: all)"
    )
    parser.add_argument(
        "--exclude-bandit",
        action="store_true",
        help="Exclude bandit from the analysis (runs much faster)"
    )
    parser.add_argument(
        "--sequential",
        action="store_true",
        help="Run tools sequentially instead of in parallel"
    )
    parser.add_argument(
        "--markdown_output",
        default=None,
        help="Output path for the Markdown report (e.g., report.md). If not provided, no Markdown report is generated."
    )
    
    args = parser.parse_args()
    
    # Check if project path exists
    if not os.path.exists(args.project_path):
        print(f"{COLORS['RED']}Error: Project path '{args.project_path}' does not exist.{COLORS['ENDC']}")
        sys.exit(1)
    
    # Determine which tools to run
    tools_to_run = list(TOOLS.keys()) if args.tools == "all" else args.tools.split(",")
    
    # Exclude bandit if specified
    if args.exclude_bandit and "bandit" in tools_to_run:
        tools_to_run.remove("bandit")
        print(f"{COLORS['YELLOW']}Note: Bandit excluded from analysis{COLORS['ENDC']}")
    
    # Run tools and collect results
    results = {}
    raw_outputs = {}
    execution_times = {}
    
    start_time = time.time()
    
    if args.sequential:
        # Sequential execution
        print(f"{COLORS['BLUE']}Running {len(tools_to_run)} tools sequentially...{COLORS['ENDC']}")
        
        for tool_name in tools_to_run:
            if tool_name not in TOOLS:
                print(f"{COLORS['YELLOW']}Warning: Unknown tool: {tool_name}{COLORS['ENDC']}")
                continue
                
            # For streamlit-analyzer-fixed, we pass the project_path directly to tools
            # The discover_python_files and is_path_ignored are not directly used here for filtering
            # files before passing to tools like pylint, mypy etc. as these tools handle
            # path recursion and some have their own ignore mechanisms.
            # However, the project_path from common args is used.
            name, issues, success, raw_output, exec_time = run_tool(tool_name, args.project_path)
            if success: # Tool ran and parsed successfully
                results[name] = issues
            # Store raw_output only if the tool was attempted, regardless of success in parsing
            # This helps in debugging or seeing partial output for failed tools.
            if raw_output is not None: 
                raw_outputs[name] = raw_output
            else: # Ensure there's a placeholder if raw_output was None (e.g. tool not found)
                raw_outputs[name] = f"Tool {tool_name} did not produce any output or failed to run."

            execution_times[name] = exec_time
    else:
        # Parallel execution using ThreadPoolExecutor
        print(f"{COLORS['BLUE']}Running {len(tools_to_run)} tools in parallel...{COLORS['ENDC']}")
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # As above, project_path is passed directly.
            future_to_tool = {
                executor.submit(run_tool, tool_name, args.project_path): tool_name 
                for tool_name in tools_to_run if tool_name in TOOLS
            }
            
            for future in concurrent.futures.as_completed(future_to_tool):
                name, issues, success, raw_output, exec_time = future.result()
                if success: # Tool ran and parsed successfully
                    results[name] = issues
                # Store raw_output if available
                if raw_output is not None:
                    raw_outputs[name] = raw_output
                else:
                    raw_outputs[name] = f"Tool {name} did not produce any output or failed to run."
                    
                execution_times[name] = exec_time
    
    total_time = time.time() - start_time
    
    # Generate and save the report
    report = generate_text_report(results, raw_outputs, execution_times)
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
    print(f"- Total execution time: {total_time:.2f} seconds")

    # Generate and save Markdown report if requested
    if args.markdown_output:
        # Ensure all tools attempted have a placeholder in results if they failed, for consistent reporting
        # The run_tool function already returns raw_output for failed tools, which isn't directly used here
        # but execution_times tracks all attempted tools.
        # The generate_markdown_report function now handles cases where results[tool_name] might be None or missing.
        markdown_report = generate_markdown_report(results, execution_times)
        save_report(markdown_report, args.markdown_output)
        # print(f"{COLORS['GREEN']}Markdown report saved to: {args.markdown_output}{COLORS['ENDC']}") # Already printed by save_report

if __name__ == "__main__":
    main()

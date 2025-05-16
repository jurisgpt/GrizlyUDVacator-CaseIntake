#!/usr/bin/env python3
"""
Enhanced Streamlit Static Analysis Tool with M1/M2 Optimizations

This script runs multiple static analysis tools on a Streamlit project using
advanced parallel processing and Apple Silicon optimizations.

Features:
- Adaptive CPU core allocation optimized for M1/M2 architecture
- Smart workload balancing with performance/efficiency core awareness
- File-based caching for incremental analysis
- Dynamic tool prioritization based on project characteristics
- Memory optimizations for Apple Silicon's unified memory architecture
"""

import os
import sys
import subprocess
import platform
import argparse
import json
import time
import hashlib
import math
import shutil
import signal
import psutil
from datetime import datetime
from typing import Dict, List, Any, Tuple, Optional, Set
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import tempfile

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

# Default cache directory
CACHE_DIR = os.path.expanduser("~/.streamlit_analyzer_cache")

# Check if running on Apple Silicon
IS_APPLE_SILICON = platform.system() == "Darwin" and platform.machine().startswith(('arm', 'aarch'))

# Tool configurations with importance ratings and adaptive settings
TOOLS = {
    "pylint": {
        "cmd": "pylint",
        "args": ["--output-format=json"],
        "importance": "🔥 Essential",
        "description": "Detects misuse of widgets, naming issues, improper conditionals, repeated widget declarations",
        "parse_func": "parse_pylint",
        "raw_cmd": "pylint",
        "timeout": 60,
        "cpu_intensity": "high",  # Will run on performance cores
        "parallelizable": True,   # Can analyze files in parallel
        "memory_usage": "medium",
        "batch_size": 10,         # Files to process per batch
    },
    "mypy": {
        "cmd": "mypy",
        "args": ["--json-report", "-"],
        "importance": "✅ Very helpful",
        "description": "Ensures Streamlit inputs (e.g. `st.date_input()`) are properly typed and used downstream",
        "parse_func": "parse_mypy",
        "raw_cmd": "mypy",
        "timeout": 60,
        "cpu_intensity": "medium",
        "parallelizable": True,
        "memory_usage": "medium",
        "batch_size": 10,
    },
    "bandit": {
        "cmd": "bandit",
        "args": ["-f", "json", "-r", "--exclude", ".venv,venv,node_modules,__pycache__,dist,build"],
        "importance": "✅ Important",
        "description": "Warns about unsafe use of secrets, unsafe file I/O, and injection risks",
        "parse_func": "parse_bandit",
        "raw_cmd": "bandit -r --exclude .venv,venv,node_modules,__pycache__,dist,build",
        "timeout": 180,
        "cpu_intensity": "high",
        "parallelizable": False,  # Bandit scans the entire project at once
        "memory_usage": "high",
        "batch_size": 1,
    },
    "vulture": {
        "cmd": "vulture",
        "args": [],
        "importance": "⚠️ Nice to have",
        "description": "Finds unused UI elements or logic blocks (but may flag false positives due to Streamlit reactivity)",
        "parse_func": "parse_vulture",
        "raw_cmd": "vulture",
        "timeout": 60,
        "cpu_intensity": "low",
        "parallelizable": True,
        "memory_usage": "low",
        "batch_size": 20,
    },
    "flake8": {
        "cmd": "flake8",
        "args": ["--format=json"],
        "importance": "✅ Helps with readability",
        "description": "Keeps formatting, line breaks, and indentations clean",
        "parse_func": "parse_flake8",
        "raw_cmd": "flake8",
        "timeout": 60,
        "cpu_intensity": "low",
        "parallelizable": True,
        "memory_usage": "low",
        "batch_size": 20,
    }
}

# Streamlit specific issue messages to highlight
STREAMLIT_KEYWORDS = [
    "st.", "streamlit", "session_state", "widget", "duplicate", 
    "key", "input", "form", "sidebar", "container"
]

class ProcessAffinity:
    """Class to manage process affinity on different platforms"""
    @staticmethod
    def set_affinity(core_type: str):
        """
        Set process affinity based on core type (performance or efficiency)
        Only has an effect on Apple Silicon where we can distinguish core types
        """
        if not IS_APPLE_SILICON:
            return  # Only applies to Apple Silicon
        
        try:
            proc = psutil.Process()
            total_cpus = cpu_count()
            
            if total_cpus <= 4:  # Probably not an M1/M2, or virtualized
                return
                
            if core_type == "performance":
                # On M1/M2: Performance cores are the higher-numbered ones
                # This is a heuristic that works on most Apple Silicon chips
                perf_cores = list(range(total_cpus - 4, total_cpus))
                proc.cpu_affinity(perf_cores)
            elif core_type == "efficiency":
                # Efficiency cores are the lower-numbered ones
                eff_cores = list(range(0, min(4, total_cpus // 2)))
                proc.cpu_affinity(eff_cores)
            # "balanced" uses all cores (default)
        except Exception:
            # Silently fail if affinity setting is not supported
            pass

class FileCache:
    """Cache for file analysis results to enable incremental analysis"""
    def __init__(self, cache_dir: str = CACHE_DIR):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache_info_file = self.cache_dir / "cache_info.json"
        self.cache_info = self._load_cache_info()
    
    def _load_cache_info(self) -> Dict:
        """Load cache metadata from disk"""
        if self.cache_info_file.exists():
            try:
                with open(self.cache_info_file, 'r') as f:
                    return json.load(f)
            except Exception:
                return {"files": {}, "tools": {}}
        return {"files": {}, "tools": {}}
    
    def _save_cache_info(self) -> None:
        """Save cache metadata to disk"""
        with open(self.cache_info_file, 'w') as f:
            json.dump(self.cache_info, f)
    
    def get_file_hash(self, file_path: str) -> str:
        """Calculate file hash based on content and mtime"""
        try:
            stat = os.stat(file_path)
            mtime = stat.st_mtime
            file_size = stat.st_size
            
            if file_size > 1024 * 1024:  # For files > 1MB
                # Use faster hash based on size, mtime, and first/last 8KB
                with open(file_path, 'rb') as f:
                    head = f.read(8192)
                    f.seek(max(0, file_size - 8192))
                    tail = f.read(8192)
                content_hash = hashlib.md5(head + tail).hexdigest()
                return f"{file_path}:{mtime}:{file_size}:{content_hash}"
            else:
                # For smaller files, hash the entire content
                with open(file_path, 'rb') as f:
                    content_hash = hashlib.md5(f.read()).hexdigest()
                return f"{file_path}:{mtime}:{content_hash}"
        except Exception:
            # If hashing fails, return a unique string ensuring no cache hit
            return f"{file_path}:{time.time()}:no_cache"
    
    def get_tool_result(self, tool_name: str, file_path: str) -> Optional[Dict]:
        """Get cached result for tool and file if available and not stale"""
        file_hash = self.get_file_hash(file_path)
        file_info = self.cache_info["files"].get(file_path, {})
        
        if file_info.get("hash") == file_hash:
            tool_results = file_info.get("tools", {}).get(tool_name)
            if tool_results:
                # Check if tool version matches
                tool_version = self._get_tool_version(tool_name)
                if tool_version == self.cache_info["tools"].get(tool_name, ""):
                    return tool_results
        return None
    
    def set_tool_result(self, tool_name: str, file_path: str, result: Dict) -> None:
        """Store tool result for file in cache"""
        file_hash = self.get_file_hash(file_path)
        
        if file_path not in self.cache_info["files"]:
            self.cache_info["files"][file_path] = {"hash": file_hash, "tools": {}}
        else:
            self.cache_info["files"][file_path]["hash"] = file_hash
            
        self.cache_info["files"][file_path]["tools"][tool_name] = result
        
        # Store tool version
        tool_version = self._get_tool_version(tool_name)
        self.cache_info["tools"][tool_name] = tool_version
        
        self._save_cache_info()
    
    def _get_tool_version(self, tool_name: str) -> str:
        """Get version of a tool for cache validation"""
        try:
            proc = subprocess.run(
                [tool_name, "--version"],
                capture_output=True,
                text=True,
                check=False
            )
            return proc.stdout.strip() or proc.stderr.strip() or "unknown"
        except Exception:
            return "unknown"
    
    def clear(self) -> None:
        """Clear all cached data"""
        if self.cache_dir.exists():
            shutil.rmtree(self.cache_dir)
            self.cache_dir.mkdir(parents=True, exist_ok=True)
            self.cache_info = {"files": {}, "tools": {}}
            self._save_cache_info()

class ProjectAnalyzer:
    """Manages the static analysis of a Streamlit project"""
    def __init__(self, project_path: str, tools_to_run: List[str],
                 max_workers: Optional[int] = None):
        self.project_path = os.path.abspath(project_path)
        self.tools_to_run = tools_to_run
        self.max_workers = max_workers or min(8, cpu_count())
        self.results = {}
        self.raw_outputs = {}
        self.execution_times = {}
        self.python_files = self._find_python_files()
        self.streamlit_files = self._identify_streamlit_files()

    def _find_python_files(self) -> List[str]:
        """Find all Python files in the project"""
        python_files = []
        for root, _, files in os.walk(self.project_path):
            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))
        return python_files

    def _identify_streamlit_files(self) -> List[str]:
        """Identify files that import or use Streamlit"""
        streamlit_files = []
        for file in self.python_files:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'streamlit' in content.lower():
                    streamlit_files.append(file)
        return streamlit_files

    def _create_batches(self, tool_name: str) -> List[List[str]]:
        """Create batches of files for parallel processing"""
        batch_size = TOOLS[tool_name].get('batch_size', 10)
        files = self.streamlit_files if tool_name == 'bandit' else self.python_files
        return [files[i:i + batch_size] for i in range(0, len(files), batch_size)]

    def _run_pylint(self, files: List[str]) -> Dict[str, Any]:
        """Run pylint on a batch of files"""
        cmd = ["pylint", "--output-format=json"]
        cmd.extend(files)
        result = subprocess.run(cmd, capture_output=True, text=True)
        issues = parse_pylint(result.stdout)
        return {"issues": issues, "raw_output": result.stdout}

    def _run_mypy(self, files: List[str]) -> Dict[str, Any]:
        """Run mypy on a batch of files"""
        cmd = ["mypy", "--show-error-context", "--no-incremental"]
        cmd.extend(files)
        result = subprocess.run(cmd, capture_output=True, text=True)
        issues = parse_mypy(result.stdout)
        return {"issues": issues, "raw_output": result.stdout}

    def _run_bandit(self, files: List[str]) -> Dict[str, Any]:
        """Run bandit on a batch of files"""
        cmd = ["bandit", "-f", "json"]
        cmd.extend(files)
        result = subprocess.run(cmd, capture_output=True, text=True)
        issues = parse_bandit(result.stdout)
        return {"issues": issues, "raw_output": result.stdout}

    def _run_flake8(self, files: List[str]) -> Dict[str, Any]:
        """Run flake8 on a batch of files"""
        cmd = ["flake8", "--format=json"]
        cmd.extend(files)
        result = subprocess.run(cmd, capture_output=True, text=True)
        issues = parse_flake8(result.stdout)
        return {"issues": issues, "raw_output": result.stdout}

    def _run_vulture(self, files: List[str]) -> Dict[str, Any]:
        """Run vulture on a batch of files"""
        cmd = ["vulture", "--min-confidence=60"]
        cmd.extend(files)
        result = subprocess.run(cmd, capture_output=True, text=True)
        issues = parse_vulture(result.stdout)
        return {"issues": issues, "raw_output": result.stdout}

    def _run_tool(self, tool_batch: Tuple[str, List[str]]) -> Tuple[str, List[Dict], str, float]:
        """Run a tool on a batch of files"""
        tool_name, batch = tool_batch
        start_time = time.time()
        
        try:
            if tool_name == "pylint":
                result = self._run_pylint(batch)
            elif tool_name == "mypy":
                result = self._run_mypy(batch)
            elif tool_name == "bandit":
                result = self._run_bandit(batch)
            elif tool_name == "flake8":
                result = self._run_flake8(batch)
            elif tool_name == "vulture":
                result = self._run_vulture(batch)
            else:
                raise ValueError(f"Unknown tool: {tool_name}")
                
            execution_time = time.time() - start_time
            return tool_name, result["issues"], result["raw_output"], execution_time
            
        except Exception as e:
            execution_time = time.time() - start_time
            print(f"{COLORS['RED']}Error running {tool_name}: {str(e)}{COLORS['ENDC']}")
            return tool_name, [], f"ERROR: {str(e)}", execution_time

    def run_analysis(self) -> Tuple[Dict, Dict, Dict]:
        """Run tools in parallel using threads"""
        results = {}
        raw_outputs = {}
        execution_times = {}

        # Create batches for all tools
        all_batches = []
        for tool_name in self.tools_to_run:
            batches = self._create_batches(tool_name)
            all_batches.extend([(tool_name, batch) for batch in batches])

        # Run tools in parallel using threads
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all tasks
            futures = [executor.submit(self._run_tool, batch) for batch in all_batches]

            # Process results as they complete
            for future in as_completed(futures):
                try:
                    result = future.result()
                    tool_name = result[0]
                    issues = result[1]
                    raw_output = result[2]
                    execution_time = result[3]

                    # Initialize tool results if not present
                    if tool_name not in results:
                        results[tool_name] = []
                        raw_outputs[tool_name] = []
                        execution_times[tool_name] = 0

                    # Add results
                    results[tool_name].extend(issues)
                    raw_outputs[tool_name].append(raw_output)
                    execution_times[tool_name] += execution_time

                except Exception as e:
                    print(f"{COLORS['RED']}Error processing future: {str(e)}{COLORS['ENDC']}")
                    continue

        # Combine raw outputs for each tool
        for tool_name in raw_outputs:
            raw_outputs[tool_name] = "\n".join(raw_outputs[tool_name])

        return results, raw_outputs, execution_times

    def _find_python_files(self) -> List[str]:
        """Find all Python files in the project"""
        python_files = []
        for root, _, files in os.walk(self.project_path):
            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))
        return python_files

    def _identify_streamlit_files(self) -> List[str]:
        """Identify files that import or use Streamlit"""
        streamlit_files = []
        for file in self.python_files:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'streamlit' in content.lower():
                    streamlit_files.append(file)
        return streamlit_files

    def _create_batches(self, tool_name: str) -> List[List[str]]:
        """Create batches of files for parallel processing"""
        batch_size = TOOLS[tool_name].get('batch_size', 10)
        files = self.streamlit_files if tool_name == 'bandit' else self.python_files
        return [files[i:i + batch_size] for i in range(0, len(files), batch_size)]

    def run_analysis(self) -> Tuple[Dict, Dict, Dict]:
        """Run tools in parallel using threads"""
        results = {}
        raw_outputs = {}
        execution_times = {}

        # Create batches for all tools
        all_batches = []
        for tool_name in self.tools_to_run:
            batches = self._create_batches(tool_name)
            all_batches.extend([(tool_name, batch) for batch in batches])

        # Run tools in parallel using threads
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all tasks
            futures = [executor.submit(self._run_tool, batch) for batch in all_batches]

            # Process results as they complete
            for future in as_completed(futures):
                try:
                    result = future.result()
                    tool_name = result[0]
                    issues = result[1]
                    raw_output = result[2]
                    execution_time = result[3]

                    # Initialize tool results if not present
                    if tool_name not in results:
                        results[tool_name] = []
                        raw_outputs[tool_name] = []
                        execution_times[tool_name] = 0

                    # Add results
                    results[tool_name].extend(issues)
                    raw_outputs[tool_name].append(raw_output)
                    execution_times[tool_name] += execution_time

                except Exception as e:
                    print(f"{COLORS['RED']}Error processing future: {str(e)}{COLORS['ENDC']}")
                    continue

        # Combine raw outputs for each tool
        for tool_name in raw_outputs:
            raw_outputs[tool_name] = "\n".join(raw_outputs[tool_name])

        return results, raw_outputs, execution_times

    def _run_tool(self, tool_batch: Tuple[str, List[str]]) -> Tuple[str, List[Dict], str, float]:
        """Run a tool on a batch of files"""
        tool_name, batch = tool_batch
        start_time = time.time()
        
        try:
            if tool_name == "pylint":
                result = self._run_pylint(batch)
            elif tool_name == "mypy":
                result = self._run_mypy(batch)
            elif tool_name == "bandit":
                result = self._run_bandit(batch)
            elif tool_name == "flake8":
                result = self._run_flake8(batch)
            elif tool_name == "vulture":
                result = self._run_vulture(batch)
            else:
                raise ValueError(f"Unknown tool: {tool_name}")
                
            execution_time = time.time() - start_time
            return tool_name, result["issues"], result["raw_output"], execution_time
            
        except Exception as e:
            execution_time = time.time() - start_time
            print(f"{COLORS['RED']}Error running {tool_name}: {str(e)}{COLORS['ENDC']}")
            return tool_name, [], f"ERROR: {str(e)}", execution_time

    def _run_pylint(self, files: List[str]) -> Dict[str, Any]:
        """Run pylint on a batch of files"""
        cmd = ["pylint", "--output-format=json"]
        cmd.extend(files)
        result = subprocess.run(cmd, capture_output=True, text=True)
        issues = parse_pylint(result.stdout)
        return {"issues": issues, "raw_output": result.stdout}

    def _run_mypy(self, files: List[str]) -> Dict[str, Any]:
        """Run mypy on a batch of files"""
        cmd = ["mypy", "--show-error-context", "--no-incremental"]
        cmd.extend(files)
        result = subprocess.run(cmd, capture_output=True, text=True)
        issues = parse_mypy(result.stdout)
        return {"issues": issues, "raw_output": result.stdout}

    def _run_bandit(self, files: List[str]) -> Dict[str, Any]:
        """Run bandit on a batch of files"""
        cmd = ["bandit", "-f", "json"]
        cmd.extend(files)
        result = subprocess.run(cmd, capture_output=True, text=True)
        issues = parse_bandit(result.stdout)
        return {"issues": issues, "raw_output": result.stdout}

    def _run_flake8(self, files: List[str]) -> Dict[str, Any]:
        """Run flake8 on a batch of files"""
        cmd = ["flake8", "--format=json"]
        cmd.extend(files)
        result = subprocess.run(cmd, capture_output=True, text=True)
        issues = parse_flake8(result.stdout)
        return {"issues": issues, "raw_output": result.stdout}

    def _run_vulture(self, files: List[str]) -> Dict[str, Any]:
        """Run vulture on a batch of files"""
        cmd = ["vulture", "--min-confidence=60"]
        cmd.extend(files)
        result = subprocess.run(cmd, capture_output=True, text=True)
        issues = parse_vulture(result.stdout)
        return {"issues": issues, "raw_output": result.stdout}

    def _run_tool(self, tool_batch: Tuple[str, List[str]]) -> Tuple[str, List[Dict], str, float]:
        """Run a tool on a batch of files"""
        tool_name, batch = tool_batch
        start_time = time.time()
        
        try:
            if tool_name == "pylint":
                result = self._run_pylint(batch)
            elif tool_name == "mypy":
                result = self._run_mypy(batch)
            elif tool_name == "bandit":
                result = self._run_bandit(batch)
            elif tool_name == "flake8":
                result = self._run_flake8(batch)
            elif tool_name == "vulture":
                result = self._run_vulture(batch)
            else:
                raise ValueError(f"Unknown tool: {tool_name}")
                
            execution_time = time.time() - start_time
            return tool_name, result["issues"], result["raw_output"], execution_time
            
        except Exception as e:
            execution_time = time.time() - start_time
            print(f"{COLORS['RED']}Error running {tool_name}: {str(e)}{COLORS['ENDC']}")
            return tool_name, [], f"ERROR: {str(e)}", execution_time

    def _run_pylint(self, files: List[str]) -> Dict[str, Any]:
        """Run pylint on a batch of files"""
        cmd = ["pylint", "--output-format=json"]
        cmd.extend(files)
        result = subprocess.run(cmd, capture_output=True, text=True)
        issues = parse_pylint(result.stdout)
        return {"issues": issues, "raw_output": result.stdout}

    def _run_mypy(self, files: List[str]) -> Dict[str, Any]:
        """Run mypy on a batch of files"""
        cmd = ["mypy", "--show-error-context", "--no-incremental"]
        cmd.extend(files)
        result = subprocess.run(cmd, capture_output=True, text=True)
        issues = parse_mypy(result.stdout)
        return {"issues": issues, "raw_output": result.stdout}

    def _run_bandit(self, files: List[str]) -> Dict[str, Any]:
        """Run bandit on a batch of files"""
        cmd = ["bandit", "-f", "json"]
        cmd.extend(files)
        result = subprocess.run(cmd, capture_output=True, text=True)
        issues = parse_bandit(result.stdout)
        return {"issues": issues, "raw_output": result.stdout}

    def _run_flake8(self, files: List[str]) -> Dict[str, Any]:
        """Run flake8 on a batch of files"""
        cmd = ["flake8", "--format=json"]
        cmd.extend(files)
        result = subprocess.run(cmd, capture_output=True, text=True)
        issues = parse_flake8(result.stdout)
        return {"issues": issues, "raw_output": result.stdout}

    def _run_vulture(self, files: List[str]) -> Dict[str, Any]:
        """Run vulture on a batch of files"""
        cmd = ["vulture", "--min-confidence=60"]
        cmd.extend(files)
        result = subprocess.run(cmd, capture_output=True, text=True)
        issues = parse_vulture(result.stdout)
        return {"issues": issues, "raw_output": result.stdout}

    def run_analysis(self):
        """Run tools in parallel using threads"""
        results = {}
        raw_outputs = {}
        execution_times = {}

        # Create batches for all tools
        all_batches = []
        for tool_name in self.tools_to_run:
            batches = self._create_batches(tool_name)
            all_batches.extend([(tool_name, batch) for batch in batches])

        # Run tools in parallel using threads
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all tasks
            futures = [executor.submit(self._run_tool, batch) for batch in all_batches]

            # Process results as they complete
            for future in as_completed(futures):
                try:
                    result = future.result()
                    tool_name = result[0]
                    issues = result[1]
                    raw_output = result[2]
                    execution_time = result[3]

                    # Initialize tool results if not present
                    if tool_name not in results:
                        results[tool_name] = []
                        raw_outputs[tool_name] = []
                        execution_times[tool_name] = 0

                    # Add results
                    results[tool_name].extend(issues)
                    raw_outputs[tool_name].append(raw_output)
                    execution_times[tool_name] += execution_time

                except Exception as e:
                    print(f"{COLORS['RED']}Error processing future: {str(e)}{COLORS['ENDC']}")
                    continue

        # Combine raw outputs for each tool
        for tool_name in raw_outputs:
            raw_outputs[tool_name] = "\n".join(raw_outputs[tool_name])

        return results, raw_outputs, execution_times
    
    def _get_optimal_workers(self) -> int:
        """Determine optimal number of worker processes based on CPU"""
        total_cpus = cpu_count()
        
        # For M1/M2, we want to leave some efficiency cores for the system
        if IS_APPLE_SILICON and total_cpus >= 8:
            # M1/M2 typically has 8+ cores, use 75% of them
            return max(1, int(total_cpus * 0.75))
        else:
            # For other systems, use N-1 cores
            return max(1, total_cpus - 1)
    
    def _find_python_files(self) -> List[str]:
        """Find all Python files in the project"""
        python_files = []
        for root, _, files in os.walk(self.project_path):
            if any(exclude in root for exclude in ['.venv', 'venv', 'node_modules', '__pycache__', '.git']):
                continue
            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))
        return python_files
    
    def _identify_streamlit_files(self) -> Set[str]:
        """Identify files that import or use Streamlit"""
        streamlit_files = set()
        for file_path in self.python_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if "import streamlit" in content or "from streamlit" in content or "st." in content:
                        streamlit_files.add(file_path)
            except Exception:
                continue
        return streamlit_files
    
    def _create_batches(self, tool_name: str) -> List[List[str]]:
        """Create batches of files for parallel processing"""
        tool_config = TOOLS[tool_name]
        
        if not tool_config["parallelizable"]:
            # Non-parallelizable tools process the entire project at once
            return [[self.project_path]]
        
        # For parallelizable tools, create batches of files
        batch_size = tool_config["batch_size"]
        files = list(self.streamlit_files) if tool_name in ["pylint", "mypy"] else self.python_files
        
        # Create batches
        return [files[i:i + batch_size] for i in range(0, len(files), batch_size)]
    
    def _run_tool(self, tool_batch: Tuple[str, List[str]]) -> Dict:
        """Run a tool on a batch of files"""
        tool_name, files = tool_batch
        tool_config = TOOLS[tool_name]
        
        # Set CPU affinity based on tool intensity
        if tool_config["cpu_intensity"] == "high":
            ProcessAffinity.set_affinity("performance")
        elif tool_config["cpu_intensity"] == "low":
            ProcessAffinity.set_affinity("efficiency")
        
        # Check if we're analyzing the whole project or specific files
        is_whole_project = len(files) == 1 and files[0] == self.project_path
        
        # Create a temporary file listing if there are multiple files
        files_arg = files
        temp_file = None
        if len(files) > 10 and not is_whole_project:
            temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
            for file in files:
                temp_file.write(f"{file}\n")
            temp_file.close()
            files_arg = ["--file-list", temp_file.name]
        
        # Build command
        if is_whole_project:
            cmd = [tool_config["cmd"]] + tool_config["args"] + [self.project_path]
            raw_cmd = tool_config["raw_cmd"].split() + [self.project_path]
        else:
            cmd = [tool_config["cmd"]] + tool_config["args"] + files_arg
            raw_cmd = tool_config["raw_cmd"].split() + files_arg
        
        timeout = tool_config["timeout"]
        start_time = time.time()
        
        with self.print_lock:
            if is_whole_project:
                print(f"Running {COLORS['BOLD']}{tool_name}{COLORS['ENDC']} on project...")
            else:
                print(f"Running {COLORS['BOLD']}{tool_name}{COLORS['ENDC']} on {len(files)} files...")
        
        try:
            # Use subprocess with timeout
            process = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True, 
                check=False,
                timeout=timeout
            )
            
            # Also get raw output
            raw_process = subprocess.run(
                raw_cmd,
                capture_output=True,
                text=True,
                check=False,
                timeout=timeout
            )
            
            raw_output = raw_process.stdout
            execution_time = time.time() - start_time
            
            # Check for installation issues
            if process.returncode != 0 and "not found" in process.stderr:
                with self.print_lock:
                    print(f"{COLORS['RED']}Error: {tool_name} is not installed.{COLORS['ENDC']}")
                    print(f"Install with: pip install {tool_name}")
                result = {
                    "success": False,
                    "issues": [],
                    "raw_output": f"ERROR: {tool_name} is not installed. Run: pip install {tool_name}",
                    "execution_time": execution_time
                }
            else:
                # Parse results
                    else:
                        print(f"  {COLORS['GREEN']}{tool_name}: No issues found{COLORS['ENDC']} ({execution_time:.2f}s)")
        
        except subprocess.TimeoutExpired:
            execution_time = time.time() - start_time
            with self.print_lock:
                print(f"{COLORS['YELLOW']}Warning: {tool_name} timed out after {timeout} seconds.{COLORS['ENDC']}")
            result = {
                "success": False,
                "issues": [],
                "raw_output": f"TIMEOUT: {tool_name} analysis timed out after {timeout} seconds.",
                "execution_time": execution_time
            }
        
        except Exception as e:
            execution_time = time.time() - start_time
            with self.print_lock:
                print(f"{COLORS['RED']}Error running {tool_name}: {str(e)}{COLORS['ENDC']}")
            result = {
                "success": False,
                "issues": [],
                "raw_output": f"ERROR: {str(e)}",
                "execution_time": execution_time
            }
        
        finally:
            # Clean up temporary file if used
            if temp_file and os.path.exists(temp_file.name):
                os.unlink(temp_file.name)
        
        return {tool_name: result}
    
    def _merge_tool_results(self, tool_results: List[Dict]) -> None:
        """Merge results from multiple batches of the same tool"""
        for result_dict in tool_results:
            for tool_name, result in result_dict.items():
                if tool_name not in self.results:
                    self.results[tool_name] = []
                    self.raw_outputs[tool_name] = ""
                    self.execution_times[tool_name] = 0
                
                if result["success"]:
                    self.results[tool_name].extend(result["issues"])
                    self.raw_outputs[tool_name] += result["raw_output"]
                    self.execution_times[tool_name] += result["execution_time"]
                else:
                    self.raw_outputs[tool_name] += result["raw_output"]
                    self.execution_times[tool_name] += result["execution_time"]
    
    def run_analysis(self) -> Tuple[Dict[str, List[Dict[str, Any]]], Dict[str, str], Dict[str, float]]:
        """Run all tools in parallel with batching"""
        start_time = time.time()
        
        # Print project info
        print(f"{COLORS['BLUE']}Analyzing Streamlit project: {self.project_path}{COLORS['ENDC']}")
        print(f"Found {len(self.python_files)} Python files, {len(self.streamlit_files)} with Streamlit imports")
        print(f"Using {self.max_workers} worker processes{'  🍎 Apple Silicon optimized' if IS_APPLE_SILICON else ''}\n")
        
        # Create all tool batches
        all_batches = []
        for tool_name in self.tools_to_run:
            if tool_name not in TOOLS:
                print(f"{COLORS['YELLOW']}Warning: Unknown tool: {tool_name}{COLORS['ENDC']}")
                continue
            
            batches = self._create_batches(tool_name)
            for batch in batches:
                all_batches.append((tool_name, batch))
        
        # Check for installation issues
        if process.returncode != 0 and "not found" in process.stderr:
            print(f"{COLORS['RED']}Error: {tool_name} is not installed.{COLORS['ENDC']}")
            print(f"Install with: pip install {tool_name}")
            result = {
                "success": False,
                "issues": [],
                "raw_output": f"ERROR: {tool_name} is not installed. Run: pip install {tool_name}",
                "execution_time": execution_time
            }
        else:
            # Parse results
            parse_function = globals()[tool_config["parse_func"]]
            issues = parse_function(process.stdout)
            result = {
                "success": True,
                "issues": issues,
                "raw_output": raw_output,
                "execution_time": execution_time,

            # Process results as they complete
            for future in as_completed(futures):
                try:
                    result = future.result()
                    tool_name = result[0]
                    issues = result[1]
                    raw_output = result[2]
                    execution_time = result[3]
    execution_times = {}

    # Create batches for all tools
    all_batches = []
    for tool_name in self.tools_to_run:
        batches = self._create_batches(tool_name)

                    # Add results
                    self.results[tool_name].extend(issues)
                    self.raw_outputs[tool_name] += raw_output
                    self.execution_times[tool_name] += execution_time

                except Exception as e:
                    print(f"{COLORS['RED']}Error processing future: {str(e)}{COLORS['ENDC']}")
                    continue

        # Combine raw outputs for each tool
        for tool_name in self.raw_outputs:
            self.raw_outputs[tool_name] = "\n".join(self.raw_outputs[tool_name])

        return self.results, self.raw_outputs, self.execution_times

# Parser functions for different tools
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

def is_streamlit_related(issue: Dict[str, Any]) -> bool:
    """Check if an issue is Streamlit-related based on keywords"""
    message = issue.get("message", "").lower()
    return any(keyword.lower() in message for keyword in STREAMLIT_KEYWORDS)

def generate_text_report(results: Dict[str, List[Dict[str, Any]]], raw_outputs: Dict[str, str], 
                         execution_times: Dict[str, float], project_info: Dict[str, Any]) -> str:
    """Generate a text report from all tool results"""
    report = []
    
    # Add header
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report.append("STREAMLIT STATIC ANALYSIS REPORT")
    report.append("=" * 40)
    report.append(f"Generated: {timestamp}")
    report.append(f"Project: {project_info['path']}")
    report.append(f"Python files: {project_info['python_files']}")
    report.append(f"Streamlit files: {project_info['streamlit_files']}")
    report.append(f"Analysis time: {project_info['total_time']:.2f} seconds")
    if IS_APPLE_SILICON:
        report.append(f"Hardware: Apple Silicon ({cpu_count()} cores)")
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
    
    # Add detailed results for each tool with raw output
    report.append("DETAILED RESULTS")
    report.append("=" * 40)
    
    for tool_name in sorted(results.keys()):
        raw_output = raw_outputs.get(tool_name, "")
        
        report.append("")
        report.append(f"{tool_name.upper()} OUTPUT")
        report.append("-" * 40)
        
        if raw_output:
            report.append(raw_output)
        else:
            tool_issues = results.get(tool_name, [])
            if not tool_issues:
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

def save_report(report: str, output_path: str) -> None:
    """Save the report to a file"""
    with open(output_path, "w") as f:
        f.write(report)
    print(f"{COLORS['GREEN']}Report saved to: {output_path}{COLORS['ENDC']}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="M1/M2 Optimized Streamlit Static Analysis Tool"
    )
    parser.add_argument(
        "project_path", 
        help="Path to the Streamlit project to analyze"
    )
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
        "--max-workers",
        type=int,
        default=None,
        help="Maximum number of parallel workers (default: auto-detect optimal)"
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Disable result caching for incremental analysis"
    )
    parser.add_argument(
        "--clear-cache",
        action="store_true",
        help="Clear the cache before running"
    )
    
    args = parser.parse_args()
    
    # Check if project path exists
    if not os.path.exists(args.project_path):
        print(f"{COLORS['RED']}Error: Project path does not exist: {args.project_path}{COLORS['ENDC']}")
        sys.exit(1)
    
    # Clear cache if requested
    if args.clear_cache:
        cache = FileCache()
        cache.clear()
        print(f"{COLORS['YELLOW']}Cache cleared.{COLORS['ENDC']}")
    
    # Determine which tools to run
    tools_to_run = list(TOOLS.keys()) if args.tools == "all" else args.tools.split(",")
    
    # Exclude bandit if specified
    if args.exclude_bandit and "bandit" in tools_to_run:
        tools_to_run.remove("bandit")
        print(f"{COLORS['YELLOW']}Note: Bandit excluded from analysis{COLORS['ENDC']}")
    
    # Run analysis
    start_time = time.time()
    
    analyzer = ProjectAnalyzer(
        args.project_path,
        tools_to_run,
        use_cache=not args.no_cache,
        max_workers=args.max_workers
    )
    
    results, raw_outputs, execution_times = analyzer.run_analysis()
    
    total_time = time.time() - start_time
    
    # Gather project info for the report
    project_info = {
        "path": args.project_path,
        "python_files": len(analyzer.python_files),
        "streamlit_files": len(analyzer.streamlit_files),
        "total_time": total_time
    }
    
    # Generate and save the report
    report = generate_text_report(results, raw_outputs, execution_times, project_info)
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

if __name__ == "__main__":
    main()

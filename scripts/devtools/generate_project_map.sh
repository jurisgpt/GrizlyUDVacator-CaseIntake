#!/bin/bash
# GrizlyUDVacator - Enhanced Project Awareness Script
# Usage: ./project_awareness.sh [--skip-tests] [--skip-graphs] [--open]

set -eo pipefail

# Configuration
PROJECT_NAME="GrizlyUDVacator"
PROJECT_DIR="grizly_app"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
OUTPUT_DIR="logs/awareness/${TIMESTAMP}"
SKIP_TESTS=false
SKIP_GRAPHS=false
OPEN_RESULTS=false

# Process arguments
for arg in "$@"; do
  case $arg in
    --skip-tests) SKIP_TESTS=true ;;
    --skip-graphs) SKIP_GRAPHS=true ;;
    --open) OPEN_RESULTS=true ;;
    --help) 
      echo "Usage: $0 [OPTIONS]"
      echo "Options:"
      echo "  --skip-tests    Skip running tests and coverage"
      echo "  --skip-graphs   Skip generating dependency graphs"
      echo "  --open          Open results when complete"
      echo "  --help          Show this help message"
      exit 0
      ;;
  esac
done

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to check if a command exists
check_command() {
  if ! command -v "$1" &> /dev/null; then
    echo -e "${RED}Error: $1 is required but not installed.${NC}"
    echo "  Install with: $2"
    return 1
  fi
  return 0
}

# Function to check if a Python module exists
check_python_module() {
  if ! python -c "import $1" &> /dev/null; then
    echo -e "${RED}Error: Python module '$1' is required but not installed.${NC}"
    echo "  Install with: pip install $2"
    return 1
  fi
  return 0
}

# Check if project directory exists
if [ ! -d "$PROJECT_DIR" ]; then
  echo -e "${RED}Error: Project directory '$PROJECT_DIR' does not exist.${NC}"
  echo "Update the PROJECT_DIR variable in the script."
  exit 1
fi

# Check required commands/modules
REQUIREMENTS_MET=true

# Base requirements
check_command "cloc" "pip install cloc or apt-get install cloc" || REQUIREMENTS_MET=false
check_command "tree" "apt-get install tree" || REQUIREMENTS_MET=false
check_python_module "radon" "radon" || REQUIREMENTS_MET=false
check_python_module "pytest" "pytest pytest-cov" || REQUIREMENTS_MET=false

# Optional requirements based on flags
if [ "$SKIP_GRAPHS" = false ]; then
  check_python_module "pyan" "pyan3" || echo -e "${YELLOW}Warning: pyan3 not found, dependency graphs will be skipped.${NC}"
  check_command "dot" "apt-get install graphviz" || echo -e "${YELLOW}Warning: graphviz not found, dependency graphs will be skipped.${NC}"
fi

# Exit if critical requirements are not met
if [ "$REQUIREMENTS_MET" = false ]; then
  echo -e "${RED}Critical requirements are missing. Please install them and try again.${NC}"
  exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Function to run a task with proper formatting
run_task() {
  local task_name="$1"
  local command="$2"
  local output_file="$3"
  local allow_failure="${4:-false}"
  
  echo -e "${BLUE}[$PROJECT_NAME]${NC} ${YELLOW}Running:${NC} $task_name"
  
  # Create a temporary file for stderr
  local stderr_file="${output_file}.stderr"
  
  # Run the command, capturing stdout and stderr separately
  if eval "$command" > "$output_file" 2> "$stderr_file"; then
    echo -e "${BLUE}[$PROJECT_NAME]${NC} ${GREEN}✓ Complete:${NC} $task_name"
    # Append stderr to the output file if it's not empty
    if [ -s "$stderr_file" ]; then
      echo -e "\n--- STDERR Output ---" >> "$output_file"
      cat "$stderr_file" >> "$output_file"
    fi
    rm "$stderr_file"
    return 0
  else
    local exit_code=$?
    echo -e "${BLUE}[$PROJECT_NAME]${NC} ${RED}✗ Failed:${NC} $task_name (Exit code: $exit_code)"
    # Append stderr to the output file
    echo -e "\n--- STDERR Output ---" >> "$output_file"
    cat "$stderr_file" >> "$output_file"
    rm "$stderr_file"
    
    if [ "$allow_failure" = true ]; then
      return 0
    else
      return $exit_code
    fi
  fi
}

# Create summary file
SUMMARY_FILE="$OUTPUT_DIR/SUMMARY.md"
echo "# $PROJECT_NAME Awareness Report" > "$SUMMARY_FILE"
echo "Generated: $(date)" >> "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"

# System information
echo "## System Information" >> "$SUMMARY_FILE"
echo '```' >> "$SUMMARY_FILE"
echo "OS: $(uname -a)" >> "$SUMMARY_FILE"
echo "Python: $(python --version 2>&1)" >> "$SUMMARY_FILE"
echo "Pip: $(pip --version 2>&1)" >> "$SUMMARY_FILE"
echo '```' >> "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"

# Project information
echo "## Project Information" >> "$SUMMARY_FILE"

# Git information if available
if [ -d ".git" ]; then
  echo "### Git Status" >> "$SUMMARY_FILE"
  echo '```' >> "$SUMMARY_FILE"
  echo "Branch: $(git branch --show-current 2>/dev/null || echo 'N/A')" >> "$SUMMARY_FILE"
  echo "Last commit: $(git log -1 --pretty=format:'%h - %s (%cr) <%an>' 2>/dev/null || echo 'N/A')" >> "$SUMMARY_FILE"
  echo "Uncommitted changes: $(git status --porcelain 2>/dev/null | wc -l || echo 'N/A')" >> "$SUMMARY_FILE"
  echo '```' >> "$SUMMARY_FILE"
  echo "" >> "$SUMMARY_FILE"
fi

# 1. Code stats
echo "### Code Statistics" >> "$SUMMARY_FILE"
run_task "Code stats (cloc)" "cloc ." "$OUTPUT_DIR/CODE_STATS.txt"
# More robust extraction of stats with fallbacks
TOTAL_LINES=$(grep -E "SUM:|^ *SUM:" "$OUTPUT_DIR/CODE_STATS.txt" | awk '{print $NF}' || echo "N/A")
TOTAL_FILES=$(grep -E "SUM:|^ *SUM:" "$OUTPUT_DIR/CODE_STATS.txt" | awk '{print $2}' || echo "N/A")
echo "See [Code Stats](CODE_STATS.txt) for detailed language breakdown" >> "$SUMMARY_FILE"
echo "Total files: $TOTAL_FILES, Total lines: $TOTAL_LINES" >> "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"

# 2. File structure
echo "### Project Structure" >> "$SUMMARY_FILE"
run_task "File tree" "tree -L 3 -I 'logs|__pycache__|*.pyc|*.pyo|*.pyd|.git|.pytest_cache|htmlcov|*.egg-info'" "$OUTPUT_DIR/FILE_TREE.txt"
echo "See [File Tree](FILE_TREE.txt) for detailed project structure" >> "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"

# 3. Folder sizes
echo "### Folder Sizes" >> "$SUMMARY_FILE"
run_task "Folder sizes" "du -sh ./* | sort -hr" "$OUTPUT_DIR/FOLDER_SIZES.txt"
echo "See [Folder Sizes](FOLDER_SIZES.txt) for detailed storage usage" >> "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"

# 4. Python packages
echo "### Installed Packages" >> "$SUMMARY_FILE"
run_task "Installed packages" "pip freeze" "$OUTPUT_DIR/REQUIREMENTS.txt"
echo "See [Requirements](REQUIREMENTS.txt) for installed packages" >> "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"

# 5. Complexity analysis
echo "### Code Complexity" >> "$SUMMARY_FILE"
run_task "Code complexity (Radon)" "radon cc \"$PROJECT_DIR/\" -s -a" "$OUTPUT_DIR/COMPLEXITY.txt" true
run_task "Maintainability index" "radon mi \"$PROJECT_DIR/\" -s" "$OUTPUT_DIR/MAINTAINABILITY.txt" true

# Extract complexity metrics for summary with better error handling
HIGH_COMPLEXITY=$(grep -c -E "^[EF]" "$OUTPUT_DIR/COMPLEXITY.txt" 2>/dev/null || echo "0")
echo "High complexity functions: $HIGH_COMPLEXITY" >> "$SUMMARY_FILE"
echo "See [Complexity Analysis](COMPLEXITY.txt) for detailed metrics" >> "$SUMMARY_FILE"
echo "See [Maintainability Index](MAINTAINABILITY.txt) for code maintainability" >> "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"

# 6. Pylint - Check if available first
if check_command "pylint" "pip install pylint" >/dev/null; then
  echo "### Code Quality (Pylint)" >> "$SUMMARY_FILE"
  run_task "Pylint analysis" "pylint --output-format=text \"$PROJECT_DIR/\"" "$OUTPUT_DIR/PYLINT.txt" true
  PYLINT_SCORE=$(grep -E "Your code has been rated at" "$OUTPUT_DIR/PYLINT.txt" | sed -E 's/.*rated at ([0-9.-]+).*/\1/' || echo "N/A")
  echo "Pylint score: $PYLINT_SCORE/10" >> "$SUMMARY_FILE"
  echo "See [Pylint Report](PYLINT.txt) for detailed analysis" >> "$SUMMARY_FILE"
  echo "" >> "$SUMMARY_FILE"
fi

# 7. Dependency graph - with better file globbing that works on macOS
if [ "$SKIP_GRAPHS" = false ] && check_python_module "pyan" "pyan3" >/dev/null && check_command "dot" "apt-get install graphviz" >/dev/null; then
  echo "### Dependency Graph" >> "$SUMMARY_FILE"
  
  # Create a list of Python files more portably
  find "$PROJECT_DIR" -name "*.py" > "$OUTPUT_DIR/python_files.txt"
  
  if [ -s "$OUTPUT_DIR/python_files.txt" ]; then
    run_task "Dependency graph (pyan3)" "pyan3 \$(cat \"$OUTPUT_DIR/python_files.txt\") --dot" "$OUTPUT_DIR/dependency.dot" true && \
    run_task "Convert to SVG" "dot -Tsvg \"$OUTPUT_DIR/dependency.dot\" -o \"$OUTPUT_DIR/dependency.svg\"" "$OUTPUT_DIR/dot_conversion.log" true
    
    if [ -f "$OUTPUT_DIR/dependency.svg" ]; then
      echo "See [Dependency Graph](dependency.svg) for code relationships" >> "$SUMMARY_FILE"
    else
      echo "Dependency graph generation failed. See logs for details." >> "$SUMMARY_FILE"
    fi
  else
    echo "No Python files found for dependency graph generation." >> "$SUMMARY_FILE"
  fi
  echo "" >> "$SUMMARY_FILE"
fi

# 8. Test coverage
if [ "$SKIP_TESTS" = false ]; then
  echo "### Test Coverage" >> "$SUMMARY_FILE"
  run_task "Test coverage (pytest)" "pytest --cov=\"$PROJECT_DIR\" --cov-report=html --cov-report=term" "$OUTPUT_DIR/TEST_COVERAGE.txt" true
  
  # Only copy htmlcov if it exists
  if [ -d "htmlcov" ]; then
    cp -r htmlcov "$OUTPUT_DIR/htmlcov" 2>/dev/null
    echo "See [Test Coverage Report](htmlcov/index.html) for detailed coverage" >> "$SUMMARY_FILE"
  else
    echo "HTML coverage report was not generated" >> "$SUMMARY_FILE"
  fi
  
  # Extract coverage percentage with more robust handling
  COVERAGE_PCT=$(grep -E "TOTAL|TOTAL\s+" "$OUTPUT_DIR/TEST_COVERAGE.txt" | awk '{print $NF}' 2>/dev/null || echo "N/A")
  echo "Test coverage: $COVERAGE_PCT" >> "$SUMMARY_FILE"
  echo "" >> "$SUMMARY_FILE"
fi

# 9. Check for security issues with bandit - if available
if check_command "bandit" "pip install bandit" >/dev/null; then
  echo "### Security Analysis" >> "$SUMMARY_FILE"
  run_task "Security scan (bandit)" "bandit -r \"$PROJECT_DIR/\"" "$OUTPUT_DIR/SECURITY.txt" true
  SECURITY_ISSUES=$(grep -c "Issue:" "$OUTPUT_DIR/SECURITY.txt" 2>/dev/null || echo "0")
  echo "Security issues found: $SECURITY_ISSUES" >> "$SUMMARY_FILE"
  echo "See [Security Report](SECURITY.txt) for detailed analysis" >> "$SUMMARY_FILE"
  echo "" >> "$SUMMARY_FILE"
fi

# 10. Performance hints - if available
if check_command "scalene" "pip install scalene" >/dev/null; then
  echo "### Performance Analysis" >> "$SUMMARY_FILE"
  
  # Find test files
  FIRST_TEST_FILE=$(find . -name "test_*.py" -o -name "*_test.py" | head -1)
  
  if [ -n "$FIRST_TEST_FILE" ]; then
    run_task "Performance profile (scalene)" "scalene \"$FIRST_TEST_FILE\" --outfile=\"$OUTPUT_DIR/PERFORMANCE.json\"" "$OUTPUT_DIR/PERFORMANCE_LOG.txt" true
    
    if [ -f "$OUTPUT_DIR/PERFORMANCE.json" ]; then
      echo "See [Performance Report](PERFORMANCE.json) for potential bottlenecks" >> "$SUMMARY_FILE"
    else
      echo "Performance profiling failed. See logs for details." >> "$SUMMARY_FILE"
    fi
  else
    echo "No test files found for performance profiling." >> "$SUMMARY_FILE"
  fi
  echo "" >> "$SUMMARY_FILE"
fi

# Final message
echo ""
echo -e "${GREEN}✅ Awareness report completed for $PROJECT_NAME${NC}"
echo -e "${BLUE}📊 Results saved in:${NC} $OUTPUT_DIR"

# Open results if requested
if [ "$OPEN_RESULTS" = true ]; then
  echo -e "${BLUE}🔍 Opening results...${NC}"
  if command -v open &>/dev/null; then
    open "$OUTPUT_DIR"
  elif command -v xdg-open &>/dev/null; then
    xdg-open "$OUTPUT_DIR"
  else
    echo "Could not automatically open results. Please navigate to $OUTPUT_DIR"
  fi
fi

# Quick summary of findings
echo ""
echo -e "${YELLOW}📋 Quick Summary:${NC}"
echo "- Files: $TOTAL_FILES"
echo "- Lines of code: $TOTAL_LINES"
if [ "$SKIP_TESTS" = false ]; then
  echo "- Test coverage: $COVERAGE_PCT"
fi
echo "- High complexity functions: $HIGH_COMPLEXITY"
if check_command "pylint" "pip install pylint" >/dev/null 2>&1; then
  echo "- Code quality: $PYLINT_SCORE/10"
fi
if check_command "bandit" "pip install bandit" >/dev/null 2>&1; then
  echo "- Security issues: $SECURITY_ISSUES"
fi
echo ""
echo -e "${BLUE}📝 Full report:${NC} $OUTPUT_DIR/SUMMARY.md"


#!/bin/bash
# GrizlyUDVacator - Project Awareness Script

set -eo pipefail

# Configuration
PROJECT_NAME="GrizlyUDVacator-CaseIntake"
PROJECT_DIR="grizly_app"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
OUTPUT_DIR="logs/awareness/${TIMESTAMP}"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}[$PROJECT_NAME]${NC} Starting project analysis..."

# Verify we're in the correct directory by checking for expected subdirectories
if [ ! -d "$PROJECT_DIR" ]; then
  echo -e "${RED}Error: Project directory '$PROJECT_DIR' not found.${NC}"
  echo "This script must be run from the project root directory."
  echo "Current directory: $(pwd)"
  echo -e "${YELLOW}Please cd to: /Users/pradeepkumar/github/GrizlyUDVacator-CaseIntake/${NC}"
  exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"
echo -e "${BLUE}[$PROJECT_NAME]${NC} Created output directory: $OUTPUT_DIR"

# Function to check if a command exists
check_command() {
  if ! command -v "$1" &> /dev/null; then
    echo -e "${YELLOW}Warning: $1 is not installed. Skipping related analysis.${NC}"
    echo "  Install with: $2"
    return 1
  fi
  return 0
}

# Function to run a task with proper formatting
run_task() {
  local task_name="$1"
  local command="$2"
  local output_file="$3"
  
  echo -e "${BLUE}[$PROJECT_NAME]${NC} ${YELLOW}Running:${NC} $task_name"
  
  if eval "$command" > "$output_file" 2>&1; then
    echo -e "${BLUE}[$PROJECT_NAME]${NC} ${GREEN}✓ Complete:${NC} $task_name"
    return 0
  else
    echo -e "${BLUE}[$PROJECT_NAME]${NC} ${RED}✗ Failed:${NC} $task_name"
    echo "  Check $output_file for details"
    return 0  # Continue script execution even if a task fails
  fi
}

# Create summary file
SUMMARY_FILE="$OUTPUT_DIR/SUMMARY.md"
echo "# $PROJECT_NAME Project Analysis" > "$SUMMARY_FILE"
echo "Generated: $(date)" >> "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"

# 1. Basic project stats
echo "## Project Structure" >> "$SUMMARY_FILE"

# File Tree (basic)
if check_command "tree" "brew install tree or apt-get install tree"; then
  run_task "File tree" "tree -L 2" "$OUTPUT_DIR/FILE_TREE.txt"
  echo "See [File Tree](FILE_TREE.txt) for project structure" >> "$SUMMARY_FILE"
else
  run_task "Directory listing" "find . -type d -maxdepth 2 | sort" "$OUTPUT_DIR/DIRECTORIES.txt"
  echo "See [Directories](DIRECTORIES.txt) for project structure" >> "$SUMMARY_FILE"
fi

# Folder sizes
run_task "Folder sizes" "du -sh ./* | sort -hr" "$OUTPUT_DIR/FOLDER_SIZES.txt"
echo "See [Folder Sizes](FOLDER_SIZES.txt) for storage usage" >> "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"

# 2. Code stats
echo "## Code Statistics" >> "$SUMMARY_FILE"
if check_command "cloc" "pip install cloc or brew install cloc"; then
  run_task "Code stats" "cloc $PROJECT_DIR" "$OUTPUT_DIR/CODE_STATS.txt"
  echo "See [Code Stats](CODE_STATS.txt) for language breakdown" >> "$SUMMARY_FILE"
else
  run_task "File count by type" "find $PROJECT_DIR -type f | grep -v '__pycache__' | sort | grep -Eo '\\.[^.]+$' | sort | uniq -c | sort -nr" "$OUTPUT_DIR/FILE_TYPES.txt"
  echo "See [File Types](FILE_TYPES.txt) for file type counts" >> "$SUMMARY_FILE"
fi
echo "" >> "$SUMMARY_FILE"

# 3. Python packages
echo "## Dependencies" >> "$SUMMARY_FILE"
run_task "Installed packages" "pip freeze" "$OUTPUT_DIR/REQUIREMENTS.txt"
echo "See [Requirements](REQUIREMENTS.txt) for installed packages" >> "$SUMMARY_FILE"
echo "" >> "$SUMMARY_FILE"

# 4. Code complexity
echo "## Code Quality" >> "$SUMMARY_FILE"
if check_command "radon" "pip install radon"; then
  run_task "Code complexity" "radon cc $PROJECT_DIR -s -a" "$OUTPUT_DIR/COMPLEXITY.txt"
  run_task "Maintainability index" "radon mi $PROJECT_DIR -s" "$OUTPUT_DIR/MAINTAINABILITY.txt"
  echo "See [Complexity Analysis](COMPLEXITY.txt) for code complexity metrics" >> "$SUMMARY_FILE"
  echo "See [Maintainability Index](MAINTAINABILITY.txt) for code maintainability" >> "$SUMMARY_FILE"
fi

if check_command "pylint" "pip install pylint"; then
  run_task "Pylint analysis" "pylint --output-format=text $PROJECT_DIR" "$OUTPUT_DIR/PYLINT.txt"
  echo "See [Pylint Report](PYLINT.txt) for code quality analysis" >> "$SUMMARY_FILE"
fi
echo "" >> "$SUMMARY_FILE"

# 5. Test coverage
echo "## Test Coverage" >> "$SUMMARY_FILE"
if check_command "pytest" "pip install pytest pytest-cov"; then
  run_task "Test coverage" "pytest --cov=$PROJECT_DIR --cov-report=html" "$OUTPUT_DIR/TEST_COVERAGE.txt"
  
  # Only copy htmlcov if it exists
  if [ -d "htmlcov" ]; then
    cp -r htmlcov "$OUTPUT_DIR/htmlcov"
    echo "See [Test Coverage Report](htmlcov/index.html) for detailed coverage" >> "$SUMMARY_FILE"
  else
    echo "No HTML coverage report was generated" >> "$SUMMARY_FILE"
  fi
else
  echo "pytest not found. Test coverage analysis skipped." >> "$SUMMARY_FILE"
fi
echo "" >> "$SUMMARY_FILE"

# Final message
echo ""
echo -e "${GREEN}✅ Project analysis completed for $PROJECT_NAME${NC}"
echo -e "${BLUE}📊 Results saved in:${NC} $OUTPUT_DIR"
echo -e "${BLUE}📝 Summary:${NC} $OUTPUT_DIR/SUMMARY.md"

# Try to open results
if command -v open &>/dev/null; then
  open "$OUTPUT_DIR"
elif command -v xdg-open &>/dev/null; then
  xdg-open "$OUTPUT_DIR"
else
  echo "Could not automatically open results. Please navigate to $OUTPUT_DIR"
fi


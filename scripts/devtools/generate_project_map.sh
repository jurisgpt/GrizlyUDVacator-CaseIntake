#!/bin/bash

set -e

echo "📁 Running situational awareness for GrizlyUDVacator"

OUTPUT_DIR="logs/awareness/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$OUTPUT_DIR"

# 1. Code stats and tree
cloc . > "$OUTPUT_DIR/CODE_STATS.txt"
tree -L 2 > "$OUTPUT_DIR/FILE_TREE.txt"
du -sh * > "$OUTPUT_DIR/FOLDER_SIZES.txt"

# 2. Complexity
radon cc grizly_app/ -s -a > "$OUTPUT_DIR/COMPLEXITY.txt"
radon mi grizly_app/ -s >> "$OUTPUT_DIR/COMPLEXITY.txt"

# 3. Dependency graph
pyan3 grizly_app/**/*.py --dot > "$OUTPUT_DIR/dependency.dot"
dot -Tsvg "$OUTPUT_DIR/dependency.dot" -o "$OUTPUT_DIR/dependency.svg"

# 4. Test coverage
pytest --cov=grizly_app --cov-report=html
cp -r htmlcov "$OUTPUT_DIR/htmlcov"

echo "✅ Awareness map saved in: $OUTPUT_DIR"
open "$OUTPUT_DIR"



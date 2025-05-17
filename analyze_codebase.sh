#!/bin/zsh

APP_ROOT="grizly_app"
OUTPUT_DIR="trace_outputs"
TARGET_MODULE="grizly_app/app.py"
DOT_FILE="$OUTPUT_DIR/graph.dot"
SVG_FILE="$OUTPUT_DIR/graph.svg"
LOG_FILE="$OUTPUT_DIR/dependency.log"

# Ensure environment is set
export PYTHONPATH=$(pwd)

mkdir -p "$OUTPUT_DIR"
echo "[INFO] Cleaning old trace files..."
rm -f "$OUTPUT_DIR"/*.dot(N) "$OUTPUT_DIR"/*.svg(N) "$OUTPUT_DIR"/*.json(N) "$OUTPUT_DIR"/*.log(N)

if [[ ! -f "$TARGET_MODULE" ]]; then
  echo "[ERROR] $TARGET_MODULE not found. Fix path."
  exit 1
fi

echo "[INFO] Running pydeps on $TARGET_MODULE..."
pydeps "$TARGET_MODULE" \
  --max-bacon=2 \
  --show-deps \
  --noshow \
  --dot-output="$DOT_FILE" &> "$LOG_FILE"

if [[ ! -f "$DOT_FILE" ]]; then
  echo "[ERROR] pydeps failed. See $LOG_FILE"
  exit 1
fi

echo "[INFO] Converting .dot → .svg..."
dot -Tsvg "$DOT_FILE" -o "$SVG_FILE"
open "$SVG_FILE"


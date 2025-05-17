#!/bin/bash

# ------------------------------------------------------------------------------
# GRAPH GENERATOR FOR GrizlyUDVacator
# Dependency Graph via pydeps + dot
# ------------------------------------------------------------------------------

# Config
TARGET_MODULE="grizly_app/app.py"
OUTDIR="trace_outputs"
DOTFILE="$OUTDIR/grizly_app_graph.dot"
SVGFILE="$OUTDIR/grizly_app_graph.svg"
PDFFILE="$OUTDIR/grizly_app_graph.pdf"
LOGFILE="$OUTDIR/dependency.log"

# Create output directory if missing
mkdir -p "$OUTDIR"

echo "[INFO] Cleaning old trace files..."
rm -f "$OUTDIR"/*.dot "$OUTDIR"/*.svg "$OUTDIR"/*.pdf "$LOGFILE"

echo "[INFO] Running pydeps on $TARGET_MODULE..."
pydeps "$TARGET_MODULE" \
  --max-bacon=2 \
  --show-deps \
  --dot-output="$DOTFILE" \
  2> "$LOGFILE"

if [ ! -s "$DOTFILE" ]; then
    echo "[ERROR] pydeps failed or produced empty DOT file. See $LOGFILE"
    exit 1
fi

echo "[INFO] DOT file generated at: $DOTFILE"

# Convert DOT to SVG
echo "[INFO] Generating SVG..."
dot -Tsvg "$DOTFILE" -o "$SVGFILE"

# Convert DOT to PDF
echo "[INFO] Generating PDF..."
dot -Tpdf "$DOTFILE" -o "$PDFFILE"

# Open files
echo "[INFO] Opening SVG in browser..."
open -a "Google Chrome" "$SVGFILE"

echo "[INFO] Opening PDF in Preview..."
open -a "Preview" "$PDFFILE"

echo "[✅ DONE] Dependency graph generated."

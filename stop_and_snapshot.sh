#!/bin/bash

# ================================
# 🧊 stop_and_snapshot.sh
# Gracefully stop all dev processes (Streamlit),
# commit working state, tag the snapshot,
# and deactivate Python venv.
# ================================

set -e  # Exit immediately on error
set -u  # Treat unset variables as errors

echo "🔍 Checking for running Streamlit processes..."

# Check if Streamlit is running
STREAMLIT_PID=$(pgrep -f "streamlit run" || true)

if [[ -n "$STREAMLIT_PID" ]]; then
    echo "🛑 Stopping Streamlit process (PID: $STREAMLIT_PID)..."
    kill "$STREAMLIT_PID"
    sleep 1
else
    echo "✅ No active Streamlit process found."
fi

echo "📂 Checking Git status..."

# Check if working directory is clean or has changes
if [[ -n $(git status --porcelain) ]]; then
    echo "📦 Staging all changes..."
    git add .

    SNAPSHOT_TAG="snapshot-$(date +%Y%m%d_%H%M%S)"
    echo "💬 Committing snapshot with tag: $SNAPSHOT_TAG"
    git commit -m "📦 Snapshot before shutdown: $SNAPSHOT_TAG"
    git push

    echo "🏷️ Tagging this commit as: $SNAPSHOT_TAG"
    git tag -a "$SNAPSHOT_TAG" -m "Snapshot taken before shutdown"
    git push origin "$SNAPSHOT_TAG"
else
    echo "✅ Working tree is clean. No commit needed."
fi

# Deactivate virtualenv if active
if [[ -n "${VIRTUAL_ENV:-}" ]]; then
    echo "👟 Deactivating Python virtual environment..."
    deactivate
else
    echo "💤 No virtual environment active."
fi

echo "🎉 Done! Project safely saved and shut down."



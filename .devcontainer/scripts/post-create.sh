#!/usr/bin/env bash

# Sync all UV groups and activate the virtual environment
echo "Synchronizing UV environment..."
uv sync --all-groups --active
if [ $? -ne 0 ]; then
    echo "Failed to synchronize UV environment."
    exit 1
fi
echo "Activating virtual environment..."
source .venv/bin/activate

#!/bin/bash

# Exit on any error
set -e

# Get the root directory of the project (one level up from scripts/)
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "🔄 Activating virtual environment..."
source "$ROOT_DIR/.venv/bin/activate"

echo "🚀 Running test suite..."
python "$ROOT_DIR/src/runner.py"

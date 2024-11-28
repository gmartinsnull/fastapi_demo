#!/bin/bash
set -e  # Exit immediately if any command fails
echo "Running unit tests..."  # This should show up in Vercel logs
# Install required packages
python -m pip install -r requirements.txt
pytest tests/unit_tests/ -v -s

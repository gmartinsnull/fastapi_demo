#!/bin/bash
set -e  # Exit immediately if any command fails
pip install -r requirements.txt
pytest tests/unit_tests/ -v -s

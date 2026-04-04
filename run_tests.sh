#!/bin/bash

# Activate conda environment in Git Bash
source "C:/Users/palmera3/AppData/Local/miniconda3/Scripts/activate"
conda activate Quantium

# Run the test suite
pytest test_app.py -v

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo "Exit code: 0"
    exit 0
else
    echo "Exit code: 1"
    exit 1
fi
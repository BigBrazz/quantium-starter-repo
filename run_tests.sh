#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate

# Run tests
pytest
TEST_EXIT_CODE=$?

# Return pytest exit code 
echo $?
exit $TEST_EXIT_CODE
#!/bin/bash

# Run all functional tests
python3 tests/functional/test_intake_form.py

# Check exit status
if [ $? -eq 0 ]; then
    echo "\n✅ All tests completed successfully"
else
    echo "\n❌ Some tests failed"
fi

from grizly_app.utils.logger import UnifiedLogger
import json
import time
from datetime import datetime

# Initialize logger
logger = UnifiedLogger()

# Generate some test logs
print("\nGenerating test logs...")

# INFO level log
logger.log('INFO', 'This is a test info message', {
    'event': 'test_event',
    'data': {
        'message': 'Test info message content'
    }
})

time.sleep(0.5)  # Give time for file operations

# ERROR level log
try:
    raise ValueError("This is a test error")
except Exception as e:
    logger.log('ERROR', 'This is a test error message', {
        'event': 'test_error',
        'data': {
            'exception': str(e),
            'traceback': 'Test traceback'
        }
    })

time.sleep(0.5)  # Give time for file operations

# Check log files
print("\nLog files location:")
print("- app.log: Contains all INFO and ERROR messages")
print("- error.log: Contains only ERROR messages")
print("\nYou can find these files in the 'logs' directory in your project root.")

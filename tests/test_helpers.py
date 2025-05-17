import os
import tempfile
import json
import logging
from typing import Dict, Any
import logging.config
import shutil

def setup_test_logging():
    """Set up test logging configuration"""
    try:
        # Create temporary directory for logs
        temp_dir = tempfile.mkdtemp(prefix="test_logs_")
        log_file = os.path.join(temp_dir, 'grizly_app.log')
        error_file = os.path.join(temp_dir, 'grizly_app_error.log')
        
        # Create logger
        logger = logging.getLogger('grizly_app')
        logger.setLevel(logging.INFO)
        logger.propagate = False
        
        # Create handlers
        file_handler = logging.FileHandler(log_file)
        error_handler = logging.FileHandler(error_file)
        error_handler.setLevel(logging.ERROR)
        
        # Set formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        error_handler.setFormatter(formatter)
        
        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(error_handler)
        
        # Debug logging
        print(f"\nUsing temporary log directory: {temp_dir}")
        print(f"Log file: {log_file}")
        print(f"Error file: {error_file}")
        
        # Verify logger setup
        print(f"\nLogger configuration:")
        print(f"Effective level: {logging.getLevelName(logger.getEffectiveLevel())}")
        print(f"Logger level: {logging.getLevelName(logger.level)}")
        print(f"Handlers configured: {len(logger.handlers)}")
        
        # Return both logger and temp_dir for cleanup
        return logger, temp_dir
    except Exception as e:
        print(f"Error setting up logging: {e}")
        raise

def cleanup_test_logging(temp_dir):
    """Clean up test logging resources"""
    try:
        if temp_dir and os.path.exists(temp_dir):
            # Remove the entire temporary directory and its contents
            shutil.rmtree(temp_dir)
    except Exception as e:
        print(f"Error cleaning up logging: {e}")
        raise

def read_logs(temp_dir, error_only: bool = False) -> list:
    """Read logs from test files"""
    # Print detailed debug information about the directory
    print(f"\nReading logs for directory: {temp_dir}")
    print(f"Directory exists: {os.path.exists(temp_dir)}")
    
    # List all files in the directory
    print("\nDirectory contents:")
    if os.path.exists(temp_dir):
        for file in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, file)
            print(f"File: {file}")
            print(f"  Path: {file_path}")
            print(f"  Exists: {os.path.exists(file_path)}")
            print(f"  Is file: {os.path.isfile(file_path)}")
            if os.path.isfile(file_path):
                print(f"  Size: {os.path.getsize(file_path)} bytes")
                print(f"  Permissions: {oct(os.stat(file_path).st_mode)}")
    
    # Determine the log file to read
    log_file = os.path.join(temp_dir, 'grizly_app_error.log' if error_only else 'grizly_app.log')
    print(f"\nTarget log file: {log_file}")
    print(f"Log file exists: {os.path.exists(log_file)}")
    
    # Check if file exists and is readable
    if not os.path.exists(log_file):
        print(f"Log file does not exist: {log_file}")
        return []
    
    if not os.access(log_file, os.R_OK):
        print(f"Log file exists but is not readable: {log_file}")
        return []
    
    print(f"\nLog file permissions: {oct(os.stat(log_file).st_mode)}")
    print(f"Log file size: {os.path.getsize(log_file)} bytes")
    
    logs = []
    with open(log_file, 'r') as f:
        print(f"\nLog file contents:")
        content = f.read()
        print(f"Raw file content: {content}")
        
        # Reset file pointer to start
        f.seek(0)
        
        for line in f:
            print(f"\nProcessing line: {line.strip()}")
            if not line.strip():
                print("Skipping empty line")
                continue
                
            try:
                # Split on spaces, but preserve message content
                parts = line.split(' - ', 3)
                if len(parts) != 4:
                    print(f"Line has incorrect format: {parts}")
                    continue
                    
                timestamp = parts[0].strip()
                name = parts[1].strip()
                level = parts[2].strip()
                message = parts[3].strip()
                
                log_entry = {
                    'timestamp': timestamp,
                    'name': name,
                    'level': level,
                    'message': message
                }
                logs.append(log_entry)
                print(f"Parsed log entry: {log_entry}")
            except Exception as e:
                print(f"Error reading log line: {e}")
                print(f"Failed to parse line: {line.strip()}")
                continue
    
    print(f"\nFound {len(logs)} log entries")
    return logs
    

class TestLogger:
    """Helper class for testing logging functionality"""
    
    logs = []
    
    @classmethod
    def setup_class(cls):
        """Initialize the logs list"""
        cls.logs = []
    
    @classmethod
    def get_logs(cls):
        return cls.logs
        
    @classmethod
    def info(cls, msg, *args, **kwargs):
        cls.logs.append({
            'level': 'INFO',
            'message': msg % args,
            **kwargs
        })
        
    @classmethod
    def error(cls, msg, *args, **kwargs):
        cls.logs.append({
            'level': 'ERROR',
            'message': msg % args,
            **kwargs
        })
        
    @classmethod
    def warning(cls, msg, *args, **kwargs):
        cls.logs.append({
            'level': 'WARNING',
            'message': msg % args,
            **kwargs
        })
        
    @classmethod
    def debug(cls, msg, *args, **kwargs):
        cls.logs.append({
            'level': 'DEBUG',
            'message': msg % args,
            **kwargs
        })
        
    @classmethod
    def assert_logged(cls, level: str, message: str, **kwargs):
        """Assert that a log entry with the given level and message exists"""
        for log in cls.logs:
            if (log['level'] == level and 
                log['message'] == message and 
                all(log.get(k) == v for k, v in kwargs.items())):
                return True
        raise AssertionError(f"No log entry found with level={level} and message={message}")


def assert_log_contains(logs: list, expected: Dict[str, Any]):
    """Assert that a log entry contains expected values"""
    for log in logs:
        if all(log.get(k) == v for k, v in expected.items()):
            return True
    return False

import unittest

class TestLoggingHelpers(unittest.TestCase):
    def setUp(self):
        self.logger = TestLogger()
        self.logger.setup_class()

    def test_log_levels(self):
        """Test all log levels"""
        self.logger.info("Test info message")
        self.logger.error("Test error message")
        self.logger.warning("Test warning message")
        self.logger.debug("Test debug message")
        
        logs = self.logger.get_logs()
        self.assertEqual(len(logs), 4)
        
        self.assertTrue(self.assert_log_contains(logs, {'level': 'INFO', 'message': 'Test info message'}))
        self.assertTrue(self.assert_log_contains(logs, {'level': 'ERROR', 'message': 'Test error message'}))
        self.assertTrue(self.assert_log_contains(logs, {'level': 'WARNING', 'message': 'Test warning message'}))
        self.assertTrue(self.assert_log_contains(logs, {'level': 'DEBUG', 'message': 'Test debug message'}))

    def test_log_with_extra_data(self):
        """Test logging with extra data"""
        self.logger.info("Test message with extra", extra={'key': 'value'})
        
        logs = self.logger.get_logs()
        self.assertEqual(len(logs), 1)
        self.assert_log_contains(logs, {'level': 'INFO', 'message': 'Test message with extra', 'key': 'value'})

    def test_assert_logged(self):
        """Test assert_logged method"""
        self.logger.info("Test message")
        
        # Should pass
        self.logger.assert_logged('INFO', 'Test message')
        
        # Should raise AssertionError
        with self.assertRaises(AssertionError):
            self.logger.assert_logged('ERROR', 'Test message')

if __name__ == '__main__':
    unittest.main()

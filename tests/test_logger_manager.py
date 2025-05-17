import unittest
import os
import json
import logging
import tempfile
import time
from grizly_app.utils.logger_manager import LoggerManager
from tests.test_helpers import cleanup_test_logging
from grizly_app.utils.debug_utils import trace_method, debug_logger_setup

# Set up debug logger
debug_logger = debug_logger_setup()

class TestLoggerManager(unittest.TestCase):
    @trace_method
    def setUp(self):
        """Set up test environment"""
        debug_logger.debug("Setting up test environment")
        self.temp_dir = tempfile.mkdtemp(prefix="test_logs_")
        debug_logger.debug(f"Created test directory: {self.temp_dir}")
        
        # Verify directory permissions
        test_file = os.path.join(self.temp_dir, '.test_write')
        try:
            with open(test_file, 'w') as f:
                f.write('test')
            os.remove(test_file)
            debug_logger.debug(f"Verified write permissions for: {self.temp_dir}")
        except PermissionError:
            debug_logger.error(f"No write permissions for: {self.temp_dir}")
            raise
        
        # Initialize LoggerManager with tracing
        debug_logger.debug("Initializing LoggerManager")
        self.manager = LoggerManager(self.temp_dir)
        self.logger = self.manager.get_logger()
        self.log_file = os.path.join(self.temp_dir, LoggerManager.LOG_FILENAME)
        self.error_file = os.path.join(self.temp_dir, LoggerManager.ERROR_FILENAME)
        
        # Verify file permissions
        for file_path in [self.log_file, self.error_file]:
            debug_logger.debug(f"\nVerifying permissions for: {file_path}")
            # Check if file exists
            self.assertTrue(os.path.exists(file_path), f"File {file_path} does not exist")
            
            # Check permissions
            stats = os.stat(file_path)
            mode = oct(stats.st_mode)[-3:]
            debug_logger.debug(f"File permissions: {mode}")
            
            # Verify write permission
            self.assertTrue(os.access(file_path, os.W_OK), 
                           f"File {file_path} is not writable")
            
            # Perform direct write test
            test_content = f"Test write to {os.path.basename(file_path)}\n"
            try:
                with open(file_path, 'w') as f:
                    f.write(test_content)
                with open(file_path, 'r') as f:
                    content = f.read()
                    self.assertIn(test_content, content, 
                                 f"Direct write test failed for {file_path}")
            except Exception as e:
                debug_logger.error(f"Error testing file write for {file_path}: {e}")
                self.fail(f"Error testing file write for {file_path}: {e}")
        
        # Verify directory permissions
        dir_stats = os.stat(self.temp_dir)
        dir_mode = oct(dir_stats.st_mode)[-3:]
        debug_logger.debug(f"Directory permissions: {dir_mode}")
        self.assertTrue(os.access(self.temp_dir, os.W_OK), 
                       f"Directory {self.temp_dir} is not writable")
        
        # Debug print handler configuration
        debug_logger.debug("\n=== Handler Configuration ===")
        for handler in self.logger.handlers:
            debug_logger.debug(f"Handler type: {type(handler).__name__}")
            debug_logger.debug(f"Handler level: {logging.getLevelName(handler.level)}")
            debug_logger.debug(f"Handler formatter: {handler.formatter._fmt if handler.formatter else None}")
            if isinstance(handler, logging.FileHandler):
                debug_logger.debug(f"Handler path: {handler.baseFilename}")
            elif isinstance(handler, logging.StreamHandler):
                debug_logger.debug(f"Handler stream: {handler.stream}")
        
        self.addCleanup(cleanup_test_logging, self.temp_dir)

class TestLoggerManager(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.temp_dir = tempfile.mkdtemp(prefix="test_logs_")
        print(f"\nCreated test directory: {self.temp_dir}")
    
        # Verify directory permissions
        test_file = os.path.join(self.temp_dir, '.test_write')
        try:
            with open(test_file, 'w') as f:
                f.write('test')
            os.remove(test_file)
            print(f"Verified write permissions for: {self.temp_dir}")
        except PermissionError:
            print(f"No write permissions for: {self.temp_dir}")
            raise
    
        print("\nPre-existing handlers:")
        for handler in logging.getLogger("grizly_app").handlers:
            print(f"  {type(handler).__name__}")
    
        self.manager = LoggerManager(self.temp_dir)
        self.logger = self.manager.get_logger()
        self.log_file = os.path.join(self.temp_dir, LoggerManager.LOG_FILENAME)
        self.error_file = os.path.join(self.temp_dir, LoggerManager.ERROR_FILENAME)
        
        # Verify file permissions
        for file_path in [self.log_file, self.error_file]:
            # Check if file exists
            self.assertTrue(os.path.exists(file_path), f"File {file_path} does not exist")
            
            # Check permissions
            stats = os.stat(file_path)
            mode = oct(stats.st_mode)[-3:]
            print(f"\nFile {os.path.basename(file_path)} permissions: {mode}")
            
            # Verify write permission
            self.assertTrue(os.access(file_path, os.W_OK), 
                           f"File {file_path} is not writable")
            
            # Perform direct write test
            test_content = f"Test write to {os.path.basename(file_path)}\n"
            try:
                with open(file_path, 'w') as f:
                    f.write(test_content)
                with open(file_path, 'r') as f:
                    content = f.read()
                    self.assertIn(test_content, content, 
                                 f"Direct write test failed for {file_path}")
            except Exception as e:
                self.fail(f"Error testing file write for {file_path}: {e}")
        
        # Verify directory permissions
        dir_stats = os.stat(self.temp_dir)
        dir_mode = oct(dir_stats.st_mode)[-3:]
        print(f"\nDirectory permissions: {dir_mode}")
        self.assertTrue(os.access(self.temp_dir, os.W_OK), 
                       f"Directory {self.temp_dir} is not writable")
        
        # Debug print to verify paths
        print(f"\nLog file path: {self.log_file}")
        print(f"Error file path: {self.error_file}")
        
        # Verify handler configuration
        file_handler = None
        error_handler = None
        console_handler = None
        
        # Verify exactly 3 handlers: 2 FileHandlers and 1 StreamHandler
        file_handlers = [h for h in self.logger.handlers if isinstance(h, logging.FileHandler)]
        stream_handlers = [h for h in self.logger.handlers if isinstance(h, logging.StreamHandler)]
        
        self.assertEqual(len(file_handlers), 2, "Expected exactly 2 FileHandlers")
        self.assertEqual(len(stream_handlers), 1, "Expected exactly 1 StreamHandler")
        
        # Verify each handler
        for handler in self.logger.handlers:
            print(f"\nHandler type: {type(handler).__name__}")
            print(f"Handler level: {logging.getLevelName(handler.level)}")
            print(f"Handler formatter: {handler.formatter._fmt if handler.formatter else None}")
            
            if isinstance(handler, logging.FileHandler):
                if handler.level == logging.INFO and handler.baseFilename == self.log_file:
                    file_handler = handler
                    self.assertEqual(handler.formatter._fmt, '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                elif handler.level == logging.ERROR and handler.baseFilename == self.error_file:
                    error_handler = handler
                    self.assertEqual(handler.formatter._fmt, '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            elif isinstance(handler, logging.StreamHandler):
                console_handler = handler
                self.assertEqual(handler.formatter._fmt, '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # Verify main file handler
        self.assertIsNotNone(file_handler)
        self.assertEqual(file_handler.level, logging.INFO)
        self.assertEqual(file_handler.baseFilename, self.log_file)
        
        # Verify error file handler
        self.assertIsNotNone(error_handler)
        self.assertEqual(error_handler.level, logging.ERROR)
        self.assertEqual(error_handler.baseFilename, self.error_file)
        
        # Verify console handler
        self.assertIsNotNone(console_handler)
        self.assertEqual(console_handler.level, logging.ERROR)
        
        # Debug print to verify paths
        print(f"\nLog file path: {self.log_file}")
        print(f"Error file path: {self.error_file}")
        print(f"Handlers: {self.logger.handlers}")
        self.addCleanup(cleanup_test_logging, self.temp_dir)
    
    def tearDown(self):
        """Cleanup test resources"""
        # Close all handlers
        logger = logging.getLogger("grizly_app")
        handlers = logger.handlers[:]
        for handler in handlers:
            try:
                handler.close()
                logger.removeHandler(handler)
            except Exception as e:
                print(f"Error closing handler: {e}")
    
    def test_basic_configuration(self):
        """Test basic logger configuration"""
        self.assertIsNotNone(self.logger)
        self.assertEqual(self.logger.name, 'grizly_app')
        self.assertEqual(self.logger.level, logging.INFO)
        self.assertFalse(self.logger.propagate)
        
    @trace_method
    def test_handler_configuration(self):
        """Test logger handlers are properly configured"""
        debug_logger.debug("Testing handler configuration")
        handlers = self.logger.handlers
        debug_logger.debug(f"Found {len(handlers)} handlers")
        self.assertGreater(len(handlers), 0)
        
        # Verify handler types
        for handler in handlers:
            debug_logger.debug(f"\nVerifying handler: {type(handler).__name__}")
            self.assertIsInstance(handler, logging.Handler)
            
            if isinstance(handler, logging.FileHandler):
                debug_logger.debug(f"Verifying FileHandler: {handler.baseFilename}")
                self.assertTrue(os.path.exists(handler.baseFilename))
                self.assertTrue(os.path.isfile(handler.baseFilename))
                
                # Verify file permissions
                perms = os.stat(handler.baseFilename).st_mode
                debug_logger.debug(f"File permissions: {oct(perms)[-3:]}")
                self.assertTrue(os.access(handler.baseFilename, os.W_OK))
                
                # Verify formatter
                self.assertIsNotNone(handler.formatter)
                debug_logger.debug(f"Formatter pattern: {handler.formatter._fmt}")
                
                # Verify handler path based on level
                if handler.level == logging.INFO:
                    expected_path = self.log_file
                    debug_logger.debug("Verifying INFO level handler path")
                elif handler.level == logging.ERROR:
                    expected_path = self.error_file
                    debug_logger.debug("Verifying ERROR level handler path")
                
                self.assertEqual(handler.baseFilename, expected_path,
                             f"Handler path mismatch for level {logging.getLevelName(handler.level)}")
            elif isinstance(handler, logging.StreamHandler):
                debug_logger.debug("Verifying StreamHandler")
                self.assertEqual(handler.level, logging.ERROR)
                self.assertIsNotNone(handler.formatter)
                debug_logger.debug(f"Formatter pattern: {handler.formatter._fmt}")

    @trace_method
    def test_utf8_character_handling(self):
        """Test UTF-8 character handling in logs"""
        debug_logger.debug("Testing UTF-8 character handling")
        
        # Test string with various UTF-8 characters
        test_string = "Test with special characters: ñáéíóúÑÁÉÍÓÚ€¥£¢¡¿©®™✓"
        
        # Log at different levels
        self.logger.info(test_string)
        try:
            raise ValueError(f"Error with special characters: {test_string}")
        except Exception as e:
            self.logger.error(str(e))
        
        # Verify files exist and can be read
        for file_path in [self.log_file, self.error_file]:
            self.assertTrue(os.path.exists(file_path))
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                self.assertIn(test_string, content, 
                             f"UTF-8 characters not found in {file_path}")

    def test_stream_handler(self):
        """Test stream handler configuration"""
        debug_logger.debug("Testing stream handler")
        stream_handler = next((h for h in self.logger.handlers if isinstance(h, logging.StreamHandler)), None)
        self.assertIsNotNone(stream_handler)
        self.assertEqual(stream_handler.level, logging.ERROR)
        self.assertIsNotNone(stream_handler.formatter)
        debug_logger.debug(f"Stream handler formatter pattern: {stream_handler.formatter._fmt}")
    
    def test_log_message_formatting(self):
        """Test log message formatting"""
        test_message = "Test message"
        print(f"\nExpected log path: {self.log_file}")  # Debug
        print(f"Expected error path: {self.error_file}")  # Debug
        
        # Try direct file write first to verify permissions
        try:
            with open(self.log_file, 'w') as f:
                f.write("Test direct write\n")
            print(f"\nSuccessfully wrote directly to file")
        except Exception as e:
            print(f"\nError writing directly to file: {e}")
            raise
        
        # Verify logger handlers
        print(f"\nLogger has {len(self.logger.handlers)} handlers")
        for handler in self.logger.handlers:
            print(f"Handler type: {type(handler).__name__}")
            print(f"Handler name: {handler.name if hasattr(handler, 'name') else 'N/A'}")
            print(f"Handler level: {handler.level}")
            print(f"Handler filename: {handler.baseFilename if hasattr(handler, 'baseFilename') else 'N/A'}")
        
        self.logger.info(f"Event: test_event, Data: {{'message': '{test_message}'}}")
        
        # Force flush all handlers immediately
        for handler in self.logger.handlers:
            if hasattr(handler, 'flush'):
                handler.flush()
        
        # Verify log file exists and has content
        self.assertTrue(os.path.exists(self.log_file))
        self.assertTrue(os.path.isfile(self.log_file))
        
        # Debug print to verify file size
        print(f"\nLog file size: {os.path.getsize(self.log_file)} bytes")
        
        # Read logs from file
        with open(self.log_file, 'r') as f:
            log_content = f.read()
        
        # Debug print log content
        print(f"\nLog content: {log_content}")
        print(f"\nFile exists: {os.path.exists(self.log_file)}")  # Debug
        print(f"File is file: {os.path.isfile(self.log_file)}")  # Debug
        print(f"File size: {os.path.getsize(self.log_file) if os.path.exists(self.log_file) else 'File does not exist'}")  # Debug
        
        self.assertIn(test_message, log_content)
        self.assertIn('INFO', log_content)
    
    def test_error_handling(self):
        """Test error logging"""
        test_error = "Test error message"
        try:
            raise ValueError(test_error)
        except ValueError as e:
            self.logger.error(f"Error occurred: {str(e)}")
        
        # Wait for file operations to complete
        time.sleep(0.1)
        
        # Verify error is logged
        self.assertTrue(os.path.exists(self.error_file))
        self.assertTrue(os.path.isfile(self.error_file))
        
        with open(self.error_file, 'r') as f:
            error_content = f.read()
        
        self.assertIn(test_error, error_content)
        self.assertIn('ERROR', error_content)
    
    def test_child_logger(self):
        """Test getting child logger"""
        child_logger = self.manager.get_logger("test_child")
        self.assertIsNotNone(child_logger)
        self.assertEqual(child_logger.name, "grizly_app.test_child")
        self.assertEqual(child_logger.level, logging.INFO)

import unittest
from grizly_app.utils.error_handler import ErrorHandler
from tests.test_helpers import TestLogger

class TestErrorHandler(unittest.TestCase):
    def setUp(self):
        TestLogger.setup_class()
        self.logger = self.test_logger.setup_test_logging()
        self.handler = ErrorHandler(self.logger)
        
    def tearDown(self):
        self.test_logger.cleanup()
        
    def test_log_error(self):
        """Test error logging"""
        test_error = "Test error message"
        try:
            raise Exception(test_error)
        except Exception as e:
            self.handler.log_error("test", e)
        
        error_logs = self.test_logger.read_logs(error_only=True)
        self.assertGreater(len(error_logs), 0)
        self.test_logger.assert_log_contains(error_logs, {
            'error_type': 'test',
            'message': test_error
        })
        
    def test_error_decorator(self):
        """Test error decorator"""
        @self.handler.error_decorator()
        def test_function():
            raise Exception("Function error")
            
        try:
            test_function()
            self.fail("Exception should have been raised")
        except Exception as e:
            error_logs = self.test_logger.read_logs(error_only=True)
            self.assertGreater(len(error_logs), 0)
            self.test_logger.assert_log_contains(error_logs, {
                'error_type': 'test_function',
                'message': 'Function error'
            })
        
    def test_error_decorator_suppress(self):
        """Test error decorator with suppression"""
        @self.handler.error_decorator(suppress=True)
        def test_function():
            raise Exception("Function error")
            
        try:
            result = test_function()
            self.assertIsNone(result)
            
            error_logs = self.test_logger.read_logs(error_only=True)
            self.assertGreater(len(error_logs), 0)
            self.test_logger.assert_log_contains(error_logs, {
                'error_type': 'test_function',
                'message': 'Function error'
            })
        except Exception:
            self.fail("Exception should have been suppressed")
        
    def test_error_context(self):
        """Test error context"""
        test_context = {'key': 'value'}
        test_error = "Test error with context"
        try:
            raise Exception(test_error)
        except Exception as e:
            self.handler.log_error("test", e, context=test_context)
        
        error_logs = self.test_logger.read_logs(error_only=True)
        self.assertGreater(len(error_logs), 0)
        self.test_logger.assert_log_contains(error_logs, {
            'error_type': 'test',
            'message': test_error,
            'key': 'value'
        })

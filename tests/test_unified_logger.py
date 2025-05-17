import unittest
from grizly_app.utils.logger import UnifiedLogger
from tests.test_helpers import TestLogger

class TestUnifiedLogger(unittest.TestCase):
    def setUp(self):
        TestLogger.setup_class()
        self.logger = self.test_logger.setup_test_logging()
        self.unified_logger = UnifiedLogger()
        
    def tearDown(self):
        self.test_logger.cleanup()
        
    def test_log_info(self):
        """Test info level logging"""
        test_message = "Test info message"
        self.unified_logger.log("INFO", test_message)
        
        logs = self.test_logger.read_logs()
        self.assertGreater(len(logs), 0)
        self.test_logger.assert_log_contains(logs, {
            'level': 'INFO',
            'message': test_message
        })
        
    def test_log_error(self):
        """Test error level logging"""
        test_message = "Test error message"
        self.unified_logger.log("ERROR", test_message)
        
        error_logs = self.test_logger.read_logs(error_only=True)
        self.assertGreater(len(error_logs), 0)
        self.test_logger.assert_log_contains(error_logs, {
            'level': 'ERROR',
            'message': test_message
        })
        
    def test_log_with_metadata(self):
        """Test logging with metadata"""
        test_message = "Test message with metadata"
        metadata = {'key': 'value', 'number': 42}
        self.unified_logger.log("INFO", test_message, metadata)
        
        logs = self.test_logger.read_logs()
        self.assertGreater(len(logs), 0)
        self.test_logger.assert_log_contains(logs, {
            'level': 'INFO',
            'message': test_message,
            'key': 'value',
            'number': 42
        })
        
    def test_session_logging(self):
        """Test session logging"""
        try:
            import streamlit as st
            st.session_state.logs = []
            
            test_message = "Test session message"
            self.unified_logger.log("INFO", test_message)
            
            self.assertIn('logs', st.session_state)
            self.assertGreater(len(st.session_state.logs), 0)
            
            last_log = st.session_state.logs[-1]
            self.assertIn('timestamp', last_log)
            self.assertIn('level', last_log)
            self.assertIn('message', last_log)
            
        except ImportError:
            # Skip if Streamlit not available
            pass

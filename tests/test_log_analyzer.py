import unittest
from grizly_app.utils.log_analyzer import LogAnalyzer
from tests.test_helpers import TestLogger

class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        TestLogger.setup_class()
        TestLogger.assert_logged("INFO", "Test log entry")
        self.analyzer = LogAnalyzer()
        
    def tearDown(self):
        TestLogger.cleanup()
        
    def test_get_logs(self):
        """Test getting logs"""
        test_message = "Test message"
        TestLogger.info(test_message)
        
        logs = self.analyzer.get_logs(hours=1)
        self.assertGreater(len(logs), 0)
        self.assertIn('timestamp', logs[0])
        self.assertIn('level', logs[0])
        self.assertIn('message', logs[0])
        
    def test_get_error_logs(self):
        """Test getting error logs"""
        test_error = "Test error message"
        try:
            raise Exception(test_error)
        except Exception as e:
            TestLogger.error(str(e))
        
        error_logs = self.analyzer.get_logs(hours=1, error_only=True)
        self.assertGreater(len(error_logs), 0)
        self.assertIn('timestamp', error_logs[0])
        self.assertIn('level', error_logs[0])
        self.assertIn('message', error_logs[0])
        
    def test_get_statistics(self):
        """Test getting log statistics"""
        # Generate some test logs
        TestLogger.info("Test log entry")
        try:
            raise Exception("Test error")
        except Exception as e:
            TestLogger.error(str(e))
        
        stats = self.analyzer.get_statistics(hours=1)
        self.assertIn('total_logs', stats)
        self.assertIn('log_types', stats)
        self.assertIn('modules', stats)
        
        self.assertGreater(stats['total_logs'], 0)
        self.assertGreater(len(stats['log_types']), 0)
        self.assertGreater(len(stats['modules']), 0)
        
    def test_log_filtering(self):
        """Test log filtering by time"""
        # Generate old log
        self.logger.info("Old message")
        
        # Wait a bit
        import time
        time.sleep(2)
        
        # Generate new log
        test_message = "Test message"
        self.logger.info(test_message)
        
        # Get logs from last second
        logs = self.analyzer.get_logs(hours=0.0001)
        
        # Should only get the new log
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0]['message'], test_message)

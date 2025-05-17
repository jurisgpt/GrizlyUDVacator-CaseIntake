import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock, patch
from grizly_app.utils.error_framework import catch_errors, handle_app_error

class TestErrorFramework:
    def setup_method(self, method):
        self.mock_st = Mock()
        self.mock_log_error = Mock()

    @patch('grizly_app.utils.error_framework.st', new_callable=Mock)
    @patch('grizly_app.utils.error_framework.log_error', new_callable=Mock)
    def test_handle_app_error(self, mock_log_error, mock_st):
        """Test error handling with different error types"""
        # Test form validation error
        error = ValueError("Invalid date format")
        context = {"field": "date_format", "value": "2025-01-01"}
        
        result = handle_app_error("form_validation", error, context)
        
        assert result is False
        mock_log_error.assert_called_once()
        mock_st.error.assert_called()
        mock_st.info.assert_called()
        
        # Reset mocks
        mock_log_error.reset_mock()
        mock_st.reset_mock()
        
        # Test with show_technical=True
        result = handle_app_error("form_validation", error, context, show_technical=True)
        
        assert result is False
        mock_st.expander.assert_called()

    def test_catch_errors_decorator(self):
        """Test the catch_errors decorator"""
        
        @catch_errors
        def test_function(date_str):
            if not date_str:
                raise ValueError("Date is required")
            return datetime.fromisoformat(date_str)

        # Test successful case
        result = test_function("2025-01-01")
        assert result is None

        # Test error case
        result = test_function("invalid-date")
        assert result is False

        # Test None input
        result = test_function(None)
        assert result is False

    def test_datetime_handling(self):
        """Test datetime validation"""
        
        @catch_errors
        def validate_date(date_str):
            try:
                return datetime.fromisoformat(date_str)
            except ValueError:
                raise ValueError(f"Invalid date format: {date_str}")

        # Test valid date
        result = validate_date("2025-01-01")
        assert isinstance(result, datetime)

        # Test invalid date
        result = validate_date("invalid-date")
        assert result is False

        # Test future date
        today = datetime.now()
        future_date = today + timedelta(days=1)
        result = validate_date(future_date.strftime("%Y-%m-%d"))
        assert result is False

    def test_error_context(self):
        """Test error context preservation"""
        
        @catch_errors
        def process_data(data):
            if not data:
                raise ValueError("Data is required")
            return data

        # Test with context
        result = process_data({"key": "value"})
        assert result is False

    def test_error_recovery(self):
        """Test error recovery mechanism"""
        
        @catch_errors
        def recoverable_operation():
            try:
                raise Exception("Test error")
            except Exception:
                return "Recovered"

        result = recoverable_operation()
        assert result == "Recovered"

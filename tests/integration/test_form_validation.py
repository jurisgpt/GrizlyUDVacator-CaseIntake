import pytest
from datetime import datetime
from grizly_app.ui.error_handler import validate_form_data

class TestFormValidation:
    def test_valid_form_data(self):
        """Test validation with valid form data"""
        data = {
            'served_date': '2025-01-01',
            'motion_date': '2025-01-15',
            'participated': True,
            'actual_notice': False,
            'relied_on_bad_advice': False
        }
        
        result = validate_form_data(data)
        assert result is True

    def test_missing_required_fields(self):
        """Test validation with missing required fields"""
        # Test missing served_date
        data = {'motion_date': '2025-01-15'}
        result = validate_form_data(data)
        assert result is False

        # Test missing motion_date
        data = {'served_date': '2025-01-01'}
        result = validate_form_data(data)
        assert result is False

    def test_invalid_date_format(self):
        """Test validation with invalid date formats"""
        data = {
            'served_date': '01-01-2025',  # Invalid format
            'motion_date': '2025-01-15'
        }
        result = validate_form_data(data)
        assert result is False

    def test_future_dates(self):
        """Test validation with future dates"""
        today = datetime.now()
        tomorrow = today + timedelta(days=1)
        
        data = {
            'served_date': tomorrow.strftime('%Y-%m-%d'),  # Future date
            'motion_date': tomorrow.strftime('%Y-%m-%d')
        }
        result = validate_form_data(data)
        assert result is False

    def test_invalid_date_relationship(self):
        """Test validation with invalid date relationship"""
        data = {
            'served_date': '2025-01-15',
            'motion_date': '2025-01-01'  # Motion date before served date
        }
        result = validate_form_data(data)
        assert result is False

    def test_complete_form_validation(self):
        """Test complete form validation with all fields"""
        data = {
            'served_date': '2025-01-01',
            'motion_date': '2025-01-15',
            'participated': True,
            'actual_notice': False,
            'relied_on_bad_advice': False,
            'extra_field': 'should_be_ignored'
        }
        result = validate_form_data(data)
        assert result is True

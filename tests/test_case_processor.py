import pytest
from grizly_app.case_processor import CaseProcessor
import json

def test_case_processing_error():
    """Test case processing with error handling"""
    processor = CaseProcessor()
    
    # Test case with invalid data
    case_data = {
        'case_id': '123',
        'case_type': 'invalid',  # This will trigger an error
        'filing_date': '2025-01-01'
    }
    
    # Process the case (should trigger error)
    result = processor.process_case(case_data)
    
    # Check that error was handled and logged
    with open('logs/error.log', 'r') as f:
        log_entries = f.readlines()
        last_entry = json.loads(log_entries[-1])
        
        assert last_entry['error_type'] == 'function_error'
        assert 'Invalid case type' in last_entry['error_message']
        assert 'process_case' in last_entry['function']
        
    assert result is False  # Function should return False on error

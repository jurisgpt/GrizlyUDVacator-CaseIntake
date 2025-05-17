import pytest
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_logging_imports():
    """
    Test that logging module imports work correctly from different locations
    """
    # Test importing from external_form_tab
    from grizly_app.ui.external_form_tab import render_external_form_tab
    assert 'render_external_form_tab' in dir(render_external_form_tab)
    
    # Test importing from error_handler
    from grizly_app.ui.error_handler import handle_app_error
    assert 'handle_app_error' in dir(handle_app_error)
    
    # Test importing from external_content
    from grizly_app.ui.components.external_content import render_external_content
    assert 'render_external_content' in dir(render_external_content)

def test_error_framework_imports():
    """
    Test that error framework imports work correctly
    """
    from grizly_app.utils.error_framework import catch_errors, handle_app_error
    assert callable(catch_errors)
    assert callable(handle_app_error)

def test_logging_functionality():
    """
    Test that logging functions can be called from different modules
    """
    from grizly_app.utils.logging import log_info, log_error
    
    # Test basic logging
    log_info("test", {"test": "info"})
    log_error("test", {"test": "error"})
    
    # Test logging from external module
    from grizly_app.ui.external_form_tab import render_external_form_tab
    render_external_form_tab()  # This should trigger logging

def test_module_structure():
    """
    Test that module structure is correct and all required files exist
    """
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Check for required directories
    assert os.path.exists(os.path.join(project_root, 'grizly_app'))
    assert os.path.exists(os.path.join(project_root, 'grizly_app', 'ui'))
    assert os.path.exists(os.path.join(project_root, 'grizly_app', 'utils'))
    
    # Check for required files
    assert os.path.exists(os.path.join(project_root, 'grizly_app', 'app.py'))
    assert os.path.exists(os.path.join(project_root, 'grizly_app', 'utils', 'logging.py'))
    assert os.path.exists(os.path.join(project_root, 'grizly_app', 'utils', 'error_framework.py'))
    assert os.path.exists(os.path.join(project_root, 'grizly_app', 'ui', 'external_form_tab.py'))
    assert os.path.exists(os.path.join(project_root, 'grizly_app', 'ui', 'components', 'external_content.py'))

def test_error_handling():
    """
    Test that error handling works across modules
    """
    from grizly_app.utils.error_framework import catch_errors
    
    @catch_errors
    def test_function():
        raise ValueError("Test error")
    
    result = test_function()
    assert result is False

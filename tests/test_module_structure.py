import pytest
import os
import sys

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_grizly_app_package_structure():
    """Test that grizly_app package structure is correct"""
    # Test that grizly_app is a package
    import grizly_app
    assert os.path.exists(os.path.join(grizly_app.__path__[0], '__init__.py'))
    
    # Test that required submodules exist
    required_submodules = [
        'ui'
    ]
    
    for submodule in required_submodules:
        assert os.path.exists(os.path.join(grizly_app.__path__[0], submodule, '__init__.py'))
    
    # Test that standalone modules exist
    standalone_modules = [
        'response_logic.py'
    ]
    
    for module in standalone_modules:
        assert os.path.exists(os.path.join(grizly_app.__path__[0], module))
    
    # Test that root-level modules exist
    root_modules = [
        'legal_logic.py'
    ]
    
    for module in root_modules:
        assert os.path.exists(os.path.join(os.path.dirname(grizly_app.__path__[0]), module))

def test_ui_structure():
    """Test that UI components are properly structured"""
    from grizly_app.ui import (
        intake_form_tab,
        motion_summary_tab,
        legal_reasoning_tab,
        decision_tree_tab,
        attachments_tab,
        external_form_tab,
        footer,
        global_styles,
        css_utils
    )
    
    # Verify that all components have their required functions
    assert hasattr(intake_form_tab, 'render_intake_tab')
    assert hasattr(motion_summary_tab, 'render_motion_tab')
    assert hasattr(legal_reasoning_tab, 'render_reasoning_tab')
    assert hasattr(decision_tree_tab, 'render_decision_tree_tab')
    assert hasattr(attachments_tab, 'render_attachments_tab')
    assert hasattr(external_form_tab, 'render_external_form_tab')
    assert hasattr(footer, 'render_footer')
    assert hasattr(global_styles, 'apply_global_styles')
    assert hasattr(css_utils, 'reduce_top_padding')

def test_utils_structure():
    """Test that utils are properly structured"""
    from utils import (
        logging,
        config,
        forms,
        session
    )
    
    # Verify that all utils have their required functions
    assert hasattr(logging, 'log_event')
    assert hasattr(config, 'load_questions')
    assert hasattr(config, 'load_config')
    assert hasattr(forms, 'render_intake_form')
    assert hasattr(session, 'init_session_state')

if __name__ == "__main__":
    pytest.main([__file__])

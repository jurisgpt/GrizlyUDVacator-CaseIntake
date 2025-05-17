import pytest
import os
import sys

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_app_imports():
    """Test all imports from app.py"""
    # Test UI tab components
    from grizly_app.ui.intake_form_tab import render_intake_tab
    from grizly_app.ui.motion_summary_tab import render_motion_tab
    from grizly_app.ui.legal_reasoning_tab import render_reasoning_tab
    from grizly_app.ui.decision_tree_tab import render_decision_tree_tab
    from grizly_app.ui.attachments_tab import render_attachments_tab
    from grizly_app.ui.external_form_tab import render_external_form_tab

    # Test UI utilities
    from grizly_app.ui.footer import render_footer
    from grizly_app.ui.global_styles import apply_global_styles
    from grizly_app.ui.css_utils import reduce_top_padding

    # Test that all functions are callable
    assert callable(render_intake_tab)
    assert callable(render_motion_tab)
    assert callable(render_reasoning_tab)
    assert callable(render_decision_tree_tab)
    assert callable(render_attachments_tab)
    assert callable(render_external_form_tab)
    assert callable(render_footer)
    assert callable(apply_global_styles)
    assert callable(reduce_top_padding)

def test_utils_imports():
    """Test imports from utils directory"""
    from utils.logging import log_event
    from utils.config import load_questions, load_config
    from utils.forms import render_intake_form
    from utils.session import init_session_state

    # Test that all functions are callable
    assert callable(log_event)
    assert callable(load_questions)
    assert callable(load_config)
    assert callable(render_intake_form)
    assert callable(init_session_state)

def test_legal_logic_imports():
    """Test imports from legal logic"""
    from legal_logic import evaluate_rules
    assert callable(evaluate_rules)

def test_streamlit_app_imports():
    """Test imports from streamlit app"""
    # Test that we can import the app module
    import streamlit_app
    assert streamlit_app is not None
    
    # Test that we can import the app
    from grizly_app import app
    assert app is not None

if __name__ == "__main__":
    pytest.main([__file__])

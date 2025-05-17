import os
import sys
from datetime import datetime

# Add project root to Python path - this MUST be at the top
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

import streamlit as st

from grizly_app.ui.attachments_tab import render_attachments_tab
from grizly_app.ui.css_utils import reduce_top_padding
from grizly_app.ui.decision_tree_tab import render_decision_tree_tab
from grizly_app.ui.external_form_tab import render_external_form_tab
from grizly_app.ui.footer import render_footer
from grizly_app.ui.global_styles import apply_global_styles
from grizly_app.ui.intake_form_tab import render_intake_tab
from grizly_app.ui.legal_reasoning_tab import render_reasoning_tab
from grizly_app.ui.monitoring_tab import show_log_dashboard
from grizly_app.ui.motion_summary_tab import render_motion_tab
from grizly_app.utils.logging import log_error, log_info


def main():
    # Log application startup
    log_info("app_startup", {"version": "1.0.0", "timestamp": datetime.now().isoformat()})
    
    # Set layout to wide for a full-width professional feel
    # ✅ Set layout to wide for a full-width professional feel
    st.set_page_config(
        page_title="Tenant Relief Evaluation Tool",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Log page configuration
    log_info("page_config", {"layout": "wide", "sidebar_state": "expanded"})

    # Apply global styles
    log_info("app_styles", {"action": "applying_global_styles"})
    reduce_top_padding()
    apply_global_styles()
    log_info("app_styles", {"action": "styles_applied"})
    
    # Add some spacing
    st.markdown("<br>", unsafe_allow_html=True)

    # Define tab definitions
    TAB_DEFINITIONS = [
        ("📋 Intake Form", "intake"),
        ("🔍 Case Insights", "motion"),
        ("🧠 Legal Reasoning", "reasoning"),
        ("🌳 Decision Tree", "decision_tree"),
        ("📂 Attachments", "attachments"),
        ("📨 Input Form", "external_form"),
        ("📊 Health Monitoring", "monitoring")
    ]

    # Initialize tab state if not exists
    log_info("tab_state", {"action": "initializing", "current_state": st.session_state.get('current_tab', 'unknown')})
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = TAB_DEFINITIONS[0][1]  # Default to first tab
    
    # Initialize force_tab if not exists
    log_info("tab_state", {"action": "initializing_force_tab", "current_value": st.session_state.get('force_tab', 'unknown')})
    if 'force_tab' not in st.session_state:
        st.session_state.force_tab = None
        # Removed the line that was deleting the 'force_tab' key and calling st.rerun()
    
    # Get the current tab index
    tab_keys = [tab[1] for tab in TAB_DEFINITIONS]
    current_tab_index = tab_keys.index(st.session_state.current_tab)

    # Create tabs
    tab_labels = [label for label, _ in TAB_DEFINITIONS]
    tabs = st.tabs(tab_labels)

    # Tab handlers mapping
    tab_handlers = {
        "intake": render_intake_tab,
        "motion": render_motion_tab,
        "reasoning": render_reasoning_tab,
        "decision_tree": render_decision_tree_tab,
        "attachments": render_attachments_tab,
        "external_form": render_external_form_tab,
        "monitoring": show_log_dashboard
    }

    # Render all tabs
    for i, (label, key) in enumerate(TAB_DEFINITIONS):
        with tabs[i]:
            try:
                if key in ["motion", "reasoning", "decision_tree"]:
                    if "evaluation" in st.session_state:
                        tab_handlers[key]()
                    else:
                        st.info("👈 Complete the Intake Form first")
                        if st.button("Go to Intake", key=f"goto_intake_{key}"):
                            st.session_state["force_tab"] = "intake"
                            st.rerun()
                else:
                    tab_handlers[key]()
            except Exception as e:
                st.error(f"Error rendering {label}: {str(e)}")
                st.markdown("---")
                st.code(f"Tab handler: {key}")
                st.code(f"Error: {str(e)}")

    # ✅ Global footer
    render_footer()


if __name__ == "__main__":
    main()

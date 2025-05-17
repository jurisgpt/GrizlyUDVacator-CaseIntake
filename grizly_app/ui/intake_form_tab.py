import os
import sys
from datetime import date, datetime
import logging

print("Starting intake_form_tab.py")
print("Current working directory:", os.getcwd())
print("PYTHONPATH:", os.environ.get('PYTHONPATH', 'Not set'))

import streamlit as st

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from grizly_app.utils.error_framework import catch_errors, handle_app_error
from grizly_app.utils.logging import log_error, log_info
from grizly_app.legal_logic_aligned import evaluate_rules


def validate_form_data(facts: dict) -> bool:
    """
    Validate form data before processing.
    
    Args:
        facts: Dictionary containing form data
        
    Returns:
        bool: True if data is valid, False otherwise
    """
    try:
        log_info("form_validation", {"action": "starting", "data_keys": list(facts.keys())})
        # Validate dates
        served_date = facts.get('served_date')
        motion_date = facts.get('motion_date')
        
        if not served_date or not motion_date:
            log_error("form_validation", {"error": "missing_dates", "missing": []})
            st.error("Please select both service and motion dates.")
            return False
            
        if motion_date < served_date:
            log_error("form_validation", {"error": "invalid_dates", "motion": str(motion_date), "served": str(served_date)})
            st.error("Motion date cannot be before service date.")
            return False
            
        # Validate boolean fields
        for field in ['participated', 'actual_notice', 'relied_on_bad_advice']:
            if field not in facts:
                log_error("form_validation", {"error": "missing_field", "field": field})
                st.error(f"Missing required field: {field}")
                return False
                
        log_info("form_validation", {"action": "success", "data_keys": list(facts.keys())})
        return True
    except Exception as e:
        log_error("form_validation", {"error": "exception", "message": str(e), "type": type(e).__name__})
        st.error(f"Error validating form data: {str(e)}")
        return False

@catch_errors
def render_intake_tab():
    try:
        # Log form render
        log_info("form_rendered", {"component": "intake_form"})

        # ----------------------------------------------------------------------------
        # UI FORM SECTION
        # ----------------------------------------------------------------------------

        with st.form(key="intake_form"):
            try:
                # Form inputs with validation
                served_date = st.date_input("📅 When were you served court papers?", 
                                         key="served_date", 
                                         max_value=date.today())
                motion_date = st.date_input("📅 Estimated date of filing Motion to Vacate Default Judgment (if eligible)", 
                                         key="motion_date", 
                                         max_value=date.today())

                participated = st.checkbox("❓ Did you (Tenant) participate in the lawsuit before default?")
                actual_notice = st.checkbox("❓ Did you (Tenant) know about the lawsuit before the judgment?")
                bad_advice = st.checkbox("❓ Did a legal professional tell you (Tenant) nothing could be done (bad legal advice)?")

                submitted = st.form_submit_button("✅ Evaluate Legal Relief")

                if submitted:
                    try:
                        # Log form submission
                        log_info("form_submitted", {
                            "served_date": str(served_date),
                            "motion_date": str(motion_date),
                            "participated": participated,
                            "actual_notice": actual_notice,
                            "bad_advice": bad_advice
                        })

                        # Collect form data
                        facts = {
                            'served_date': served_date,
                            'motion_date': motion_date,
                            'participated': participated,
                            'actual_notice': actual_notice,
                            'relied_on_bad_advice': bad_advice
                        }
                        
                        # Validate form data
                        if not validate_form_data(facts):
                            return
                        
                        # Process form data
                        try:
                            evaluation = evaluate_rules(facts)
                            st.session_state['evaluation'] = evaluation
                            st.session_state['facts'] = facts

                            # Navigate to motion tab
                            st.session_state['force_tab'] = 'motion'
                            st.session_state['show_success'] = True
                            st.rerun()

                        except Exception as e:
                            handle_app_error("form_submission", e, {
                                "facts": facts
                            })
                            return
                    except Exception as e:
                        handle_app_error('form_submission', e)
            except Exception as e:
                handle_app_error('form_render', e)
    except Exception as e:
        handle_app_error('form_render', e)

    # Show success message if redirected from form submission
    if st.session_state.get("show_success", False):
        st.success("✅ Review case insights and eligibility potential based on the information provided by clicking Case Insights tab above.")
        st.session_state["show_success"] = False  # Clear the flag

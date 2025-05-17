from datetime import datetime

import streamlit as st

from grizly_app.utils.error_framework import catch_errors, handle_app_error
from grizly_app.utils.logging import log_error

# Legacy error handler - use handle_app_error instead
# def handle_error(error_type: str, error: Exception, context: dict = None):
#     """Handle errors gracefully with logging and user feedback.
#     
#     Args:
#         error_type (str): Type of error (e.g., 'form_render', 'form_submission')
#         error (Exception): The caught exception
#         context (dict, optional): Additional context information for logging
#     """
#     # Log the error with context
#     log_error(error_type, {
#         "error_message": str(error),
#         "error_type": type(error).__name__,
#         "timestamp": datetime.now().isoformat(),
#         **(context or {})
#     })
#     
#     # Show appropriate user feedback
#     if error_type == 'form_render':
#         st.error("An unexpected error occurred while rendering the form. Please try again or contact support.")
#     elif error_type == 'form_submission':
#         st.error("An error occurred while processing your form. Please check your inputs and try again.")
#     
#     # Clear any pending state
#     st.session_state.pop("show_success", None)
#     st.session_state.pop("evaluation", None)
#     st.session_state.pop("facts", None)
#     
#     return False

@catch_errors
def validate_form_data(data: dict) -> bool:
    """Validate form data before processing.
    
    Args:
        data (dict): Form data to validate
        
    Returns:
        bool: True if data is valid, False otherwise
    """
    try:
        # Basic validation
        served_date = data.get('served_date')
        motion_date = data.get('motion_date')
        
        if not served_date:
            st.error("Please select a valid served date")
            return False
            
        if not motion_date:
            st.error("Please select a valid motion date")
            return False
            
        # Validate date format
        try:
            served_date = datetime.fromisoformat(served_date)
            motion_date = datetime.fromisoformat(motion_date)
        except ValueError as e:
            handle_app_error("form_validation", e, {
                "field": "date_format",
                "value": served_date or motion_date
            })
            return False
            
        # Validate date relationship
        if motion_date < served_date:
            st.error("Motion date cannot be before served date")
            return False
            
        # Validate dates are not in the future
        today = datetime.now()
        if served_date > today:
            st.error("Served date cannot be in the future")
            return False
            
        if motion_date > today:
            st.error("Motion date cannot be in the future")
            return False
            
        return True
    except Exception as e:
        handle_app_error("form_validation", e, data)
        return False

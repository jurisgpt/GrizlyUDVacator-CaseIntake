import datetime
import json
import logging
import traceback
from typing import Any, Callable, Dict, Optional

import streamlit as st

# Use basic logging setup
logger = logging.getLogger(__name__)

def log_error(error_type: str, error_data: Dict):
    """
    Log an error with detailed context.
    
    Args:
        error_type: Type/category of error (e.g., 'validation', 'api', 'system')
        error_data: Dictionary containing error details
    """
    error_data['timestamp'] = datetime.now().isoformat()
    error_data['error_type'] = error_type
    logger.error(json.dumps(error_data, indent=2))

def log_info(event_type: str, data: Dict):
    """
    Log an info-level event.
    
    Args:
        event_type: Type of event
        data: Dictionary containing event data
    """
    data['timestamp'] = datetime.datetime.now().isoformat()
    data['event_type'] = event_type
    logger.info(json.dumps(data, indent=2))

def log_error(error_type: str, error_data: Dict):
    """
    Log an error with detailed context.
    
    Args:
        error_type: Type/category of error (e.g., 'validation', 'api', 'system')
        error_data: Dictionary containing error details
    """
    error_data['timestamp'] = datetime.now().isoformat()
    error_data['error_type'] = error_type
    logger.error(json.dumps(error_data, indent=2))

def handle_app_error(
    error_type: str, 
    exception: Exception, 
    context: Optional[Dict[str, Any]] = None,
    show_technical: bool = False
) -> bool:
    """
    Centralized error handler that:
    1. Logs the error with full context
    2. Provides user-friendly error message
    3. Optionally shows technical details
    
    Returns False to indicate error occurred
    """
    # Log detailed error
    error_data = {
        "error_message": str(exception),
        "error_type": type(exception).__name__,
        "stack_trace": traceback.format_exc(),
        "timestamp": datetime.datetime.now().isoformat(),
        **(context or {})
    }
    log_error(error_type, error_data)
    log_info("error_handled", {"error_type": error_type, "handled": True})
    
    # Show user-friendly error message
    st.error(f"An error occurred: {str(exception)}")
    
    # Optionally show technical details
    if show_technical:
        with st.expander("Technical Details"):
            st.code(error_data)
    
    return False

def catch_errors(func: Callable) -> Callable:
    """
    Decorator to automatically catch and handle errors in functions.
    Preserves function signature and returns False on error.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return handle_app_error(
                "function_error",
                e,
                {
                    "function": func.__name__,
                    "args": str(args),
                    "kwargs": str(kwargs)
                }
            )
    return wrapper

def safe_module_operation(module_name: str, operation: Callable) -> bool:
    """
    Safely execute operations within a module to prevent module-level crashes.
    
    Args:
        module_name: Name of the module being operated on
        operation: Callable operation to perform
    
    Returns:
        True if operation succeeded, False if error occurred
    """
    try:
        result = operation()
        return True
    except Exception as e:
        handle_app_error(
            "module_error",
            e,
            {
                "module": module_name,
                "operation": operation.__name__
            }
        )
        return False

def monitor_recurring_errors(error_log_file: str = "logs/error.log") -> Dict[str, int]:
    """
    Monitor error log for recurring patterns.
    
    Returns:
        Dictionary of error patterns and their occurrence counts
    """
    error_patterns = {}
    try:
        with open(error_log_file, 'r') as f:
            for line in f:
                try:
                    error_data = json.loads(line)
                    error_key = f"{error_data['error_type']}:{error_data['error_message']}"
                    error_patterns[error_key] = error_patterns.get(error_key, 0) + 1
                except:
                    continue
    except:
        return {}
    
    return error_patterns

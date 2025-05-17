import logging
import os
import sys
from datetime import datetime
from typing import Dict, Optional
import json

import streamlit as st

# Configure logging
LOG_DIR = "logs"
APP_LOG_FILE = os.path.join(LOG_DIR, "app.json")
ERROR_LOG_FILE = os.path.join(LOG_DIR, "error.json")

# Create logs directory with proper permissions
try:
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR, exist_ok=True)
        os.chmod(LOG_DIR, 0o755)
except Exception as e:
    print(f"Error creating logs directory: {e}")

# Configure app logger (info level)
try:
    logging.basicConfig(
        filename=APP_LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)
except Exception as e:
    print(f"Error configuring app logger: {e}")

# Configure error logger (error level)
try:
    error_handler = logging.FileHandler(ERROR_LOG_FILE)
    error_handler.setLevel(logging.ERROR)
    error_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    error_handler.setFormatter(error_formatter)
    
    error_logger = logging.getLogger('error_logger')
    error_logger.addHandler(error_handler)
    error_logger.setLevel(logging.ERROR)
    
    # Also log errors to console for immediate visibility
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)
    console_handler.setFormatter(error_formatter)
    error_logger.addHandler(console_handler)
except Exception as e:
    print(f"Error configuring error logger: {e}")

# Initialize session state logs if not exists
try:
    if "logs" not in st.session_state:
        st.session_state.logs = []
except:
    # If we're not in a Streamlit context, just ignore
    pass

# Helper function to safely get session state
def get_session_state() -> Optional[Dict]:
    """Get Streamlit session state safely."""
    try:
        return st.session_state
    except:
        return None

def log_event(event_type: str, data: Dict, level: str = "INFO"):
    """Log an event with specified level."""
    try:
        # Prepare log entry
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "name": __name__,
            "levelname": level.upper(),
            "message": f"{event_type}: {json.dumps(data, default=str)}",
            "module": __name__.split('.')[-1],
            "funcName": "log_event",
            "lineno": 0  # We'll set this to 0 since we're not tracking line numbers
        }

        # Write to appropriate file
        try:
            with open(ERROR_LOG_FILE if level.upper() == "ERROR" else APP_LOG_FILE, 'a') as f:
                f.write(json.dumps(log_entry) + "\n")
        except Exception as e:
            print(f"Error writing to log file: {str(e)}")

        # Add to session state if available
        try:
            session_state = get_session_state()
            if session_state:
                session_state.logs.append(log_entry)
        except Exception as e:
            print(f"Failed to log to session state: {str(e)}")
    except Exception as e:
        print(f"Critical error in log_event: {str(e)}")

def log_error(event_type: str, data: Dict):
    """Log an error-level event."""
    try:
        log_event(event_type, data, "ERROR")
    except Exception as e:
        print(f"Error in log_error: {str(e)}")

def log_info(event_type: str, data: Dict):
    """Log an info-level event."""
    try:
        log_event(event_type, data, "INFO")
    except Exception as e:
        print(f"Error in log_info: {str(e)}")

def show_debug_panel():
    """Show debug panel with session state and event log."""
    try:
        session_state = get_session_state()
        if session_state:
            st.subheader("Debug Panel")
            with st.expander("Session State"):
                try:
                    st.json(dict(session_state))
                except Exception as e:
                    st.error(f"Failed to display session state: {str(e)}")
            
            with st.expander("Event Log"):
                try:
                    st.json(session_state.logs)
                except Exception as e:
                    st.error(f"Failed to display event log: {str(e)}")
    except Exception as e:
        print(f"Error in show_debug_panel: {str(e)}")



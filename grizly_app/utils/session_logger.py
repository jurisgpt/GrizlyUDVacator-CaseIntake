import json
from datetime import datetime
from typing import Optional

import streamlit as st


class SessionLogger:
    def __init__(self):
        self.is_streamlit = False
        try:
            import streamlit as st
            self.is_streamlit = True
        except ImportError:
            pass
            
    def log_to_session(self, level: str, message: str):
        """Log to session state if in Streamlit context"""
        if not self.is_streamlit:
            return
            
        try:
            if "logs" not in st.session_state:
                st.session_state.logs = []
                
            log_entry = {
                'timestamp': datetime.now().isoformat(),
                'level': level,
                'message': message
            }
            st.session_state.logs.append(log_entry)
        except Exception as e:
            print(f"Error logging to session: {str(e)}")

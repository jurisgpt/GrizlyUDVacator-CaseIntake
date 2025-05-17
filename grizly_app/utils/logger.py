import datetime
import json
import logging
from typing import Any, Dict, Optional

from grizly_app.utils.error_handler import ErrorHandler
from grizly_app.utils.logger_manager import LoggerManager
from grizly_app.utils.session_logger import SessionLogger


class UnifiedLogger:
    def __init__(self):
        self.manager = LoggerManager()
        self.error_handler = ErrorHandler(self.manager.get_logger())
        self.session_logger = SessionLogger()
        
    def log(self, level: str, message: str, metadata: Optional[Dict[str, Any]] = None):
        """Unified logging method"""
        data = {
            'timestamp': datetime.datetime.now().isoformat(),
            'level': level,
            'message': message,
            **(metadata or {})
        }
        
        # Log to appropriate handlers
        if level.upper() == 'ERROR':
            self.error_handler.log_error('application', Exception(message), metadata)
        else:
            self.manager.get_logger().info(json.dumps(data, indent=2))
            
        # Log to session if in Streamlit
        self.session_logger.log_to_session(level, message)

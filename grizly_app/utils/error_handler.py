import datetime
import json
import logging
import traceback
from typing import Any, Dict, Optional


class ErrorHandler:
    def __init__(self, logger):
        self.logger = logger
        
    def log_error(self, error_type: str, exception: Exception, context: Optional[Dict[str, Any]] = None, suppress: bool = False):
        """Log error with proper context"""
        error_data = {
            'timestamp': datetime.datetime.now().isoformat(),
            'error_type': error_type,
            'message': str(exception),
            'stack_trace': traceback.format_exc(),
            **(context or {})
        }
        self.logger.error(json.dumps(error_data, indent=2))
        
        # Only suppress exception if explicitly requested
        if not suppress:
            raise exception
            
    def error_decorator(self, suppress: bool = False):
        """Decorator for error handling"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    self.log_error(
                        error_type=func.__name__,
                        exception=e,
                        context={'function': func.__name__, 'args': args, 'kwargs': kwargs},
                        suppress=suppress
                    )
            return wrapper
        return decorator

import functools
import logging
import time
from typing import Callable


def trace_handler_write():
    """Monkeypatch logging handlers to trace write operations"""
    original_emit = logging.FileHandler.emit
    
    def tracking_emit(self, record):
        print(f"\n=== Handler Write Trace ===")
        print(f"Handler: {self.baseFilename}")
        print(f"Level: {logging.getLevelName(record.levelno)}")
        print(f"Message: {record.getMessage()}")
        print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("=== End Trace ===")
        original_emit(self, record)
    
    logging.FileHandler.emit = tracking_emit

def trace_method(func: Callable):
    """Decorator to trace method calls"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n=== Method Trace: {func.__name__} ===")
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        print("=== End Trace ===")
        return result
    return wrapper

def debug_logger_setup():
    """Set up debug logging"""
    # Create a debug logger
    debug_logger = logging.getLogger('debug')
    debug_logger.setLevel(logging.DEBUG)
    
    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    
    # Add handler
    debug_logger.addHandler(ch)
    
    return debug_logger

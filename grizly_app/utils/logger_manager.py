import json
import logging
import logging.config
import os
from datetime import datetime

from grizly_app.utils.debug_utils import debug_logger_setup, trace_method
from grizly_app.utils.file_utils import (check_file_permissions,
                                         test_file_writable)

# Set up debug logger
debug_logger = debug_logger_setup()

class LoggerManager:
    # Constants for log filenames
    LOG_FILENAME = 'app.json'
    ERROR_FILENAME = 'error.json'
    
    @trace_method
    def __init__(self, log_dir=None):
        """Initialize logger with optional custom log directory"""
        debug_logger.debug("Initializing LoggerManager")
        debug_logger.debug(f"Log directory: {log_dir}")
        
        # Store log directory first
        self.log_dir = log_dir
        
        # Get or create logger
        self.logger = logging.getLogger('grizly_app')
        
        # Check if logger is already configured
        if not self.logger.handlers:  # Only configure if no handlers exist
            debug_logger.debug("Logger not configured, proceeding with setup")
            
            # Configure logging
            debug_logger.debug("Configuring logging")
            self.configure_logging(log_dir)
            
            # Ensure log directory exists
            debug_logger.debug("Ensuring log directory")
            self.ensure_log_directory()
        else:
            debug_logger.debug("Logger already configured, skipping setup")
        
    @trace_method
    def configure_logging(self, log_dir=None):
        """Configure logging using dictConfig"""
        debug_logger.debug("Configuring logging")
        debug_logger.debug(f"Log directory: {log_dir}")
        
        # Use provided log directory or default to 'logs'
        log_dir = log_dir or "logs"
        
        # Get logger and check for existing handlers
        logger = logging.getLogger('grizly_app')
        
        # Check if we need to configure handlers
        if not logger.handlers:
            debug_logger.debug("No existing handlers, configuring new ones")
            logger.handlers.clear()  # Clear handlers before configuration
            logger.propagate = False
        else:
            debug_logger.debug(f"{len(logger.handlers)} existing handlers found")
            # Remove any StreamHandlers if they exist
            logger.handlers = [h for h in logger.handlers if not isinstance(h, logging.StreamHandler)]
            logger.propagate = False
        
        # Ensure log directory exists before configuration
        try:
            os.makedirs(log_dir, exist_ok=True)
            debug_logger.debug(f"Log directory created: {log_dir}")
        except Exception as e:
            debug_logger.error(f"Error creating log directory: {e}")
            raise
        
        # Start tracing handler writes
        from grizly_app.utils.debug_utils import trace_handler_write
        trace_handler_write()
        
        # Custom JSON formatter class
        class CustomJsonFormatter(logging.Formatter):
            def format(self, record):
                log_entry = {
                    'timestamp': datetime.fromtimestamp(record.created).isoformat(),
                    'name': record.name,
                    'levelname': record.levelname,
                    'message': record.getMessage(),
                    'module': record.module,
                    'funcName': record.funcName,
                    'lineno': record.lineno
                }
                return json.dumps(log_entry, ensure_ascii=False) + '\n'

        # Create formatter instances
        json_formatter = CustomJsonFormatter()
        error_formatter = CustomJsonFormatter()
        standard_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Create formatter instances
        json_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(module)s - %(funcName)s - %(lineno)d')
        error_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(module)s - %(funcName)s - %(lineno)d')
        standard_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        LOGGING_CONFIG = {
            'version': 1,
            'disable_existing_loggers': True,
            'formatters': {
                'json': {
                    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(module)s - %(funcName)s - %(lineno)d'
                },
                'error': {
                    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(module)s - %(funcName)s - %(lineno)d'
                },
                'standard': {
                    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                }
            },
            'handlers': {
                'file': {
                    'class': 'logging.FileHandler',
                    'filename': os.path.join(log_dir, self.LOG_FILENAME),
                    'formatter': 'json',
                    'level': 'INFO',
                    'encoding': 'utf-8'
                },
                'error_file': {
                    'class': 'logging.FileHandler',
                    'filename': os.path.join(log_dir, self.ERROR_FILENAME),
                    'formatter': 'error',
                    'level': 'ERROR',
                    'encoding': 'utf-8'
                },
                'console': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'standard',
                    'level': 'ERROR'
                }
            },
            'loggers': {
                'grizly_app': {
                    'handlers': ['file', 'error_file', 'console'],
                    'level': 'INFO',
                    'propagate': False
                }
            }
        }
        
        debug_logger.debug("Applying logging configuration")
        logging.config.dictConfig(LOGGING_CONFIG)
        
        # Get the configured logger
        logger = logging.getLogger('grizly_app')
        
        # Ensure console handler exists
        if not any(h.name == 'console' for h in logger.handlers):
            console_handler = logging.StreamHandler()
            console_handler.name = 'console'
            console_handler.setLevel(logging.ERROR)
            console_handler.setFormatter(standard_formatter)
            logger.addHandler(console_handler)
            
        # Debug print complete logger configuration
        debug_logger.debug("=== Logger Configuration ===")
        debug_logger.debug(f"Logger name: {logger.name}")
        debug_logger.debug(f"Logger level: {logging.getLevelName(logger.level)}")
        debug_logger.debug(f"Logger propagate: {logger.propagate}")
        debug_logger.debug(f"Logger handlers: {len(logger.handlers)}")
        
        # Print detailed handler information
        for i, handler in enumerate(logger.handlers):
            debug_logger.debug(f"\nHandler {i}: {type(handler).__name__}")
            debug_logger.debug(f"  Name: {handler.name if hasattr(handler, 'name') else 'N/A'}")
            debug_logger.debug(f"  Level: {logging.getLevelName(handler.level)}")
            debug_logger.debug(f"  Formatter: {handler.formatter._fmt if handler.formatter else None}")
            if isinstance(handler, logging.FileHandler):
                debug_logger.debug(f"  Path: {handler.baseFilename}")
            elif isinstance(handler, logging.StreamHandler):
                debug_logger.debug(f"  Stream: {handler.stream}")
        
        # Verify exactly 2 FileHandlers and 1 StreamHandler
        file_handlers = [h for h in logger.handlers if isinstance(h, logging.FileHandler)]
        stream_handlers = [h for h in logger.handlers if isinstance(h, logging.StreamHandler)]
        
        debug_logger.debug(f"\nFile handlers found: {len(file_handlers)}")
        debug_logger.debug(f"Stream handlers found: {len(stream_handlers)}")
        
        # Verify formatter patterns
        for handler in logger.handlers:
            formatter = handler.formatter
            if formatter:
                debug_logger.debug(f"\nHandler {type(handler).__name__} formatter pattern:")
                debug_logger.debug(f"  Format: {formatter._fmt}")
                debug_logger.debug(f"  Date format: {formatter.datefmt if hasattr(formatter, 'datefmt') else 'default'}")
        
        debug_logger.debug("Logging configuration complete")
        
    @trace_method
    def ensure_log_directory(self):
        """Ensure log directory exists and has proper permissions"""
        debug_logger.debug("Ensuring log directory")
        debug_logger.debug(f"Log directory: {self.log_dir}")
        
        if not self.log_dir:
            debug_logger.debug("No log directory specified")
            return
            
        try:
            # Create directory if it doesn't exist
            if not os.path.exists(self.log_dir):
                debug_logger.debug("Creating log directory")
                os.makedirs(self.log_dir, exist_ok=True)
                debug_logger.debug(f"Log directory created: {self.log_dir}")
                # Set permissions to allow read/write by all
                os.chmod(self.log_dir, 0o777)
            else:
                debug_logger.debug(f"Using existing log directory: {self.log_dir}")
                
            # Check directory permissions
            dir_perms = check_file_permissions(self.log_dir)
            debug_logger.debug(f"Directory permissions: {dir_perms}")
            
            # Create test files if they don't exist
            log_file = os.path.join(self.log_dir, self.LOG_FILENAME)
            error_file = os.path.join(self.log_dir, self.ERROR_FILENAME)
            
            # Test file permissions
            for file_path in [log_file, error_file]:
                # Create empty file if it doesn't exist
                if not os.path.exists(file_path):
                    debug_logger.debug(f"Creating file: {file_path}")
                    open(file_path, 'a').close()
                    os.chmod(file_path, 0o666)
                
                # Check permissions
                file_perms = check_file_permissions(file_path)
                debug_logger.debug(f"File {os.path.basename(file_path)} permissions: {file_perms}")
                
                # Test if we can write to the file
                write_test = test_file_writable(file_path)
                debug_logger.debug(f"Write test for {os.path.basename(file_path)}: {'success' if write_test else 'failed'}")
                
                # Set proper permissions if needed
                if not file_perms['writable']:
                    try:
                        debug_logger.debug(f"Setting permissions for {file_path} to 666")
                        os.chmod(file_path, 0o666)
                    except Exception as e:
                        debug_logger.error(f"Error setting permissions for {file_path}: {e}")
                        
        except Exception as e:
            debug_logger.error(f"Error ensuring log directory: {e}")
            raise
            
    def get_logger(self, name=None):
        """Get properly configured logger with correct level"""
        debug_logger.debug(f"Getting logger: {name if name else 'root'}")
        
        if name:
            child_logger = self.logger.getChild(name)
            # Clear existing handlers to prevent duplicates
            child_logger.handlers.clear()
            # Inherit handlers from parent
            for handler in self.logger.handlers:
                child_logger.addHandler(handler)
            # Set level to match parent
            child_logger.setLevel(self.logger.level)
            # Prevent propagation to avoid duplicate messages
            child_logger.propagate = False
        else:
            child_logger = self.logger
            # Clear and reapply handlers to ensure no duplicates
            child_logger.handlers.clear()
            for handler in logging.getLogger('grizly_app').handlers:
                child_logger.addHandler(handler)
            child_logger.propagate = False

        debug_logger.debug(f"Logger {child_logger.name} has {len(child_logger.handlers)} handlers")
        return child_logger

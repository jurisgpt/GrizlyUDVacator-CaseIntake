from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional


@dataclass
class MonitoringState:
    """Class to manage monitoring dashboard state."""
    
    time_range: int = 12
    error_count: int = 0
    app_logs_count: int = 0
    unique_errors: int = 0
    prev_unique_errors: int = 0
    last_update: datetime = datetime.now()
    prev_error_count: int = 0
    prev_app_logs_count: int = 0
    
    def update_metrics(self, error_count: int, app_logs_count: int, unique_errors: int):
        """Update monitoring metrics."""
        self.prev_error_count = self.error_count
        self.prev_app_logs_count = self.app_logs_count
        self.prev_unique_errors = self.unique_errors
        
        self.error_count = error_count
        self.app_logs_count = app_logs_count
        self.unique_errors = unique_errors
        self.last_update = datetime.now()

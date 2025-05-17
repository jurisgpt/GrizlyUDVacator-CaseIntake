import json
import os
from collections import deque
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional


class LogAnalyzer:
    """Analyze and visualize log data"""

    def __init__(self, log_dir: str = "logs") -> None:
        """Initialize LogAnalyzer with default settings"""
        self.log_dir = log_dir
        self.error_log_file = os.path.join(self.log_dir, "error.json")
        self.app_log_file = os.path.join(self.log_dir, "app.json")
        
        # Ensure log directory exists
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def log_file_exists(self, file_type: str = "app") -> bool:
        """Check if log file exists"""
        if file_type == "error":
            return os.path.exists(self.error_log_file)
        return os.path.exists(self.app_log_file)

    def get_recent_logs(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Retrieve most recent log entries"""
        if not self.log_file_exists():
            return []
        
        try:
            with open(self.app_log_file, 'r') as f:
                # Read last N lines efficiently
                lines = deque(f, maxlen=limit)
                return [json.loads(line) for line in lines if line.strip()]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading logs: {str(e)}")
            return []

    def get_logs(self, hours: int = 24, error_only: bool = False) -> List[Dict]:
        """Get logs from last N hours"""
        cutoff_time = datetime.now() - timedelta(hours=hours)
        logs = []
        
        try:
            # Use error log file for error logs
            if error_only:
                if not self.log_file_exists("error"):
                    return []
                with open(self.error_log_file, 'r') as f:
                    for line in f:
                        try:
                            # Parse JSON line
                            log_entry = json.loads(line.strip())
                            
                            # Extract timestamp from JSON
                            timestamp = datetime.fromisoformat(log_entry['timestamp'])
                            
                            if timestamp >= cutoff_time:
                                # Convert to our expected format
                                formatted_entry = {
                                    'timestamp': timestamp.isoformat(),
                                    'name': log_entry['name'],
                                    'levelname': log_entry['levelname'],
                                    'message': log_entry['message'],
                                    'module': log_entry['module'],
                                    'funcName': log_entry['funcName'],
                                    'lineno': log_entry['lineno']
                                }
                                logs.append(formatted_entry)
                        except Exception as e:
                            print(f"Error parsing JSON log entry: {e}")
                            continue
            # Use app log file for all logs
            else:
                if not self.log_file_exists():
                    return []
                with open(self.app_log_file, 'r') as f:
                    for line in f:
                        try:
                            # Parse JSON line
                            log_entry = json.loads(line.strip())
                            
                            # Extract timestamp from JSON
                            timestamp = datetime.fromisoformat(log_entry['timestamp'])
                            
                            if timestamp >= cutoff_time:
                                # Convert to our expected format
                                formatted_entry = {
                                    'timestamp': timestamp.isoformat(),
                                    'name': log_entry['name'],
                                    'levelname': log_entry['levelname'],
                                    'message': log_entry['message'],
                                    'module': log_entry['module'],
                                    'funcName': log_entry['funcName'],
                                    'lineno': log_entry['lineno']
                                }
                                logs.append(formatted_entry)
                        except Exception as e:
                            print(f"Error parsing JSON log entry: {e}")
                            continue
        except Exception as e:
            print(f"Error reading logs: {e}")
            return []
            
        return logs

    def get_error_logs(self, hours: int = 24) -> List[Dict]:
        """Get error logs from last N hours"""
        return self.get_logs(hours=hours, error_only=True)

    def get_app_logs(self, hours: int = 24) -> List[Dict]:
        """Get application logs from last N hours"""
        return self.get_logs(hours=hours, error_only=False)

    def get_error_trend(self, hours: int = 24, interval: str = 'hour') -> Dict[str, Any]:
        """Get error trend over time
        
        Args:
            hours: Number of hours to look back
            interval: Time interval ('hour' or 'day')
            
        Returns:
            Dictionary with error counts per interval
        """
        errors = self.get_error_logs(hours)
        trend: Dict[str, int] = {}
        
        for error in errors:
            timestamp = datetime.fromisoformat(error['timestamp'])
            
            if interval == 'hour':
                key = timestamp.strftime('%Y-%m-%d %H:00')
            else:  # day
                key = timestamp.strftime('%Y-%m-%d')
            
            trend[key] = trend.get(key, 0) + 1
            
        # Sort by time
        trend = dict(sorted(trend.items()))
        
        return {
            'data': trend,
            'total_errors': sum(trend.values()),
            'interval': interval
        }

# Remove this duplicate method - it's already defined earlier in the class

    def get_error_distribution(self, hours: int = 24) -> Dict[str, int]:
        """Get distribution of error types"""
        errors = self.get_error_logs(hours)
        distribution: Dict[str, int] = {}
        
        for error in errors:
            error_type = error.get('levelname', 'unknown')
            distribution[error_type] = distribution.get(error_type, 0) + 1
            
        return distribution

    def get_statistics(self, hours: int = 24) -> Dict[str, Any]:
        """Get log statistics"""
        logs = self.get_logs(hours)
        stats: Dict[str, Any] = {
            'total_logs': len(logs),
            'log_types': {},
            'modules': {}
        }
        
        for log in logs:
            log_type = log.get('levelname', 'unknown')  # Changed from error_type to levelname
            module = log.get('module', 'unknown')
            
            stats['log_types'][log_type] = stats['log_types'].get(log_type, 0) + 1
            stats['modules'][module] = stats['modules'].get(module, 0) + 1
            
        return stats

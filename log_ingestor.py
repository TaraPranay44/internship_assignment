import os
import json
from datetime import datetime

class LogIngestor:
    def _init_(self, config):
        # Load configuration
        self.config = config

        # Create log directory if not exists
        if not os.path.exists('logs'):
            os.makedirs('logs')

    def ingest_log(self, log_data):
        try:
            # Parse log data
            log_data = json.loads(log_data)

            # Validate log format
            required_fields = ['level', 'log_string', 'timestamp', 'metadata']
            if not all(field in log_data for field in required_fields):
                raise ValueError("Invalid log format. Missing required fields.")

            # Validate timestamp format
            datetime.strptime(log_data['timestamp'], '%Y-%m-%dT%H:%M:%SZ')

            # Write log to file
            log_file = os.path.join('logs', log_data['metadata']['source'])
            with open(log_file, 'a') as file:
                file.write(json.dumps(log_data) + '\n')

            return True, None
        except Exception as e:
            return False, str(e)
import os
import json

class LogQueryInterface:
    def _init_(self):
        pass

    def search_logs(self, search_query, filters=None):
        results = []
        log_files = [f for f in os.listdir('logs') if f.endswith('.log')]
        
        for log_file in log_files:
            with open(os.path.join('logs', log_file), 'r') as file:
                for line in file:
                    log_data = json.loads(line)
                    if self._filter_log(log_data, search_query, filters):
                        results.append(log_data)

        return results

    def _filter_log(self, log_data, search_query, filters):
        if filters:
            for key, value in filters.items():
                if key in log_data['metadata'] and log_data['metadata'][key] != value:
                    return False
        if search_query:
            if search_query.lower() not in log_data['log_string'].lower():
                return False
        return True

# Usage example:
query_interface = LogQueryInterface()
results = query_interface.search_logs("Inside the Search API", {"source": "log3.log"})
print(results)
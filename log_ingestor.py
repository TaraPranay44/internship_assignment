# log_ingestor.py

from flask import Flask, request
from datetime import datetime
import json
import os

from config import LOGGING_LEVELS, LOG_FILES
from database import get_session, LogEntry

app = Flask(__name__)

@app.route('/log/<api_name>', methods=['POST'])
def log(api_name):
    if api_name not in LOG_FILES:
        return {"error": "Invalid API name"}, 400
    
    log_data = request.json
    level = log_data.get('level')
    log_string = log_data.get('log_string')
    timestamp = log_data.get('timestamp', datetime.utcnow().isoformat())
    source = log_data.get('source', f'{api_name}.log')

    log_entry = {
        "level": level,
        "log_string": log_string,
        "timestamp": timestamp,
        "source": source
    }

    with open(LOG_FILES[api_name], 'a') as f:
        f.write(json.dumps(log_entry) + '\n')

    session = get_session()
    new_log = LogEntry(
        level=level,
        log_string=log_string,
        timestamp=datetime.fromisoformat(timestamp),
        source=source
    )
    session.add(new_log)
    session.commit()
    
    return {"message": "Log entry created"}, 201

if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.makedirs('logs')
    app.run(debug=True)

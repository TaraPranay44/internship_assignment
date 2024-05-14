# query_interface.py

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from database import get_session, LogEntry
from sqlalchemy import and_

app = Flask(__name__)
api = Api(app)

class QueryLogs(Resource):
    def get(self):
        level = request.args.get('level')
        log_string = request.args.get('log_string')
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')
        source = request.args.get('source')

        session = get_session()
        query = session.query(LogEntry)

        if level:
            query = query.filter(LogEntry.level == level)
        if log_string:
            query = query.filter(LogEntry.log_string.contains(log_string))
        if start_time and end_time:
            query = query.filter(and_(LogEntry.timestamp >= start_time, LogEntry.timestamp <= end_time))
        if source:
            query = query.filter(LogEntry.source == source)

        results = query.all()
        logs = [
            {
                "level": log.level,
                "log_string": log.log_string,
                "timestamp": log.timestamp.isoformat(),
                "source": log.source
            } for log in results
        ]
        
        return jsonify(logs)

api.add_resource(QueryLogs, '/query_logs')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

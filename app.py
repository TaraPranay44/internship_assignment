# app.py

from log_ingestor import app as log_ingestor_app
from query_interface import app as query_interface_app

if __name__ == '__main__':
    log_ingestor_app.run(port=5000)
    query_interface_app.run(port=5001)

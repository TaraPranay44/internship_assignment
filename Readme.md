
# Quality Log Control

## Overview

This project provides a logging and querying system that integrates with multiple APIs to store and query logs efficiently.

## Features

- Log Ingestor: Integrates with multiple APIs to capture logs.
- Query Interface: Provides a web interface to query logs based on various filters.
- Supports filtering by log level, log string, timestamp, and source.
- Efficient search and retrieval of log entries.

## Installation

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Set up the SQLite database by running `database.py`.

## Usage

1. Start the log ingestor service:
    ```bash
    python log_ingestor.py
    ```

2. Start the query interface service:
    ```bash
    python query_interface.py
    ```

3. Access the query interface at `http://localhost:5001/query_logs`.

## Example

To log data, send a POST request to `http://localhost:5000/log/<api_name>` with the following JSON body:
```json
{
    "level": "info",
    "log_string": "Example log message",
    "timestamp": "2023-09-15T08:00:00Z",
    "source": "log1.log"
}

# FastAPI Time API

## Description
This project implements a simple RESTful API using FastAPI, a modern web framework for building APIs with Python. The API provides a single endpoint, `/time`, which returns the current date and time in UTC format. Optionally, it allows users to specify a timezone offset to get the current time adjusted to that timezone.

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/geekmood/dwallo.git
    ```

2. **Install the required dependencies:**
    ```bash
    pip install fastapi pytest
    ```

3. **Run the FastAPI application:**
    ```bash
    fastapi dev main.py
    ```
    The API will be accessible at `http://localhost:8000`.

## Usage
### Endpoint
- `/time`: GET endpoint to retrieve the current date and time.

#### Query Parameters
- `timezone` (optional): A string representing a valid timezone offset (e.g., "+05:30").

### Example Usage
- To get the current time in UTC:
  ```bash
  curl http://localhost:8000/time?timezone=+06:00
  ```

### Testcase

**Run the test cases:**
```
pytest test.py
```

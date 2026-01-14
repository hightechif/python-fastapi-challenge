# Python FastAPI Challenges

Backend Challenge using FastAPI Python.

## Prerequisites

- [uv](https://github.com/astral-sh/uv)
- PostgreSQL

## Setup

1. **Install dependencies**:
    ```bash
    uv sync
    ```

2. **Configure Database**:
    Ensure a PostgreSQL database is running.
    The project expects a database URL. You can configure it in a `.env` file:
    ```
    DATABASE_URL=postgresql://user:password@localhost:5432/dbname
    ```

## Running the Application

Run the application using `uv`:

```bash
uv run uvicorn app.main:app --reload --port 8080
```

## API Documentation

Once running, access the documentation at:
- Swagger UI: [http://localhost:8080/docs](http://localhost:8080/docs)
- ReDoc: [http://localhost:8080/redoc](http://localhost:8080/redoc)

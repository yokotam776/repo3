# repo3

FastAPI application that returns the current date and time.

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
uvicorn src.main:app --reload
```

The API will be available at http://localhost:8000

## API Endpoints

- `GET /` - Welcome message
- `GET /current-datetime` - Returns the current date and time in multiple formats

## API Documentation

Interactive API documentation is available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

Run the tests with pytest:

```bash
pytest tests/test_main.py -v
```

## Example Response

```json
{
  "datetime": "2026-01-07T06:26:56.003505",
  "timestamp": 1767767216.003505,
  "year": 2026,
  "month": 1,
  "day": 7,
  "hour": 6,
  "minute": 26,
  "second": 56
}
```
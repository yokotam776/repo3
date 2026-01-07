from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="DateTime API")


@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "DateTime API"}


@app.get("/current-datetime")
def get_current_datetime():
    """Returns the current date and time"""
    current_time = datetime.now()
    return {
        "datetime": current_time.isoformat(),
        "timestamp": current_time.timestamp(),
        "year": current_time.year,
        "month": current_time.month,
        "day": current_time.day,
        "hour": current_time.hour,
        "minute": current_time.minute,
        "second": current_time.second
    }

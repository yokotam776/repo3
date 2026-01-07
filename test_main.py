import pytest
from fastapi.testclient import TestClient
from datetime import datetime
from main import app

client = TestClient(app)


def test_read_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "DateTime API"}


def test_get_current_datetime():
    """Test the current datetime endpoint"""
    # Get the datetime before making the request
    before = datetime.now()
    
    response = client.get("/current-datetime")
    
    # Get the datetime after making the request
    after = datetime.now()
    
    assert response.status_code == 200
    data = response.json()
    
    # Check that all expected keys are present
    assert "datetime" in data
    assert "timestamp" in data
    assert "year" in data
    assert "month" in data
    assert "day" in data
    assert "hour" in data
    assert "minute" in data
    assert "second" in data
    
    # Verify the datetime string can be parsed
    returned_datetime = datetime.fromisoformat(data["datetime"])
    
    # Check that the returned datetime is between before and after
    assert before <= returned_datetime <= after
    
    # Verify timestamp matches the datetime
    assert abs(returned_datetime.timestamp() - data["timestamp"]) < 1
    
    # Verify individual components
    assert data["year"] == returned_datetime.year
    assert data["month"] == returned_datetime.month
    assert data["day"] == returned_datetime.day
    assert data["hour"] == returned_datetime.hour
    assert data["minute"] == returned_datetime.minute
    assert data["second"] == returned_datetime.second


def test_get_current_datetime_format():
    """Test that the datetime is in ISO format"""
    response = client.get("/current-datetime")
    assert response.status_code == 200
    data = response.json()
    
    # Verify ISO format can be parsed
    datetime_str = data["datetime"]
    parsed = datetime.fromisoformat(datetime_str)
    assert isinstance(parsed, datetime)


def test_get_current_datetime_types():
    """Test that the response has correct data types"""
    response = client.get("/current-datetime")
    assert response.status_code == 200
    data = response.json()
    
    assert isinstance(data["datetime"], str)
    assert isinstance(data["timestamp"], (int, float))
    assert isinstance(data["year"], int)
    assert isinstance(data["month"], int)
    assert isinstance(data["day"], int)
    assert isinstance(data["hour"], int)
    assert isinstance(data["minute"], int)
    assert isinstance(data["second"], int)

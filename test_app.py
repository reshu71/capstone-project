import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app import app

# 1. Initialize the Test Client
# This "client" acts like a web browser.
client = TestClient(app)

def test_health_check():
    """Test the root endpoint /"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "online",
        "service": "Currency Converter API",
        "version": "1.0.0"
    }

# 2. Test the Happy Path (Mocking the Logic)
# We patch 'app.converter.fetch_rate' because that is the specific instance
# the web server is using.
@patch('app.converter.fetch_rate')
def test_convert_success(mock_fetch):
    # ARRANGE: Force the rate to be 0.85
    mock_fetch.return_value = 0.85

    # ACT: Send a GET request to the endpoint
    response = client.get("/convert?amount=100&target=EUR")

    # ASSERT: Check Status Code and JSON Data
    assert response.status_code == 200
    
    data = response.json()
    assert data['target_currency'] == "EUR"
    assert data['converted_amount'] == 85.0
    assert data['rate_used'] == 0.85

# 3. Test the Error Path
@patch('app.converter.fetch_rate')
def test_convert_failure(mock_fetch):
    # ARRANGE: Force the logic to crash
    mock_fetch.side_effect = ValueError("Currency XXX not supported")

    # ACT: Request with bad data
    response = client.get("/convert?amount=100&target=XXX")

    # ASSERT: The API should catch the crash and return a 400 Bad Request
    assert response.status_code == 400
    assert response.json()['detail'] == "Currency XXX not supported"
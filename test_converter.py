import pytest
import requests
import sys
from unittest.mock import Mock,patch
from converter import fetch_rate,convert_currency

@patch("converter.convert_currency")
def test_math_logic(mock_get):
    amount = convert_currency(100,1.2)
    assert amount == 120.0

@patch("converter.requests.get")
def test_api_mock(mock_get):
    response = Mock()
    response.status_code = 200
    # mock_get.return_value = response

    response.json.return_value = {"rates": {"EUR": 0.853}}

    mock_get.return_value = response

    rate = fetch_rate("EUR")

    assert rate == 0.853





    

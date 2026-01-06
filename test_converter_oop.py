import pytest
from unittest.mock import Mock, patch
from converter_oop import CurrencyConverter


@patch('converter_oop.requests.Session')
def test_fetch_rate_success(mock_session_cls):

    mock_instance = mock_session_cls.return_value # mocking the constructor call

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"EUR": 0.853}}

    mock_instance.get.return_value = mock_response

    converter = CurrencyConverter('https://api.exchangerate-api.com/v4/latest/USD')

    rate = converter.fetch_rate('EUR')

    assert rate==0.853

    mock_instance.get.assert_called_once()



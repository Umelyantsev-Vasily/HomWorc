import pytest
from unittest.mock import patch, Mock
from src.external_api import get_amount_in_rub
import requests


def test_get_amount_in_rub_rub():
    """Тест для транзакции в рублях (должна возвращать сумму как есть)"""
    transaction = {
        "operationAmount": {
            "amount": "1000.00",
            "currency": {
                "code": "RUB"
            }
        }
    }
    assert get_amount_in_rub(transaction) == 1000.00


@patch('your_module.requests.get')
def test_get_amount_in_rub_usd_success(mock_get):
    """Тест успешной конвертации USD в RUB"""
    # Настраиваем мок для requests.get
    mock_response = Mock()
    mock_response.json.return_value = {"result": 7500.50}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "code": "USD"
            }
        }
    }

    result = get_amount_in_rub(transaction)
    assert result == 7500.50
    mock_get.assert_called_once()


@patch('your_module.requests.get')
def test_get_amount_in_rub_eur_success(mock_get):
    """Тест успешной конвертации EUR в RUB"""
    # Настраиваем мок для requests.get
    mock_response = Mock()
    mock_response.json.return_value = {"result": 8500.75}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "code": "EUR"
            }
        }
    }

    result = get_amount_in_rub(transaction)
    assert result == 8500.75
    mock_get.assert_called_once()


@patch('your_module.requests.get')
def test_get_amount_in_rub_api_error(mock_get):
    """Тест обработки ошибки API"""
    mock_get.side_effect = requests.exceptions.RequestException("API error")

    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "code": "USD"
            }
        }
    }

    with pytest.raises(Exception, match="Ошибка конвертации валюты: API error"):
        get_amount_in_rub(transaction)


@patch('your_module.requests.get')
def test_get_amount_in_rub_invalid_response(mock_get):
    """Тест обработки невалидного ответа API"""
    mock_response = Mock()
    mock_response.json.return_value = {}  # Нет ключа "result"
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "code": "USD"
            }
        }
    }

    with pytest.raises(Exception, match="Ошибка конвертации валюты:"):
        get_amount_in_rub(transaction)


def test_get_amount_in_rub_invalid_amount():
    """Тест обработки невалидной суммы в транзакции"""
    transaction = {
        "operationAmount": {
            "amount": "invalid",
            "currency": {
                "code": "USD"
            }
        }
    }

    with pytest.raises(Exception, match="Ошибка конвертации валюты:"):
        get_amount_in_rub(transaction)


def test_get_amount_in_rub_missing_data():
    """Тест обработки отсутствия необходимых данных"""
    transaction = {}

    with pytest.raises(Exception, match="Ошибка конвертации валюты:"):
        get_amount_in_rub(transaction)
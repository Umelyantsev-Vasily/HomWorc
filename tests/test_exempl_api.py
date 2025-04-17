import unittest
from unittest.mock import MagicMock, patch

import requests

from src.external_api import get_amount_in_rub


class TestGetAmountInRub(unittest.TestCase):

    def test_rub_transaction(self):
        """Тест для транзакции в рублях (конвертация не требуется)."""
        transaction = {"operationAmount": {"amount": "1000.00", "currency": {"code": "RUB"}}}
        result = get_amount_in_rub(transaction)
        self.assertEqual(result, 1000.00)

    @patch("requests.get")
    def test_usd_conversion(self, mock_get):
        """Тест успешной конвертации USD в RUB."""
        # Настраиваем мок для requests.get
        mock_response = MagicMock()
        mock_response.json.return_value = {"result": 7500.50}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}
        result = get_amount_in_rub(transaction)
        self.assertEqual(result, 7500.50)
        mock_get.assert_called_once()

    @patch("requests.get")
    def test_api_error(self, mock_get):
        """Тест обработки ошибки API."""
        mock_get.side_effect = requests.exceptions.RequestException("API недоступен")

        transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "EUR"}}}
        with self.assertRaises(Exception) as context:
            get_amount_in_rub(transaction)
        self.assertTrue("Ошибка конвертации валюты" in str(context.exception))

    def test_invalid_amount(self):
        """Тест с невалидной суммой транзакции."""
        transaction = {"operationAmount": {"amount": "не число", "currency": {"code": "USD"}}}
        with self.assertRaises(Exception) as context:
            get_amount_in_rub(transaction)
        self.assertTrue("Ошибка конвертации валюты" in str(context.exception))

    def test_missing_currency(self):
        """Тест с отсутствующей валютой."""
        transaction = {"operationAmount": {"amount": "100.00", "currency": {}}}  # Нет кода валюты
        # По умолчанию должна использоваться RUB
        result = get_amount_in_rub(transaction)
        self.assertEqual(result, 100.00)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch, MagicMock
import requests
from src.external_api import get_amount_in_rub
from src.external_api import process_transactions
from io import StringIO
import sys


class TestGetAmountInRub(unittest.TestCase):

    def setUp(self):
        # Общие тестовые данные
        self.rub_transaction = {
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "RUB"}
            }
        }
        self.usd_transaction = {
            "operationAmount": {
                "amount": "50.00",
                "currency": {"code": "USD"}
            }
        }
        self.eur_transaction = {
            "operationAmount": {
                "amount": "75.00",
                "currency": {"code": "EUR"}
            }
        }
        self.invalid_transaction = {
            "operationAmount": {
                "amount": "invalid",
                "currency": {"code": "USD"}
            }
        }
        self.missing_currency_transaction = {
            "operationAmount": {
                "amount": "100.00"
            }
        }

    @patch('src.external_api.requests.get')
    def test_rub_transaction_no_conversion(self, mock_get):
        """Тест транзакции в рублях (без конвертации)"""
        result = get_amount_in_rub(self.rub_transaction)
        self.assertEqual(result, 100.00)
        mock_get.assert_not_called()

    @patch('src.external_api.requests.get')
    def test_usd_transaction_with_conversion(self, mock_get):
        """Тест конвертации USD в RUB"""
        # Настраиваем мок ответа API
        mock_response = MagicMock()
        mock_response.json.return_value = {"result": 3750.00}  # 50 USD * 75 RUB/USD
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = get_amount_in_rub(self.usd_transaction)
        self.assertEqual(result, 3750.00)

        # Проверяем параметры вызова API
        mock_get.assert_called_once()
        args, kwargs = mock_get.call_args
        self.assertEqual(kwargs['params']['from'], 'USD')
        self.assertEqual(kwargs['params']['to'], 'RUB')
        self.assertEqual(kwargs['params']['amount'], 50.00)

    @patch('src.external_api.requests.get')
    def test_eur_transaction_with_conversion(self, mock_get):
        """Тест конвертации EUR в RUB"""
        mock_response = MagicMock()
        mock_response.json.return_value = {"result": 8250.00}  # 75 EUR * 110 RUB/EUR
        mock_get.return_value = mock_response

        result = get_amount_in_rub(self.eur_transaction)
        self.assertEqual(result, 8250.00)
        mock_get.assert_called_once()


    @patch('src.external_api.requests.get')
    def test_api_error_handling(self, mock_get):
        """Тест обработки ошибки API"""
        mock_get.side_effect = requests.exceptions.RequestException("API Error")

        with self.assertRaises(Exception) as context:
            get_amount_in_rub(self.usd_transaction)

        self.assertIn("Ошибка конвертации валюты: API Error", str(context.exception))

    @patch('src.external_api.requests.get')
    def test_invalid_amount_format(self, mock_get):
        """Тест неверного формата суммы"""
        with self.assertRaises(Exception) as context:
            get_amount_in_rub(self.invalid_transaction)

        self.assertIn("Ошибка конвертации валюты", str(context.exception))
        mock_get.assert_not_called()

    @patch('src.external_api.requests.get')
    def test_missing_currency_code(self, mock_get):
        """Тест отсутствия кода валюты"""
        result = get_amount_in_rub(self.missing_currency_transaction)
        self.assertEqual(result, 100.00)  # Должен использовать RUB по умолчанию
        mock_get.assert_not_called()

    @patch('src.external_api.requests.get')
    def test_api_response_without_result(self, mock_get):
        """Тест некорректного ответа API (без поля result)"""
        mock_response = MagicMock()
        mock_response.json.return_value = {"error": "Invalid API key"}
        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            get_amount_in_rub(self.usd_transaction)

        self.assertIn("Ошибка конвертации валюты", str(context.exception))


if __name__ == '__main__':
    unittest.main()

# 2

class TestProcessTransactions(unittest.TestCase):
    def setUp(self):
        # Сохраняем оригинальный stdout для восстановления после тестов
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()  # Перенаправляем вывод в StringIO

    def tearDown(self):
        # Восстанавливаем оригинальный stdout
        sys.stdout = self.original_stdout

    @patch('src.external_api.load_transactions')
    @patch('src.external_api.get_amount_in_rub')
    def test_successful_processing(self, mock_get_amount, mock_load_transactions):
        """Тест успешной обработки транзакций"""
        # Настраиваем моки
        mock_load_transactions.return_value = [
            {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "RUB"}}},
            {"id": 2, "operationAmount": {"amount": "50", "currency": {"code": "USD"}}}
        ]
        mock_get_amount.side_effect = [100.0, 3750.0]  # RUB -> 100, USD -> 3750 (50 * 75)

        # Вызываем тестируемую функцию
        process_transactions()

        # Получаем вывод
        output = sys.stdout.getvalue().strip().split('\n')

        # Проверяем вывод
        self.assertIn("Транзакция 1: 100.0 руб.", output)
        self.assertIn("Транзакция 2: 3750.0 руб.", output)

    @patch('src.external_api.load_transactions')
    @patch('src.external_api.get_amount_in_rub')
    def test_skip_non_dict_transactions(self, mock_get_amount, mock_load_transactions):
        """Тест пропуска транзакций, которые не являются словарями"""
        mock_load_transactions.return_value = [
            "invalid transaction",
            {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}
        ]
        mock_get_amount.return_value = 100.0

        process_transactions()

        output = sys.stdout.getvalue().strip().split('\n')
        self.assertEqual(len(output), 1)  # Только одна транзакция обработана
        self.assertIn("Транзакция 1: 100.0 руб.", output)
        mock_get_amount.assert_called_once()  # Вызывался только для валидной транзакции

    @patch('src.external_api.load_transactions')
    @patch('src.external_api.get_amount_in_rub')
    def test_error_handling(self, mock_get_amount, mock_load_transactions):
        """Тест обработки ошибок при конвертации"""
        mock_load_transactions.return_value = [
            {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "EUR"}}}
        ]
        mock_get_amount.side_effect = Exception("API недоступен")

        process_transactions()

        output = sys.stdout.getvalue().strip()
        self.assertIn("Ошибка обработки транзакции 1: API недоступен", output)

    @patch('src.external_api.load_transactions')
    @patch('src.external_api.get_amount_in_rub')
    def test_transaction_without_id(self, mock_get_amount, mock_load_transactions):
        """Тест обработки транзакции без ID"""
        mock_load_transactions.return_value = [
            {"operationAmount": {"amount": "200", "currency": {"code": "RUB"}}}
        ]
        mock_get_amount.return_value = 200.0

        process_transactions()

        output = sys.stdout.getvalue().strip()
        self.assertIn("Транзакция без ID: 200.0 руб.", output)

    @patch('src.external_api.load_transactions')
    def test_empty_transactions_list(self, mock_load_transactions):
        """Тест обработки пустого списка транзакций"""
        mock_load_transactions.return_value = []

        process_transactions()

        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "")  # Ничего не должно быть выведено


if __name__ == '__main__':
    unittest.main()

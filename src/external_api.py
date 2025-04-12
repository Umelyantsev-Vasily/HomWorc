import os
import requests
from dotenv import load_dotenv

from src.utils import load_transactions

load_dotenv()

EXCHANGE_RATES_API_KEY = os.getenv("API_KEY")
BASE_API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def get_amount_in_rub(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    Для USD/EUR использует текущий курс через API.

    Args:
        transaction: Словарь с информацией о транзакции

    Returns:
        Сумма транзакции в рублях (float)

    Raises:
        Exception: Если произошла ошибка при конвертации
    """
    try:
        # Извлекаем данные из транзакции
        operation_amount = transaction.get("operationAmount", {})
        amount = float(operation_amount.get("amount", 0))
        currency = operation_amount.get("currency", {}).get("code", "RUB")

        # Если валюта уже в рублях, возвращаем как есть
        if currency == "RUB":
            return amount

        # Формируем параметры запроса
        params = {"to": "RUB", "from": currency, "amount": amount}

        # Отправляем запрос к API
        response = requests.get(BASE_API_URL, params=params, headers={"apikey": EXCHANGE_RATES_API_KEY}, timeout=10)
        response.raise_for_status()  # Проверяем на ошибки HTTP

        # Получаем и возвращаем результат конвертации
        result = response.json()
        return round(result["result"], 2)

    except (requests.exceptions.RequestException, KeyError, ValueError) as e:
        raise Exception(f"Ошибка конвертации валюты: {str(e)}")


def process_transactions():
    """Обрабатывает список транзакций, конвертируя суммы в рубли."""
    transactions = load_transactions("../data/operations.json")

    for transaction in transactions:
        try:
            # Проверяем, что это действительно транзакция
            if not isinstance(transaction, dict):
                continue

            amount_rub = get_amount_in_rub(transaction)
            transaction_id = transaction.get("id", "без ID")
            print(f"Транзакция {transaction_id}: {amount_rub} руб.")
        except Exception as e:
            transaction_id = transaction.get("id", "без ID")
            print(f"Ошибка обработки транзакции {transaction_id}: {str(e)}")


if __name__ == "__main__":
    process_transactions()

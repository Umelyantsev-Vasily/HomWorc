import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()

EXCHANGE_RATES_API_KEY = os.getenv("API_KEY")
BASE_API_URL = "https://api.apilayer.com/exchangerates_data/convert"

logger = logging.getLogger(__name__)

# Настройка обработчиков
file_handler = logging.FileHandler("logs/external_api.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)  # Убедимся, что обработчик принимает все уровни

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Форматтеры
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)

console_formatter = logging.Formatter("%(levelname)s: %(message)s")
console_handler.setFormatter(console_formatter)

# Добавляем обработчики к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)


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
        logger.info("Извлекаем данные из транзакции")
        operation_amount = transaction.get("operationAmount", {})
        amount = float(operation_amount.get("amount", 0))
        currency = operation_amount.get("currency", {}).get("code", "RUB")

        # Если валюта уже в рублях, возвращаем как есть
        logger.info("Проверяем валюту")
        if currency == "RUB":
            return amount

        # Формируем параметры запроса
        params = {"to": "RUB", "from": currency, "amount": amount}
        logger.info(f"Формируем параметры запроса {params}")

        # Отправляем запрос к API
        logger.info("Отправляем запрос к API")
        response = requests.get(BASE_API_URL, params=params, headers={"apikey": EXCHANGE_RATES_API_KEY}, timeout=10)
        response.raise_for_status()  # Проверяем на ошибки HTTP

        # Получаем и возвращаем результат конвертации
        result = response.json()
        logger.info("Получаем и возвращаем результат конвертации")
        return round(result["result"], 2)

    except (requests.exceptions.RequestException, KeyError, ValueError) as e:
        logger.error(f"Ошибка конвертации валюты: {e}")
        raise Exception(f"Ошибка конвертации валюты: {str(e)}")


# def process_transactions(transaction):
#     """Обрабатывает список транзакций, конвертируя суммы в рубли."""
#
#
#     try:
#         logger.info("Проверяем, что это действительно транзакция")
#         if not isinstance(transaction, dict):
#             return None
#
#         amount_rub = get_amount_in_rub(transaction)
#         transaction_id = transaction.get("id", "без ID")
#         print(f"Транзакция {transaction_id}: {amount_rub} руб.")
#         logger.info(f"Выводим {transaction_id}: {amount_rub} руб.")
#     except Exception as e:
#         transaction_id = transaction.get("id", "без ID")
#         logger.error(f"Ошибка обработки транзакции {e}")
#         print(f"Ошибка обработки транзакции {transaction_id}: {str(e)}")
#

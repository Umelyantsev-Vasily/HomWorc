from typing import Any, Dict, Iterator, List


def filter_by_currency(list_dict: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Функция которая  возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    for value in list_dict:
        # Проверяем по ключу значение, равно ли оно: currency, и возращаем
        try:
            if value.get("operationAmount").get("currency").get("code") == currency:
                yield value
        except AttributeError:
            continue


lst_dct = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]

title_filter_by_currency = filter_by_currency(lst_dct, "USD")
print(next(title_filter_by_currency))


def transaction_descriptions(list_dict: List[Dict[str, Any]]) -> Iterator[Dict[str, Any]]:
    """Генератор, который вызывает ValueError при отсутствии description"""
    for transfer_information in list_dict:
        if not isinstance(transfer_information, dict):
            raise ValueError("Ожидается словарь")

        if "description" not in transfer_information:
            continue  # Для отсутствующего поля

        title = transfer_information["description"]
        if title is None:
            continue  # Для None
        yield title


title_transaction_descriptions = transaction_descriptions(lst_dct)
print(next(title_transaction_descriptions))
print(next(title_transaction_descriptions))


def card_number_generator(start: int = 1, end: int = 9999999999999999) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    Генерирует последовательные номера в заданном диапазоне
    """
    if not 1 <= start <= end <= 9999999999999999:
        raise ValueError("Некорректный диапазон номеров карт")

    for number in range(start, end + 1):
        num_str = f"{number:016d}"  # Форматируем в 16 цифр с ведущими нулями
        yield f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"

    # Генерация первых 5 номеров карт


cards = card_number_generator(1, 5)
for card in cards:
    print(card)

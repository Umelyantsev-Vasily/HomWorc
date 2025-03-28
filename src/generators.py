def filter_by_currency(list_dict: list[dict], currency: str) -> iter:
    """Функция которая  возвращать итератор, который поочередно выдает транзакции,
     где валюта операции соответствует заданной (например, USD)."""
    for value in list_dict: # Перебираем список словарей
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
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "RUB",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }]

title_filter_by_currency = filter_by_currency(lst_dct,"USD")
print(next(title_filter_by_currency))




def transaction_descriptions(list_dict: list[dict:str]):
    """ Генератаор который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    for transfer_information in list_dict:
        title = transfer_information.get("description")
        if title is not None:
            yield title

title_transaction_descriptions = transaction_descriptions(lst_dct)
# print(next(title_transaction_descriptions))
# print(next(title_transaction_descriptions))
# print(next(title_transaction_descriptions))
from collections.abc import Iterator

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_basic_currency_filter(
    dict_filter_by_currency: list[dict], currency_arg: str, dict_filter_by_currency_result_1: list[dict]
) -> None:
    """Тест базовой фильтрации по валюте"""
    result = filter_by_currency(dict_filter_by_currency, currency_arg)
    assert isinstance(result, Iterator)
    assert next(result) == dict_filter_by_currency_result_1
    with pytest.raises(StopIteration):
        next(result)


def test_multiple_matches(dict_filter_by_currency_multiple: list[dict], currency_arg: str) -> None:
    """Тест нескольких совпадений"""
    result = filter_by_currency(dict_filter_by_currency_multiple, currency_arg)
    assert len(list(result)) == 2


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        ([], "USD", []),  # Тест с пустым списком
        ([{"operationAmount": {"amount": 100}}], "USD", []),  # Нет поля currency
        ([{"operationAmount": {"currency": {"code": "EUR"}}}], "USD", []),  # Другая валюта
        ([None], "USD", []),
        ([{"operationAmount": "invalid"}], "USD", []),
        ([{"operationAmount": {"currency": None}}], "USD", []),
    ],
)
def test_missing_currency_field(transactions: list[dict], currency: str, expected: list) -> None:
    """Тест обработки некорректных структур данных"""
    result = filter_by_currency(transactions, currency)
    assert list(result) == expected


def test_currency_case_sensitivity(currency_case_sensitivity: list[dict], currency_arg: str) -> None:
    """Тест чувствительности к регистру валюты"""
    result = filter_by_currency(currency_case_sensitivity, currency_arg)
    assert len(list(result)) == 1  # Только точное совпадение


# Тест генератора: transaction_descriptions


@pytest.mark.parametrize(
    "dict_list, extend_title",
    [
        (
            [
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
            ],
            "Перевод организации",
        )
    ],
)
def test_transaction_descriptions(dict_list: list[dict], extend_title: str) -> None:
    result = transaction_descriptions(dict_list)
    assert isinstance(result, Iterator)
    assert next(result) == extend_title


def test_normal_iteration_case(normal_transactions: list[dict]) -> None:
    result = transaction_descriptions(normal_transactions)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод с карты на карту"
    assert next(result) == "Оплата услуг"
    with pytest.raises(StopIteration):
        next(result)


def test_zero_iteration(empty_transactions: list) -> None:
    result = transaction_descriptions(empty_transactions)
    assert list(result) == []


def test_mixed_data(mixed_transactions: list[dict]) -> None:
    """Тест со смешанными данными"""
    result = transaction_descriptions(mixed_transactions)
    assert next(result) == "Зарплата"
    assert next(result) == ""  # Пустая строка не пропускается
    with pytest.raises(StopIteration):
        next(result)


def test_no_description_field(no_description_transactions: list[dict]) -> None:
    """Тест с транзакциями без поля description"""
    gen = transaction_descriptions(no_description_transactions)
    assert list(gen) == []  # Все элементы должны быть пропущены


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ([{"description": "Test"}], ["Test"]),
        ([{"description": "A"}, {"description": "B"}], ["A", "B"]),
        ([{"description": ""}], [""]),  # Пустое описание
        ([{"amount": 100}], []),  # Нет description
        ([{"description": None}], []),  # None
    ],
)
def test_parametrized(input_data: list[dict], expected: list) -> None:
    """Параметризованный тест разных случаев"""
    assert list(transaction_descriptions(input_data)) == expected


# Тест генератора card_number_generator
def test_card_number_generator(number_title: list[str]) -> None:
    result = card_number_generator(1, 5)
    assert isinstance(result, Iterator)
    assert next(result) == number_title[0]
    assert next(result) == number_title[1]
    assert next(result) == number_title[2]
    assert next(result) == number_title[3]
    assert next(result) == number_title[4]
    with pytest.raises(StopIteration):
        next(result)


def test_format_correctness() -> None:
    gen = card_number_generator(1234567812345678, 1234567812345678)
    card = next(gen)
    assert len(card) == 19  # 16 цифр + 3 пробела
    assert card.count(" ") == 3
    assert card.replace(" ", "").isdigit()
    assert card == "1234 5678 1234 5678"


def test_range_count_numb() -> None:
    with pytest.raises(ValueError, match="Некорректный диапазон"):
        list(card_number_generator(0, 5))  # start < 1

    with pytest.raises(ValueError):
        list(card_number_generator(5, 2))  # start > end

    with pytest.raises(ValueError):
        list(card_number_generator(1, 10000000000000000))  # end > 9999999999999999

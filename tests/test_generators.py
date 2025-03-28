import pytest

from src.generators import filter_by_currency

from collections.abc import Iterator


def test_basic_currency_filter(dict_filter_by_currency: list[dict], currency_arg: str, dict_filter_by_currency_result_1: list[dict]) -> None:
    """Тест базовой фильтрации по валюте"""
    result = filter_by_currency(dict_filter_by_currency, currency_arg)
    assert isinstance(result, Iterator)
    assert next(result) == dict_filter_by_currency_result_1
    with pytest.raises(StopIteration):
        next(result)


def test_multiple_matches(dict_filter_by_currency_multiple: list[dict], currency_arg: str )-> None:
    """Тест нескольких совпадений"""
    result = filter_by_currency(dict_filter_by_currency_multiple, currency_arg)
    assert len(list(result)) == 2


@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        ([], "USD", []),  # Тест с пустым списком
        (
            [{"operationAmount": {"amount": 100}}],  # Нет поля currency
            "USD",
            []
        ),
        (
            [{"operationAmount": {"currency": {"code": "EUR"}}}],  # Другая валюта
            "USD",
            []
        ),
        ([None], "USD", []),
        ([{"operationAmount": "invalid"}], "USD", []),
        ([{"operationAmount": {"currency": None}}],"USD", [])
    ]
)

def test_missing_currency_field(transactions: list[dict], currency: str, expected: list) -> None:
    """Тест обработки некорректных структур данных"""
    result = filter_by_currency(transactions, currency)
    assert list(result) == expected


def test_currency_case_sensitivity(currency_case_sensitivity: list[dict], currency_arg: str) ->None:
    """Тест чувствительности к регистру валюты"""
    result = filter_by_currency(currency_case_sensitivity, currency_arg)
    assert len(list(result)) == 1  # Только точное совпадение



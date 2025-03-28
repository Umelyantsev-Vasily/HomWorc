import pytest

from src.generators import filter_by_currency

from collections.abc import Iterator

import pytest
from collections.abc import Iterator


def test_basic_currency_filter(dict_filter_by_currency, currency_arg, dict_filter_by_currency_result_1):
    """Тест базовой фильтрации по валюте"""
    result = filter_by_currency(dict_filter_by_currency, currency_arg)
    assert isinstance(result, Iterator)
    assert next(result) == dict_filter_by_currency_result_1
    with pytest.raises(StopIteration):
        next(result)


def test_multiple_matches(dict_filter_by_currency_multiple, currency_arg ):
    """Тест нескольких совпадений"""
    result = filter_by_currency(dict_filter_by_currency_multiple, currency_arg)
    assert len(list(result)) == 2


def test_missing_currency_field(missing_currency_field, currency_arg):
    """Тест обработки отсутствующих полей (без исключения)"""
    result = filter_by_currency(missing_currency_field, currency_arg)
    assert list(result) == []  # Ожидаем пустой списо



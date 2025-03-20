from src.masks import get_mask_card_number
import pytest


@pytest.mark.parametrize(
    "number, expected_result",
    [
        ("1234567812345678", "1234 567** **** 5678"),
        ("8765432187654321", "8765 432** **** 4321"),
        ("1234123456785678", "1234 123** **** 5678"),
    ],
)
def test_get_mask_card_number(number, expected_result):
    assert get_mask_card_number(number) == expected_result


def test_get_mask_card_count_number_(number_card):
    assert get_mask_card_number(number_card) == "1234 567** **** 5678"


def test_get_mask_card_count_number_2(number_count):
    with pytest.raises(ValueError):
        assert get_mask_card_number(number_count)

def test_get_mask_card_count_number_2(number_count):
    with pytest.raises(ValueError):
        assert get_mask_card_number("1234")


def test_get_mask_card_str(str_card):
    with pytest.raises(ValueError):
        assert get_mask_card_number(str_card)

def test_get_mask_card_zero():
    with pytest.raises(ValueError):
        assert get_mask_card_number("")

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


@pytest.mark.parametrize(
    "number, expected",
    [("12345678123456789", ValueError), ("1234", ValueError), ("card", ValueError), ("", ValueError)],
)
def test_get_mask_card_error(number, expected):
    with pytest.raises(ValueError):
        assert get_mask_card_number(number) == expected

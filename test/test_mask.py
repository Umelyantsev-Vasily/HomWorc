import pytest

from src.masks import get_mask_account,get_mask_card_number

# Фунуция: get_mask_account
def test_get_mask_account_mask(mask_account_mask, mask_account_mask_return):
        assert get_mask_account(mask_account_mask) == mask_account_mask_return


@pytest.mark.parametrize(
    "x, expected",
    [
        ("1252156", ValueError),
        ("fgsagh", ValueError),
        ("123456789012345678900", ValueError),
        ("", ValueError),
        ("$%&*(*(**^#?>?<:{}", ValueError),
    ],
)
def test_get_mask_account_len(x, expected):
    with pytest.raises(ValueError):
        assert get_mask_account(x) == expected

# Функция get_mask_card_number

@pytest.mark.parametrize(
    "number, expected_result",
    [
        ("1234567812345678", "1234 67** **** 5678"),
        ("8765432187654321", "8765 32** **** 4321"),
        ("1234123456785678", "1234 23** **** 5678"),
    ],
)
def test_get_mask_card_number(number, expected_result):
    assert get_mask_card_number(number) == expected_result


def test_get_mask_card_number_2(mask_card, mask_card_mask):
    assert get_mask_card_number(mask_card) == mask_card_mask



@pytest.mark.parametrize(
    "number, expected",
    [("12345678123456789", ValueError), ("1234", ValueError), ("card", ValueError), ("", ValueError)],
)
def test_get_mask_card_error(number, expected):
    with pytest.raises(ValueError):
        assert get_mask_card_number(number) == expected

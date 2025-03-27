import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "num, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 92** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 7000792289606361", "MasterCard 7000 92** **** 6361"),
    ],
)
def test_mask_account_card(num: str, expected: str) -> None:
    assert mask_account_card(num) == expected


def test_mask_account_car_2(mask_get_mask: str, mask_get_mask_return: str) -> None:
    assert mask_account_card(mask_get_mask) == mask_get_mask_return


def test_mask_account_car_3(mask_account_card_account: str, mask_account_card_account_return: str) -> None:
    assert mask_account_card(mask_account_card_account) == mask_account_card_account_return


@pytest.mark.parametrize(
    "listed, title_expected",
    [
        ("Visa", ValueError),
        ("700079228960", ValueError),
        ("", ValueError),
        ("#%*_??><", ValueError),
        ("123456789012345678900985", ValueError),
        ("MasterCard", ValueError),
        ("1234567890", ValueError),
    ],
)
def test_mask_account_card_error(listed: str, title_expected: type) -> None:
    with pytest.raises(ValueError):
        assert mask_account_card(listed) == title_expected


@pytest.mark.parametrize(
    "num,date_expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2042-05-11T02:26:18.671407", "11.05.2042"),
        ("2023-10-01", "01.10.2023"),
    ],
)
def test_get_date(num: str, date_expected: str) -> None:
    assert get_date(num) == date_expected


def test_get_date_2(get_date_str: str, get_date_return: str) -> None:
    assert get_date(get_date_str) == get_date_return


@pytest.mark.parametrize(
    "text, date_expect", [("data", ValueError), ("", ValueError), ("gdys", ValueError), ("data", vars())]
)
def test_get_date_error(text: str, date_expect: type) -> None:
    with pytest.raises(ValueError):
        assert get_date(text) == date_expect

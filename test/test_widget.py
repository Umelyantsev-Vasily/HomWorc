from src.widget import mask_account_card,get_date
import pytest

@pytest.mark.parametrize("num, expected",[
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 92** **** 6361"),
    ("Счет 73654108430135874305","Счет **4305"),
    ("MasterCard 7000792289606361", "MasterCard 7000 92** **** 6361"),
])

def test_mask_account_card(num, expected):
    assert mask_account_card(num) == expected


@pytest.mark.parametrize("x, title_expected",[
    ("Visa", ValueError ),
    ("700079228960",ValueError),
    ("",ValueError),
    ("#%*_??><", ValueError),
    ("123456789012345678900985",ValueError),
    ("MasterCard", ValueError),
    ("1234567890", ValueError)
])

def test_mask_account_card_error(x, title_expected):
    with pytest.raises(ValueError):
        assert mask_account_card(x) == title_expected


@pytest.mark.parametrize("x,date_expected",[
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2042-05-11T02:26:18.671407", "11.05.2042"),
    ("сегодня/2020/02/20","20.02.2020"),
    ("Сегодня 2023-10-01", "01.10.2023")
])

def test_get_date(x, date_expected):
    assert get_date(x) == date_expected


@pytest.mark.parametrize("text, date_expect",[
    ("data", ValueError ),
    ("", ValueError),
])

def test_get_date_error(text, date_expect):
    with pytest.raises(ValueError):
        assert get_date(text) == date_expect


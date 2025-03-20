from src.widget import mask_account_card
import pytest

@pytest.mark.parametrize("num, expected",[
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 92** **** 6361"),
    ("Счет 73654108430135874305","Счет **4305"),

])

def test_mask_account_card(num, expected):
    assert mask_account_card(num) == expected


@pytest.mark.parametrize("x, title_expected",[
    ("Visa", ValueError ),
    ("700079228960",ValueError),
    ("",ValueError),
    ("#%*_??><", ValueError),
    ("123456789012345678900985",ValueError)
])

def test_mask_account_card_error(x, title_expected):
    with pytest.raises(ValueError):
        assert mask_account_card(x) == title_expected
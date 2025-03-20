import pytest

from src.masks import get_mask_account


def test_get_mask_account_mask(mask_account_mask):
    assert get_mask_account(mask_account_mask) == "**7890"



@pytest.mark.parametrize("x, expected",[
    ("1252156", ValueError),
    ("fgsagh", ValueError),
    ("123456789012345678900", ValueError),
    ("", ValueError)
])
def test_get_mask_account_len(x,expected):
    with pytest.raises(ValueError):
        assert get_mask_account(x) == expected










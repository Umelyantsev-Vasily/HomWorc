import pytest


@pytest.fixture
def mask_account_mask():
    return "12345678901234567890"

@pytest.fixture
def mask_get_mask():
    return "Visa Platinum 7000 92** **** 6361"

@pytest.fixture
def by_state_list():
    return [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

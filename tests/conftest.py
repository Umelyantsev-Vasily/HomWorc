import pytest


# Файл masks.py
@pytest.fixture
def mask_card() -> str:
    return "1234123456785678"


@pytest.fixture
def mask_card_mask() -> str:
    return "1234 23** **** 5678"


# Фунуция: get_mask_account
@pytest.fixture
def mask_account_mask() -> str:
    return "73654108430135874305"


@pytest.fixture
def mask_account_mask_return() -> str:
    return "**4305"


# Файл: widget.py
@pytest.fixture
def mask_account_mask_widget() -> str:
    return "Счет 73654108430135874305"


# Файл widget.py
@pytest.fixture
def mask_get_mask() -> str:
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def mask_get_mask_return() -> str:
    return "Visa Platinum 7000 92** **** 6361"


@pytest.fixture
def mask_account_card_account() -> str:
    return "Счет 73654108430135874305"


@pytest.fixture
def mask_account_card_account_return() -> str:
    return "Счет **4305"


# Функция: get_date
@pytest.fixture
def get_date_str() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def get_date_return() -> str:
    return "11.03.2024"


# Файл: processing.py
@pytest.fixture
def state_list_info() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def by_state_list() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def by_state_test_list() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def by_state_list_2() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

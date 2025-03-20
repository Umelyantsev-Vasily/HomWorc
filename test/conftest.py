import pytest


@pytest.fixture
def number_card():
    return "1234567812345678"

@pytest.fixture
def number_count():
    return "12345678912345678"

@pytest.fixture
def str_card():
    return "card"

@pytest.fixture
def mask_account_mask():
    return "12345678901234567890"


@pytest.fixture
def len_account():
    return "123456789012345678901"


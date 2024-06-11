import pytest


@pytest.fixture
def card_number():
    return "7000 79** **** 6361"


@pytest.fixture
def account_number():
    return "**4305"


@pytest.fixture
def date_for_test():
    return "11-07-2018"

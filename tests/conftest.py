import pytest

from src.generators import card_number_generator


@pytest.fixture
def card_number():
    return "7000 79** **** 6361"


@pytest.fixture
def account_number():
    return "**4305"


@pytest.fixture
def date_for_test():
    return "11-07-2018"


DICT_1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


@pytest.fixture
def dict_fixture_1():
    return DICT_1.copy()


DICT_2 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


@pytest.fixture
def dict_fixture_2():
    return DICT_2.copy()


DICT_3 = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.fixture
def dict_fixture_3():
    return DICT_3.copy()


DICT_4 = [939719570, 142264268, 895315941]


@pytest.fixture
def dict_fixture_4():
    return DICT_4.copy()


@pytest.fixture
def card_generator_fixture():
    return card_number_generator(1, 8)

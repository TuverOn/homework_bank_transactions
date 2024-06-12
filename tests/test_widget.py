import pytest

from src.widget import get_data, mask_account_card


def test_get_data_1(date_for_test):
    assert get_data("2018-07-11T02:26:18.671407") == date_for_test
    with pytest.raises(ValueError):
        get_data("2018-07-11T02")


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2019-07-03T18:35:29.512364", "03-07-2019"),
        ("2018-06-30T02:08:58.425572", "30-06-2018"),
        ("2018-09-12T21:27:25.241689", "12-09-2018"),
    ],
)
def test_get_data_2(value, expected):
    assert get_data(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected

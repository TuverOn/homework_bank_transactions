import pytest

from src.masks import mask_card, mask_account


def test_mask_card(card_number):
    assert mask_card("7000792289606361") == card_number


def test_mask_account(account_number):
    assert mask_account("73654108430135874305") == account_number
    with pytest.raises(TypeError):
        mask_account(73654108430135874305)


@pytest.mark.parametrize("value, expected", [
    ("1596837868705199", "1596 83** **** 5199"),
    ("7158300734726758", "7158 30** **** 6758"),
    ("6831982476737658", "6831 98** **** 7658"),
])
def test_mask_card(value, expected):
    assert mask_card(value) == expected

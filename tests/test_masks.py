import pytest

from src.masks import mask_account, mask_card


def test_mask_card_1(card_number):
    assert mask_card("7000792289606361") == card_number


def test_mask_account(account_number):
    assert mask_account("73654108430135874305") == account_number
    with pytest.raises(TypeError):
        mask_account(73654108430135874305)


@pytest.mark.parametrize(
    "value, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
    ],
)
def test_mask_card_2(value, expected):
    assert mask_card(value) == expected

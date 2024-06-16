from src.generators import (filter_by_currency, transaction_descriptions,
                            transactions)


def test_transaction_descriptions():
    descriptions = transaction_descriptions(transactions)
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

    for expected in expected_descriptions:
        assert next(descriptions) == expected


def test_filter_by_currency():
    usd_transactions = filter_by_currency(transactions, "USD")
    expected_result = [939719570, 142264268, 895315941]
    for expected in expected_result:
        assert next(usd_transactions)["id"] == expected

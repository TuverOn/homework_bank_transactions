from src.generators import filter_by_currency, transaction_descriptions, transactions


def test_transaction_descriptions(dict_fixture_3):
    descriptions = transaction_descriptions(transactions)

    for expected in dict_fixture_3:
        assert next(descriptions) == expected


def test_filter_by_currency(dict_fixture_4):
    usd_transactions = filter_by_currency(transactions, "USD")
    for expected in dict_fixture_4:
        assert next(usd_transactions)["id"] == expected


def test_card_number_generator(card_generator_fixture):
    expected_output = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
        "0000 0000 0000 0006",
        "0000 0000 0000 0007",
        "0000 0000 0000 0008",
    ]

    for expected, actual in zip(expected_output, card_generator_fixture):
        assert expected == actual

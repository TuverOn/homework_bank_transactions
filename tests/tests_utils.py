from src.utils import get_transactions_dictionary, return_transaction_amount


def test_get_transactions_dictionary(get_path):
    assert get_transactions_dictionary(get_path)[1] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_get_transactions_dictionary(get_wrong_path):
    assert get_transactions_dictionary(get_wrong_path) == []


def test_get_transactions_dictionary(get_bad_file):
    assert get_transactions_dictionary(get_bad_file) == []


def test_return_transaction_amount(transactions, rub_transaction_number):
    assert return_transaction_amount(transactions, rub_transaction_number) == 31957.58

import json

from src.external_api import convert_to_rub


def get_transactions_dictionary(path):
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    try:
        with open(path, "r") as operations:
            try:
                transactions_data = json.load(operations)
                return transactions_data
            except json.JSONDecodeError:
                transactions_data = []
                return transactions_data
    except FileNotFoundError:
        transactions_data = []
        return transactions_data


def return_transaction_amount(transactions, transaction_id):
    """Функция принимает транзакцию и возвращает сумму транзакции в рублях, если не в рублях, конвертирует в рубли с
    помошью API"""

    for transaction in transactions:
        if transaction["id"] == transaction_id:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                return transaction["operationAmount"]["amount"]
            else:
                not_rub_amount = transaction["operationAmount"]["amount"]
                currency = transaction["operationAmount"]["currency"]["code"]
                rub_amount = convert_to_rub(not_rub_amount, currency)
                return round(rub_amount, 2)


if __name__ == "__main__":
    transactions = get_transactions_dictionary("../data/operations.json")
    print(return_transaction_amount(transactions, 441945886))

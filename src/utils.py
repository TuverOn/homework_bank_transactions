import json
import logging

from src.external_api import convert_to_rub

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/utils.log",
    filemode="w",
)

logger = logging.getLogger("utils")


def get_transactions_dictionary(path):
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    logger.info("Start.get_transactions_dictionary")
    try:
        logger.info("Getting transaction list starts")
        with open(path, "r") as operations:
            try:
                logger.info("Transactions list ready")
                transactions_data = json.load(operations)
                return transactions_data
            except json.JSONDecodeError:
                logger.error("Decode error")
                transactions_data = []
                return transactions_data
    except FileNotFoundError:
        logger.error("File was not found")
        transactions_data = []
        return transactions_data


def return_transaction_amount(transactions, transaction_id):
    """Функция принимает транзакцию и возвращает сумму транзакции в рублях, если не в рублях, конвертирует в рубли с
    помошью API"""

    logger.info("Start.return_transaction_amount")
    logger.info("Getting transaction amount starts")
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            rub_amount = convert_to_rub(transaction)
            logger.info("Transaction amount in RUB")
            return round(rub_amount, 2)


if __name__ == "__main__":
    transactions = get_transactions_dictionary("../data/operations.json")
    print(return_transaction_amount(transactions, 464419177))

import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction):
    """Функция принимает сумму транзакции в другой валюте и возвращает сумму транзакции в рублях"""

    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return float(amount)
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)
        json_result = response.text
        rub_amount = json.loads(json_result)["result"]
        return float(rub_amount)

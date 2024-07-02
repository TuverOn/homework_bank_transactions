import json
import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")


def convert_to_rub(amount, currency):
    """Функция принимает сумму транзакции в другой валюте и возвращает сумму транзакции в рублях"""

    if currency == "USD":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"
        headers = {"apikey": API_KEY}
        responce = requests.get(url, headers=headers)
        json_result = responce.text
        rub_amount = json.loads(json_result)["result"]
        return rub_amount
    elif currency == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount}"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)
        json_result = response.text
        rub_amount = json.loads(json_result)["result"]
        return rub_amount

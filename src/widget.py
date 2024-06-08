import datetime

from src.masks import mask_account, mask_card


def mask_account_card(coming_str: str) -> str:
    """Функция, которая возвращает исходную строку с замаскированными данными карты или счета"""

    new_coming_str = coming_str.split()
    mask_number = ""
    for i in new_coming_str:
        if i.isalpha():
            mask_number += i + " "
        elif i.isdigit() and len(i) == 16:
            mask_number += mask_card(i)
        elif i.isdigit() and len(i) == 20:
            mask_number += mask_account(i)
    return mask_number


if __name__ == "__main__":
    result_1 = mask_account_card("Visa Platinum 7000792289606361")
    result_2 = mask_account_card("Счет 73654108430135874305")
    print(result_1)
    print(result_2)


def get_data(data: str) -> str:
    """Функция, которая меняет формат времени"""

    time = datetime.datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    new_format = time.strftime("%d-%m-%Y")
    return new_format

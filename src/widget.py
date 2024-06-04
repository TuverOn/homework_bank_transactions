from masks import mask_account, mask_card


def mask_type(coming_str: str) -> str:
    """Функция, которая возвращает исходную строку с замаскированными данными карты или счета"""

    new_coming_str = coming_str.split()
    mask_number = ""
    for i in new_coming_str:
        if i.isalpha():
            mask_number += i + " "
        elif i.isdigit() and len(i) == 16:
            mask_number += mask_card(i) + " "
        elif i.isdigit() and len(i) == 20:
            mask_number += mask_account(i) + " "
    return mask_number


def date_conv(date: str) -> str:
    """Функция преобразует дату"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"

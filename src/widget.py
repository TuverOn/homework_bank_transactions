from masks import mask_card
from masks import mask_account

def mask_type(coming_str: str) -> str:
    """Функция, которая возвращает исходную строку с замаскированными данными карты или счета"""

    new_coming_str = coming_str.split()
    mask_number = ''
    for i in new_coming_str:
        if i.isalpha():
            mask_number += i + ' '
        elif i.isdigit() and len(i) == 16:
            mask_number += mask_card(i) + ' '
        elif i.isdigit() and len(i) == 20:
            mask_number += mask_account(i) + ' '
    return mask_number

if __name__ == '__main__':
    result = mask_type('Счет 35383033474447895560')
    print(result)


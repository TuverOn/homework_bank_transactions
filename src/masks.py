def mask_card(card_number: str) -> str:
    """Возвращает замаскированный номер карты в виде строки"""

    return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"


def mask_account(acc_number: str) -> str:
    """Возвращает замаскированный номер счета в виде строки"""

    return f"{"*" * 2}{acc_number[-4:]}"

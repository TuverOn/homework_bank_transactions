import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/masks.log",
    filemode="w",
)

logger = logging.getLogger("masks")


def mask_card(card_number: str) -> str:
    """Возвращает замаскированный номер карты в виде строки"""

    logging.info("Start.mask_card")
    new_card_number = (
        f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"
    )
    # return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"
    logging.info("Return of mask card number")
    logging.info("Stop")
    return new_card_number


def mask_account(acc_number: str) -> str:
    """Возвращает замаскированный номер счета в виде строки"""

    logging.info("Start.mask_account")
    new_acc_number = f"{"*" * 2}{acc_number[-4:]}"
    logging.info("Return of mask account number")
    logging.info("Stop")
    return new_acc_number


if __name__ == "__main__":
    print(mask_card("1324321343213213"))
    print(mask_account("75645867564756664756"))

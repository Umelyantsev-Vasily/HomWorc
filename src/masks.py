import logging
from typing import Union

card_user = "1234123456785678"
account_numbers = "73654108430135874305"
# Создаем лог
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8")
console_handler = logging.StreamHandler()
file_formater = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_user: Union[str]) -> Union[str]:
    """Функция которая маскирует номер карты"""
    logger.info(f"Получаем данные карты")
    if len(str(card_user)) != 16 or not str(card_user.isdigit()):
        logger.error(f"Неправельный ввод: {card_user}")
        raise ValueError(f"Некорректный ввод")

    string_card = str(card_user)
    title = f"{string_card[:4]} {string_card[5:7]}** **** {string_card[-4:]}"
    logger.info(f"Возращаем маску {title}")
    return title


def get_mask_account(account_numbers: Union[str]) -> Union[str]:
    """Функция которая принимает номер счета и возращает маску"""
    logger.info(f"Получаем данные счета")
    if len(str(account_numbers)) != 20 or not str(account_numbers.isdigit()):
        logger.error(f"Неправельный номер счета!")
        raise ValueError("Не правильный ввод!")

    str_account_numbers = str(account_numbers)
    title = f"**{str_account_numbers[-4:]}"
    logger.info(f"Возращаем маску счета {title}")
    return title


print(get_mask_card_number(card_user))
print(get_mask_account(account_numbers))

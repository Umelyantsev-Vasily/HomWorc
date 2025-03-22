from typing import Union

# card_user = "1234123456785678"
# account_numbers = "73654108430135874305"
""" Получаем данные от пользователя"""


def get_mask_card_number(card_user: Union[str]) -> Union[str]:
    """Функция которая маскирует номер карты"""
    if len(str(card_user)) != 16 or not str(card_user.isdigit()):
        raise ValueError("Не правельный ввод!")


    string_card = str(card_user)
    return f"{string_card[:4]} {string_card[5:7]}** **** {string_card[-4:]}"


def get_mask_account(account_numbers: Union[str]) -> Union[str]:
    """Функция которая принимает номер счета и возращает маску"""
    if len(str(account_numbers)) != 20 or not str(account_numbers.isdigit()):
        raise ValueError("Не правильный ввод!")

    str_account_numbers = str(account_numbers)
    return f"**{str_account_numbers[-4:]}"


# print(get_mask_card_number(card_user))
# print(get_mask_account(account_numbers))

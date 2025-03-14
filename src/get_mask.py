from typing import Union

# card_user = input("Введите номер карты: ")
# account_numbers = input("Введите номер счета: ")
""" Получаем данные от пользователя"""


def get_mask_card_number(card_user: Union[str]) -> Union[str]:
    """Функция которая маскирует номер карты"""
    if len(str(card_user)) != 16 or not str(card_user.isdigit()):
        return "Не правельный ввод!"

    string_card = str(card_user)
    return f"{string_card[:4]} {string_card[4:7]}** **** {string_card[-4:]}"


def get_mask_account(account_numbers: Union[str]) -> Union[str]:
    """Функция которая принимает номер счета и возращает маску"""
    if len(str(account_numbers)) != 20 or not str(account_numbers.isdigit()):
        return "Не правильный ввод!"

    str_account_numbers = str(account_numbers)
    return f"**{str_account_numbers[-4:]}"


# print(get_mask_card_number(card_user))
# print(get_mask_account(account_numbers))

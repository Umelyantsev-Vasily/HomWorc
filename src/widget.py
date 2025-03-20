from masks import get_mask_account, get_mask_card_number


def mask_account_card(number_name: str) -> tuple[str, str]:
    """Функция которая маскирует карту и счет"""
    title_num = ""
    title_name = ""
    for element in number_name:
        if element.isdigit():  # Проверяем есть ли в строке числа
            title_num += element  # Добавляем числа в переменную номер
        else:
            title_name += element  # Если это не числа то добавляем строку во вторую переменную имя
    return title_name, title_num


test = "Visa Platinum 7000792289606361"
# test_2 = "Счет 73654108430135874305"
name, num = mask_account_card(test)
if len(num) <= 16:  # Проверяем колличество цифр в строке
    new_mask = get_mask_card_number(num)  # Применяем функцию для маски карты
else:
    new_mask = get_mask_account(num)  # Применяем функцию для маски счета
print(f"{name}{new_mask}")


def get_date(input_str: str) -> str:
    """Функция которая преобразует дату и выводит"""
    data_title = ""
    for items in input_str:
        if items.isdigit():
            data_title += items
    return f"{data_title[6:8]}.{data_title[4:6]}.{data_title[0:4]}"


test_3 = "2024-03-11T02:26:18.671407"
print(get_date(test_3))

from idlelib.replace import replace

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_name: str) -> str:
    """Функция которая маскирует карту и счет"""
    title_num = ""
    title_name = ""
    for element in number_name:
        if element.isdigit():  # Проверяем есть ли в строке числа
            title_num += element  # Добавляем числа в переменную номер
        elif element.isalpha() or element.isspace():
            title_name += element  # Если этo буквы то добавляем строку во вторую переменную имя
    strip_title_name = title_name.strip()
    if len(title_num) == 16:  # Проверяем колличество цифр в строке
        title_nums = get_mask_card_number(title_num)
    elif len(title_num) == 20:
        title_nums = get_mask_account(title_num)
    else:
        raise ValueError("Неправильный ввод")
    title_mask = str(title_name) + str(title_nums)
    return title_mask


# test = "Visa Platinum 7000792289606361"
test_2 = "Счет 73654108430135874305"
print(mask_account_card(test_2))
#name, num = mask_account_card(test)
#if len(num) == 16:  # Проверяем колличество цифр в строке
#    new_mask = get_mask_card_number(num)
#elif len(num) == 20:
#   new_mask = get_mask_account(num)
#else:
#    raise ValueError("Неправильный ввод")
# print(f"{name}{new_mask}")


def get_date(input_str: str) -> str:
    """Функция, которая преобразует дату и выводит в формате DD.MM.YYYY"""
    data_title = ""
    if input_str[:10].isalpha():
        raise ValueError("Введите цыфровое значение ")
    new_data = input_str[:10]
    replace_new_data = new_data.replace("-","")

    # Проверка, что у нас есть достаточное количество цифр, и они не буквы
    if not replace_new_data.isdigit() or len(replace_new_data) < 8:
        raise ValueError("Не корректный ввод")
    # Форматирование даты
    data_title = f"{replace_new_data[6:]}.{replace_new_data[4:6]}.{replace_new_data[:4]}"
    return data_title


# test_3 = "2024-03-11T02:26:18.671407"
# test7 = "325326457687970"
# print(get_date(test_3))


#def get_date(input_str: str) -> str:
#    """Функция которая преобразует дату и выводит"""
#    data_title = ""
#    new_data = ""
#    for items in input_str:
#        if items.isdigit():
#            data_title += items
#    new_data = data_title[:8]
#   if len(new_data) != 8 or not new_data.isdigit():
#        raise ValueError("НЕправельный ввод")
#    return f"{data_title[6:8]}.{data_title[4:6]}.{data_title[0:4]}"
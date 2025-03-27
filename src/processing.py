from typing import Dict, List


def filter_by_state(list_dictionaries: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    """
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.

    :param list_dictionaries: Список словарей, которые нужно отфильтровать.
    :param state: Значение ключа "state", по которому производится фильтрация. По умолчанию "EXECUTED".
    :return: Новый список словарей, отфильтрованных по значению ключа "state".
    :raises ValueError: Если передан пустой список словарей или если ключ "state" отсутствует или пуст.
    """
    if not list_dictionaries:
        raise ValueError("Нет словарей")

    nev_list_dictionaries = []
    for transactions in list_dictionaries:
        if not isinstance(transactions, dict):
            raise ValueError("Элемент списка не является словарем")
        if transactions.get("state") == state:
            nev_list_dictionaries.append(transactions)
        elif transactions.get("state") == "":
            raise ValueError("Нет текста")
    return nev_list_dictionaries


def sort_by_date(list_dict: List[Dict[str, str]], parameter: bool = True) -> List[Dict[str, str]]:
    """
    Функция возвращает новый список, отсортированный по дате.

    :param list_dict: Список словарей, которые нужно отсортировать.
    :param parameter: Флаг, определяющий порядок сортировки. Если True, сортировка по убыванию, иначе по возрастанию.
    :return: Новый список словарей, отсортированных по дате.
    :raises ValueError: Если дата в словаре некорректна.
    """
    for u in list_dict:
        if not isinstance(u, dict):
            raise ValueError("Элемент списка не является словарем")
        new_date = u.get("date")
        if new_date:
            date_part = new_date[:10]
            replace_new_list = date_part.replace("-", "")
            if not replace_new_list.isdigit():  # Проверяем дату, чтобы состояла из чисел
                raise ValueError("Некорректные данные")
    # Сортируем список
    data = sorted(list_dict, key=lambda x: x["date"], reverse=parameter)
    return data


# Пример использования функций
test = [
    {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(test))
print(sort_by_date(test))

# Делаем проверку второй функции
# test_2 = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]
#
# print(sort_by_date(test_2))

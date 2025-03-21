from typing import Any, Dict, List, Optional


def filter_by_state(list_dictionaries: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""
    nev_list_dictionaries = []
    if list_dictionaries == {}:
        raise ValueError("Нет словарей")
    for transactions in list_dictionaries:
        if transactions.get("state") == state:
            nev_list_dictionaries.append(transactions)
        elif transactions.get("state") == "" or transactions == {}:
            raise ValueError("Нет текста")
    return nev_list_dictionaries


test = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
]
print(filter_by_state(test))


def sort_by_date(list_dict: List[Dict], parameter: Optional[bool] = True) -> List[Dict]:
    """Функция которая возращает  новый список, отсортированный по дате"""
    new_list = []
    for u in list_dict:
        new_date = u.get("date")
        new_list = new_date[:10]
        replace_new_list = new_list.replace("-","")
        if not replace_new_list.isdigit():
            raise ValueError("Некорректные данные")

    data = sorted(list_dict, key=lambda x: x["date"], reverse=parameter)
    return data


# Делаем проверку второй функции
test_2 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(sort_by_date(test_2))

from typing import List, Dict, Any

def filter_by_state(list_dictionaries: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению """
    nev_list_dictionaries = []
    for transactions in list_dictionaries:
        if transactions.get("state") == state:
            nev_list_dictionaries.append(transactions)
    return nev_list_dictionaries


test = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
print(filter_by_state(test))
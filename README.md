# Обучение 
---
Я ученик школы Skypro, учусь писать программу, которая работает с банковскими данными.
---
## Содержание
- [Функции маски ](https://github.com/Umelyantsev-Vasily/HomWorc/blob/feature/homework_10_1/src/get_mask.py)
- [Функции сортировки даты и проверки значения](https://github.com/Umelyantsev-Vasily/HomWorc/blob/feature/homework_10_1/src/processing.py)
---
## Инструменты которые используется в проекте 
- [flake8](https://flake8.pycqa.org/en/latest/)
- [black](https://pypi.org/project/black/)
- [isort](https://pycqa.github.io/isort/)
- [mypy](https://mypy-lang.org/)
## Пример кода:
```
def filter_by_state(list_dictionaries: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""
    nev_list_dictionaries = []
    for transactions in list_dictionaries:
        if transactions.get("state") == state:
            nev_list_dictionaries.append(transactions)
    return nev_list_dictionaries
```

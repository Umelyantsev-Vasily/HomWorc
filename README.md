# Проект "Банковские операции "
---
## Описание
Проект представляет инструменты для работы с транзакциями, фильтрация и сортировка, а также делает маску номера счета/карт.
---
## Установка:
1. Убедитесь ,что у вас установлен Python 3.13 и выше.
2. Установите Poetry:
```
pip instal poetry 
```
3. Клонируйте репозиторий:
```
https://github.com/Umelyantsev-Vasily/HomWorc
```
4. Установите зависимости:
```
pip install -r requirements.txt
```
---
## Использование:
### Основные модули:
- masks.py: Содержит функцию для маскировки карт/счетов.
- get_mask.py: Основной модуль для взаимодействия с пользователем.
- processing.py: Содержит функции для фильтрации и сортировки данных.
---
### Пример использования:
*Функция для фильтрации*
```
from src_.processing import filter_by_state

transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

filter_transactions = filter_by_state(transactions)
print(filter_transactions)

```

*Функция для сортировки*
```
from src_.processing import sort_by_date

transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

filter_transactions = sort_by_date(transactions)
print(filter_transactions)

```
---
*Тестовые данные:*
```
---------- coverage: platform win32, python 3.13.2-final-0 -----------
Name                       Stmts   Miss  Cover
----------------------------------------------
src\__init__.py                0      0   100%
src\masks.py                  12      0   100%
src\processing.py             28      1    96%
src\widget.py                 28      0   100%
tests\__init__.py              0      0   100%
tests\conftest.py             46      1    98%
tests\test_mask.py            17      0   100%
tests\test_processing.py      21      0   100%
tests\test_widget.py          22      0   100%
----------------------------------------------
TOTAL                        174      2    99%

```
---
## Документация:


Дополнительную информацию о структуре проекта и API можно найти в [документации](https://github.com/Umelyantsev-Vasily/HomWorc/edit/main/README.md)

Дополнительную нформацию о тесте можно посмотреть: [tests](file:///C:/Users/tanec/PycharmProjects/HomWorc/htmlcov/function_index.html)
## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).

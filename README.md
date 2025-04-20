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
- generators.py: Содержит Функции генераторы.
- decorator.py: Декорирует функцию.
- utils.py: Содержит функцию которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
- external_api.py: Содержит функция которая принимает на вход транзакцию и возвращает сумму транзакции в рублях.
- external_api.py: Содержит Функцию которая: конвертирует сумму транзакции в рубли.
    Для USD/EUR использует текущий курс через API.
- utils.py: Содержит Функцию которая: загружает транзакции из JSON-файла.
- read_csv_end_xlsx_file.py: Функция которая читает данные из CSV или XLSX файла и возвращает их в виде списка словарей.
- finder_func: Содержит Функцию: которая фильтрует список банковских операций по заданной строке и функцию которая: подсчитывает количество операций в каждой заданной категории
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

*Функция генерации номера*
```
def card_number_generator(start: int = 1, end: int = 9999999999999999) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    Генерирует последовательные номера в заданном диапазоне
    """
    if not 1 <= start <= end <= 9999999999999999:
        raise ValueError("Некорректный диапазон номеров карт")

    for number in range(start, end + 1):
        num_str = f"{number:016d}"  # Форматируем в 16 цифр с ведущими нулями
        yield f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"

    # Генерация первых 5 номеров карт
cards = card_number_generator(1, 5)
for card in cards:
    print(card)
    
# Вывод:
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# 0000 0000 0000 0003
# 0000 0000 0000 0004
# 0000 0000 0000 0005

```
*Функция декоратор*
```
# Лог положительный в файл
@log("log.txt")
def add(a, b):
    return a + b

add(2, 3)  # Запишет в operations.log: "add ok"

# Лог в консоль
@log()  # Без параметра - вывод в консоль
def multiply(x, y):
    return x * y

multiply(3, 4)  # Выведет в консоль: "multiply ok"

```
*Функция которая читает данные из CSV или XLSX*
```
def read_csv_end_xlsx_file(file_path: str, delimiter: str = ";")-> List[dict]:
    """
    Функция которая читает данные из CSV или XLSX файла и возвращает их в виде списка словарей.
    """
    if "csv" in file_path:
        try:
            df = pd.read_csv(file_path, delimiter=delimiter)
            return df.to_dict(orient="records")
        except FileNotFoundError:
            print(f"Ошибка: файл {file_path} не найден!")
            return []
        except Exception as e:
            print(f"Ошибка при чтении CSV: {e}")
            return []
    elif "xlsx" in file_path:
        try:
            df = pd.read_excel(file_path)
            return df.to_dict(orient="records")
        except FileNotFoundError:
            print(f"Ошибка: файл {file_path} не найден!")
            return []
        except Exception as e:
            print(f"Ошибка при чтении XLSX: {e}")
            return []
    else:
        print("Ошибка: неподдерживаемый формат файла (должен быть .csv или .xlsx)")
        return []

```

*Фильтрует список банковских операций по заданной строке*
```
def finder_inf(list_data: List[Dict[str, Any]], input_str: str) -> List[Dict[str, Any]]:
    """Фильтрует список банковских операций по заданной строке"""
    try:
        pattern = re.compile(re.escape(input_str), re.IGNORECASE)  # Экранируем спецсимволы
        filtered_list = []

        for item in list_data:
            # Проверяем все строковые значения в словаре
            for value in item.values():
                if isinstance(value, str) and pattern.search(value):
                    filtered_list.append(item)
                    break
                elif isinstance(value, dict):
                    # Рекурсивно проверяем вложенные словари
                    for sub_value in value.values():
                        if isinstance(sub_value, str) and pattern.search(sub_value):
                            filtered_list.append(item)
                            break

        return filtered_list
    except Exception as e:
        print(f"Ошибка при фильтрации: {e}")
        return []
        
```

---
*Тестовые данные:*
```
Name                                   Stmts   Miss  Cover
----------------------------------------------------------
src\__init__.py                            0      0   100%
src\decorator.py                          44      0   100%
src\external_api.py                       39      0   100%
src\finder_func.py                        30      3    90%
src\generators.py                         33      1    97%
src\masks.py                              29      0   100%
src\processing.py                         26      1    96%
src\read_csv_end_xlsx_file.py             25      6    76%
src\utils.py                              29      0   100%
src\widget.py                             28      0   100%
tests\__init__.py                          0      0   100%
tests\conftest.py                         85      4    95%
tests\test_decorator.py                   26      0   100%
tests\test_exempl_api.py                  35      0   100%
tests\test_finder_func.py                 68      1    99%
tests\test_generators.py                  70      0   100%
tests\test_mask.py                        17      0   100%
tests\test_processing.py                  21      0   100%
tests\test_read_csv_end_xlsx_file.py      51      0   100%
tests\test_utils.py                       51      1    98%
tests\test_widget.py                      22      0   100%
----------------------------------------------------------
TOTAL                                    729     17    98%



```
---
## Документация:


Дополнительную информацию о структуре проекта и API можно найти в [документации](https://github.com/Umelyantsev-Vasily/HomWorc/edit/main/README.md)

Дополнительную нформацию о тесте можно посмотреть: [tests](file:///C:/Users/tanec/PycharmProjects/HomWorc/htmlcov/function_index.html)

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).

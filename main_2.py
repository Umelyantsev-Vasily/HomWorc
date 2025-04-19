from config import PATH_JSON, PATH_TO_EXCEL, PATH_TO_CSV
from src.external_api import get_amount_in_rub
from src.utils import load_transactions
from src.read_csv_end_xlsx_file import read_csv_end_xlsx_file
from src.finder_func import finder_inf
from src.processing import sort_by_date
from src.processing import filter_by_state
from pprint import pprint

def main():
    print("""
    Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """)


    while True:
        file_type = str(input().lower().strip())
        if  file_type == '1':
            print('Вы выбрали JSON-файла')
            break
        elif file_type == '2':
            print('Вы выбрали CSV-файла')
            break
        elif file_type == '3':
            print('Вы выбрали XLSX-файла')
            break
        else:
            print('Введите корректное число!')


    while True:
        print('Введите статус, по которому необходимо выполнить фильтрацию. '
              'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')

        state = input().lower().strip()

        statuses = ['EXECUTED','CANCELED', 'PENDING']

        if state.upper() in statuses:
            break
        else:
            print(f'Статус операции не доступен {state}')


    while True:
        print('Отсортировать операции по дате? Да/Нет')

        sorted_data = input().lower().strip()

        if sorted_data in ['да', 'нет']:
            break

    while True:
        print("""Отсортировать -
              1: по возрастанию,
              2: по убыванию
              """)

        sorted_by_data = input().lower().strip()

        if sorted_by_data in ['1', '2']:
            break

    while True:
        print('Выводить только рублевые тразакции? Да/Нет')

        rub_sorted = input().lower().strip()

        if rub_sorted in ['да', 'нет']:
            break


    while True:
        print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')

        word_sort = input().lower().strip()

        if word_sort in 'нет':
            break
        elif word_sort in 'да':
            print('Напишите слово для фильтрации:')

            word = input().lower().strip()

            break

    while True:
        if file_type == '1':
            file = load_transactions(PATH_JSON)
            break
        elif file_type == '2':
            file = read_csv_end_xlsx_file(PATH_TO_CSV)
            break
        elif file_type == '3':
            file = read_csv_end_xlsx_file(PATH_TO_EXCEL)
            break
        else:
            print('Введите число от 1-3')


    file = filter_by_state(file, state)

    if sorted_data == 'да':
        if sorted_by_data == '2':
            sort_data_new = sort_by_date(file)

            pprint(sort_data_new)
        else:
            sort_data_new = sort_by_date(file, False)
            pprint(sort_data_new)

    print('Вывод конечного результата ')
    pprint(sort_data_new)




if __name__ == '__main__':
    main()
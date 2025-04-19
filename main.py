from config import PATH_JSON, PATH_TO_EXCEL, PATH_TO_CSV
from src.external_api import get_amount_in_rub
from src.utils import load_transactions
from src.read_csv_end_xlsx_file import read_csv_end_xlsx_file
from src.finder_func import finder_inf
from src.processing import sort_by_date

def user_inp()-> list[dict]:
    print("""
Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
""")

    while True:
        user = str(input().lower().strip())
        if user == '1':
            result = load_transactions(PATH_JSON)
            return result
        elif user == '2':
            result = read_csv_end_xlsx_file(PATH_TO_CSV)
            return result
        elif user == '3':
            result = read_csv_end_xlsx_file(PATH_TO_EXCEL)
            print('работа прет')
            return result
        else:
            print('Не правельный ввод!')
            continue


def filter_status(transaction):
    print('Введите статус, по которому необходимо выполнить фильтрацию. '
          'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')

    transaction_exec = 'EXECUTED'
    transaction_can = 'CANCELED'
    transaction_pen = 'PENDING'

    while True:
        user = str(input().lower().strip())

        if user == transaction_exec.lower():
            print(f'Операции отфильтрованы по статусу {transaction_exec}')
            result = finder_inf(transaction_exec)
            return result
        elif user == transaction_can.lower():
            print(f'Операции отфильтрованы по статусу {transaction_can}')
            result = finder_inf(transaction_can)
            return result
        elif user == transaction_pen.lower():
            print(f'Операции отфильтрованы по статусу {transaction_pen}')
            result = finder_inf(transaction_pen)
            return result
        else:
            print(f'Статус операции {user} недоступен.')
            continue


def sorted_transaction(list_filter):
    print('Отсортировать операции по дате? Да/Нет')
    assert_yes = 'Да'
    assert_no = 'Нет'

    user = str(input().lower().strip())

    if user == assert_yes.lower():
        print('Отсортировать по возрастанию или по убыванию? ')

        user = str(input().lower().strip())

        if user == assert_yes.lower():
            result = sort_by_date(list_filter)

        elif user == assert_no.lower():
            pass





# if __name__ == "__main__":
    # transactions = load_transactions(PATH_JSON)
    #
    # print(get_amount_in_rub(transactions[1]))
    # print(read_csv_end_xlsx_file(PATH_TO_EXCEL))
    # print(read_csv_end_xlsx_file(PATH_TO_CSV))

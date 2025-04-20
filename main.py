from config import PATH_JSON, PATH_TO_EXCEL, PATH_TO_CSV
from src.utils import load_transactions
from src.read_csv_end_xlsx_file import read_csv_end_xlsx_file
from src.processing import sort_by_date, filter_by_state
from src.finder_func import finder_inf, coun_description
from src.widget import mask_account_card, get_date


def format_transaction(transaction):
    """Форматирует транзакцию для вывода в заданном формате"""
    try:
        # Получаем отформатированную дату
        date = get_date(transaction.get('date', ''))

        # Получаем описание транзакции
        description = transaction.get('description', 'Описание отсутствует')

        # Обрабатываем отправителя
        from_account = ''
        if 'from' in transaction:
            from_value = str(transaction['from'])
            from_account = mask_account_card(from_value)

        # Обрабатываем получателя
        to_value = str(transaction.get('to', 'Получатель не указан'))
        to_account = mask_account_card(to_value)

        # Извлекаем и форматируем сумму
        operation_amount = transaction.get('operationAmount', {})
        amount = operation_amount.get('amount', '0') if isinstance(operation_amount, dict) else '0'
        currency = operation_amount.get('currency', {}).get('code', '') if isinstance(operation_amount, dict) else ''

        # Преобразуем сумму к числовому формату
        try:
            # Убираем лишние нули после точки, если они есть
            amount_float = float(amount)
            formatted_amount = f"{amount_float:,.2f}".replace(',', ' ').replace('.00', '')
        except (ValueError, TypeError):
            formatted_amount = amount

        # Собираем результат в нужном формате
        result = f"{date} {description}\n"
        if from_account:
            result += f"{from_account} -> "
        result += f"{to_account}\n"
        result += f"Сумма: {formatted_amount} {currency}"

        return result

    except Exception as e:
        print(f"Ошибка форматирования транзакции: {e}")
        return f"Не удалось отформатировать транзакцию: {transaction}"


def show_statistics(transactions):
    """Выводит статистику по операциям, используя coun_description"""
    common_categories = [
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод со счета на счет",
        "Открытие вклада",
        "Пополнение счета"
    ]

    stats = coun_description(transactions, common_categories)
    print("\nСтатистика операций по категориям:")
    for category, count in stats.items():
        print(f"{category}: {count}")


def main():
    print("""
    Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """)

    # Выбор файла
    while True:
        file_type = input("Ваш выбор (1-3): ").strip()
        if file_type == '1':
            print("\nДля обработки выбран JSON-файл.")
            break
        elif file_type == '2':
            print("\nДля обработки выбран CSV-файл.")
            break
        elif file_type == '3':
            print("\nДля обработки выбран XLSX-файл.")
            break
        else:
            print("Пожалуйста, введите число от 1 до 3")

    # Загрузка данных
    transactions = []

    try:
        if file_type == '1':
            transactions = load_transactions(PATH_JSON)
        elif file_type == '2':
            transactions = read_csv_end_xlsx_file(PATH_TO_CSV)
        elif file_type == '3':
            transactions = read_csv_end_xlsx_file(PATH_TO_EXCEL)
    except Exception as e:
        print(f"\nОшибка при загрузке файла: {e}")
        transactions = []  # Явно указываем пустой список

    # Фильтрация по статусу
    while True:
        print('\nВведите статус, по которому необходимо выполнить фильтрацию.')
        print('Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
        state = input("Ваш выбор: ").upper().strip()

        if state in ['EXECUTED', 'CANCELED', 'PENDING']:
            transactions = filter_by_state(transactions, state)
            print(f"\nОперации отфильтрованы по статусу '{state}'")
            break
        else:
            print(f'\nСтатус операции "{state}" недоступен')

    # Сортировка по дате
    while True:
        sort_choice = input("\nОтсортировать операции по дате? (Да/Нет): ").lower().strip()
        if sort_choice in ['да', 'нет']:
            break

    if sort_choice == 'да':
        while True:
            sort_order = input("Отсортировать по возрастанию или по убыванию? ").lower().strip()
            if sort_order in ['по возрастанию', 'по убыванию']:
                reverse = (sort_order == 'по убыванию')
                transactions = sort_by_date(transactions, True)
                break

        # Фильтрация по ключевому слову
        while True:
            filter_word = input("\nОтфильтровать список транзакций по слову в описании? (Да/Нет): ").lower().strip()
            if filter_word in ['да', 'нет']:
                break

        if filter_word == 'да':
            keyword = input("Введите слово для фильтрации: ").strip()
            transactions = finder_inf(transactions, keyword)

        else:
            print('Не корректные данные')


    # Вывод результатов
    print("\nРаспечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(transactions)}\n")

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        for transaction in transactions:
            print(format_transaction(transaction))
            print('-' * 50)

    if transactions:  # Только если есть транзакции
        show_statistics(transactions)


if __name__ == '__main__':
    main()
from src.external_api import get_amount_in_rub
from src.utils import load_transactions
from config import PATH_JSON
from config import PATH_TO_EXCEL, PATH_TO_CSV
from src.read_csv_end_xlsx_file import read_csv_end_xlsx_file


if __name__ == "__main__":
    transactions = load_transactions(PATH_JSON)

    # print(get_amount_in_rub(transactions[1]))
    print(read_csv_end_xlsx_file(PATH_TO_EXCEL))
    print(read_csv_end_xlsx_file(PATH_TO_CSV))

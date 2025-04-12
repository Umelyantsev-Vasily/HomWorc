from src.external_api import get_amount_in_rub
from src.utils import load_transactions
from config import PATH_JSON


if __name__ == "__main__":
    transactions = load_transactions(PATH_JSON)

    print(get_amount_in_rub(transactions[1]))

import json
import logging
import os
from typing import Dict, List

# Получаем путь к текущему скрипту
script_dir = os.path.dirname(os.path.abspath(__file__))


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8")
console_handler = logging.StreamHandler()
file_formater = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_transactions(file_path: str) -> List[Dict]:
    """
    Загружает транзакции из JSON-файла.
    """
    logger.info("Получаем данные из файл")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            # Проверяем, что data — это список
            logger.info("Проверяем, что data — это список")
            if isinstance(data, list):
                return data
            return []

    except FileNotFoundError as ex:
        logger.error(f"Файл не найден по пути: {file_path}, ошибка: {ex}")
        print("Файл не найден")
        return []
    except json.JSONDecodeError as ex:
        logger.error(f"Ошибка при декодировании JSON из файла: {file_path}, ошибка: {ex}")
        print("Некорректный JSON")
        return []

import pandas as pd
from typing import List, Dict


def read_csv_end_xlsx_file(file_path: str, delimiter: str = ";")-> List[dict]:
    """
    Читает данные из CSV или XLSX файла и возвращает их в виде списка словарей.

    Args:
        file_path (str): Путь к файлу (CSV или XLSX).
        delimiter (str): Разделитель для CSV (по умолчанию ";").

    Returns:
        List[Dict[str, Any]]: Список словарей с данными из файла.
                             В случае ошибки возвращает пустой список.
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
from typing import List

import pandas as pd


def read_csv_end_xlsx_file(file_path: str, delimiter: str = ";") -> List[dict]:
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

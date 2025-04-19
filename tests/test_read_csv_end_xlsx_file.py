import os
import unittest

import pandas as pd

from src.read_csv_end_xlsx_file import read_csv_end_xlsx_file


class TestReadCsvEndXlsxFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Создаем тестовые файлы перед запуском тестов."""
        # Тестовые данные
        cls.test_data = [
            {"id": 1, "name": "Alice", "age": 25},
            {"id": 2, "name": "Bob", "age": 30},
            {"id": 3, "name": "Charlie", "age": 35},
        ]

        # Создаем тестовый CSV файл
        cls.csv_file = "test_file.csv"
        pd.DataFrame(cls.test_data).to_csv(cls.csv_file, sep=";", index=False)

        # Создаем тестовый XLSX файл
        cls.xlsx_file = "test_file.xlsx"
        pd.DataFrame(cls.test_data).to_excel(cls.xlsx_file, index=False)

        # Создаем пустой файл с неподдерживаемым форматом
        cls.unsupported_file = "test_file.txt"
        with open(cls.unsupported_file, "w") as f:
            f.write("This is a text file")

        # Создаем несуществующий файл
        cls.non_existent_file = "non_existent_file.csv"

    @classmethod
    def tearDownClass(cls):
        """Удаляем тестовые файлы после выполнения тестов."""
        if os.path.exists(cls.csv_file):
            os.remove(cls.csv_file)
        if os.path.exists(cls.xlsx_file):
            os.remove(cls.xlsx_file)
        if os.path.exists(cls.unsupported_file):
            os.remove(cls.unsupported_file)

    def test_read_csv_file(self):
        """Тест чтения CSV файла."""
        result = read_csv_end_xlsx_file(self.csv_file, delimiter=";")
        self.assertEqual(result, self.test_data)

    def test_read_xlsx_file(self):
        """Тест чтения XLSX файла."""
        result = read_csv_end_xlsx_file(self.xlsx_file)
        self.assertEqual(result, self.test_data)

    def test_read_csv_with_wrong_delimiter(self):
        """Тест чтения CSV с неправильным разделителем."""
        result = read_csv_end_xlsx_file(self.csv_file, delimiter=",")
        # Должен вернуть пустой список или список с некорректными данными
        self.assertNotEqual(result, self.test_data)

    def test_read_nonexistent_file(self):
        """Тест чтения несуществующего файла."""
        result = read_csv_end_xlsx_file(self.non_existent_file)
        self.assertEqual(result, [])

    def test_unsupported_file_format(self):
        """Тест чтения файла неподдерживаемого формата."""
        result = read_csv_end_xlsx_file(self.unsupported_file)
        self.assertEqual(result, [])

    def test_empty_csv_file(self):
        """Тест чтения пустого CSV файла."""
        empty_csv = "empty_test.csv"
        pd.DataFrame().to_csv(empty_csv, sep=";", index=False)
        result = read_csv_end_xlsx_file(empty_csv, delimiter=";")
        self.assertEqual(result, [])
        os.remove(empty_csv)

    def test_empty_xlsx_file(self):
        """Тест чтения пустого XLSX файла."""
        empty_xlsx = "empty_test.xlsx"
        pd.DataFrame().to_excel(empty_xlsx, index=False)
        result = read_csv_end_xlsx_file(empty_xlsx)
        self.assertEqual(result, [])
        os.remove(empty_xlsx)

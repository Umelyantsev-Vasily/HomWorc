import json
import os
import tempfile
import unittest
from unittest.mock import patch

from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):
    def setUp(self):
        # Создаем временную директорию для тестов
        self.test_dir = tempfile.TemporaryDirectory()
        self.script_dir = self.test_dir.name
        self.valid_json_path = os.path.join(self.script_dir, "valid.json")
        self.invalid_json_path = os.path.join(self.script_dir, "invalid.json")
        self.nonexistent_path = os.path.join(self.script_dir, "nonexistent.json")

        # Создаем тестовые файлы
        with open(self.valid_json_path, "w", encoding="utf-8") as f:
            json.dump([{"id": 1}, {"id": 2}], f)

        with open(self.invalid_json_path, "w", encoding="utf-8") as f:
            f.write("invalid json")

    def tearDown(self):
        # Удаляем временную директорию после тестов
        self.test_dir.cleanup()

    def test_load_valid_transactions(self):
        """Тест загрузки корректного JSON файла"""
        result = load_transactions(self.valid_json_path)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[1]["id"], 2)

    def test_load_invalid_json(self):
        """Тест обработки некорректного JSON"""
        with patch("builtins.print") as mock_print:
            result = load_transactions(self.invalid_json_path)
            self.assertEqual(result, [])
            mock_print.assert_called_once()

    def test_file_not_found(self):
        """Тест обработки отсутствующего файла"""
        with patch("builtins.print") as mock_print:
            result = load_transactions(self.nonexistent_path)
            self.assertEqual(result, [])
            mock_print.assert_called_once()

    def test_non_list_json(self):
        """Тест обработки JSON, который не является списком"""
        non_list_path = os.path.join(self.script_dir, "non_list.json")
        with open(non_list_path, "w", encoding="utf-8") as f:
            json.dump({"key": "value"}, f)

        result = load_transactions(non_list_path)
        self.assertEqual(result, [])

    def test_empty_file(self):
        """Тест обработки пустого файла"""
        empty_path = os.path.join(self.script_dir, "empty.json")
        with open(empty_path, "w", encoding="utf-8"):
            pass

        with patch("builtins.print") as mock_print:
            result = load_transactions(empty_path)
            self.assertEqual(result, [])
            mock_print.assert_called_once()


if __name__ == "__main__":
    unittest.main()

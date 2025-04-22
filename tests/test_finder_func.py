import unittest
from typing import Any, Dict, List

from src.finder_func import coun_description, finder_inf


class TestFinderInf(unittest.TestCase):
    def setUp(self):
        """Подготовка тестовых данных"""
        self.sample_data: List[Dict[str, Any]] = [
            {
                "id": 1,
                "description": "Перевод организации",
                "from": "Maestro 1234567890123456",
                "operationAmount": {"amount": "1000.50", "currency": {"name": "руб.", "code": "RUB"}},
            },
            {
                "id": 2,
                "description": "Пополнение счета",
                "to": "Счет 9876543210987654",
                "operationAmount": {"amount": "500.00", "currency": {"name": "USD", "code": "USD"}},
            },
            {
                "id": 3,
                "description": "Перевод с карты на карту",
                "from": "Visa 1111222233334444",
                "to": "MasterCard 5555666677778888",
            },
        ]

    def test_find_by_description(self):
        """Поиск по описанию транзакции"""
        result = finder_inf(self.sample_data, "Перевод")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[1]["id"], 3)

    def test_find_by_card_number(self):
        """Поиск по номеру карты"""
        result = finder_inf(self.sample_data, "1234")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 1)

    def test_case_insensitive_search(self):
        """Проверка регистронезависимого поиска"""
        result = finder_inf(self.sample_data, "пОпОлН")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 2)

    def test_no_matches(self):
        """Проверка случая, когда совпадений нет"""
        result = finder_inf(self.sample_data, "Биткоин")
        self.assertEqual(len(result), 0)

    def test_special_characters(self):
        """Проверка обработки спецсимволов"""
        result = finder_inf(self.sample_data, "1000.50")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 1)

    def test_empty_input(self):
        """Проверка пустой строки поиска"""
        result = finder_inf(self.sample_data, "")
        self.assertEqual(len(result), 3)  # Должен вернуть все элементы

    def test_empty_data(self):
        """Проверка пустого списка транзакций"""
        result = finder_inf([], "Перевод")
        self.assertEqual(len(result), 0)


# ////////////////////////////////////////////////////////////


class TestCounDescription(unittest.TestCase):
    def setUp(self):
        """Подготовка тестовых данных"""
        self.sample_transactions = [
            {"description": "Перевод организации", "amount": 100},
            {"description": "Перевод с карты на карту", "amount": 50},
            {"description": "Перевод организации", "amount": 200},
            {"description": "Пополнение счета", "amount": 300},
            {"description": "Открытие вклада", "amount": 400},
            {"description": "Перевод организации", "amount": 150},
            {"description": "Перевод со счета на счет", "amount": 250},
        ]

        self.common_descriptions = [
            "Перевод организации",
            "Перевод с карты на карту",
            "Перевод со счета на счет",
            "Открытие вклада",
            "Пополнение счета",
        ]

    def test_basic_counting(self):
        """Тест базового подсчета"""
        result = coun_description(self.sample_transactions, self.common_descriptions)
        expected = {
            "Перевод организации": 3,
            "Перевод с карты на карту": 1,
            "Перевод со счета на счет": 1,
            "Открытие вклада": 1,
            "Пополнение счета": 1,
        }
        self.assertEqual(result, expected)

    def test_case_insensitivity(self):
        """Тест регистронезависимости"""
        modified_transactions = [
            {"description": "ПЕРЕВОД ОРГАНИЗАЦИИ", "amount": 100},
            {"description": "перевод с карты на карту", "amount": 50},
        ]
        result = coun_description(modified_transactions, self.common_descriptions)
        expected = {
            "Перевод организации": 1,
            "Перевод с карты на карту": 1,
            "Перевод со счета на счет": 0,
            "Открытие вклада": 0,
            "Пополнение счета": 0,
        }
        self.assertEqual(result, expected)

    def test_empty_transactions(self):
        """Тест с пустым списком транзакций"""
        result = coun_description([], self.common_descriptions)
        expected = {
            "Перевод организации": 0,
            "Перевод с карты на карту": 0,
            "Перевод со счета на счет": 0,
            "Открытие вклада": 0,
            "Пополнение счета": 0,
        }
        self.assertEqual(result, expected)

    def test_empty_descriptions(self):
        """Тест с пустым списком категорий"""
        result = coun_description(self.sample_transactions, [])
        self.assertEqual(result, {})

    def test_missing_description_field(self):
        """Тест с транзакциями без поля description"""
        transactions = [{"amount": 100}, {"note": "Перевод организации"}]
        result = coun_description(transactions, self.common_descriptions)
        expected = {
            "Перевод организации": 0,
            "Перевод с карты на карту": 0,
            "Перевод со счета на счет": 0,
            "Открытие вклада": 0,
            "Пополнение счета": 0,
        }
        self.assertEqual(result, expected)

    def test_partial_description_match(self):
        """Тест на частичное совпадение описаний"""
        transactions = [{"description": "Перевод", "amount": 100}, {"description": "Организация", "amount": 200}]
        result = coun_description(transactions, self.common_descriptions)
        expected = {
            "Перевод организации": 0,
            "Перевод с карты на карту": 0,
            "Перевод со счета на счет": 0,
            "Открытие вклада": 0,
            "Пополнение счета": 0,
        }
        self.assertEqual(result, expected)

    def test_extra_descriptions(self):
        """Тест с категориями, которых нет в транзакциях"""
        extra_descriptions = self.common_descriptions + ["Новая категория"]
        result = coun_description(self.sample_transactions, extra_descriptions)
        self.assertEqual(result["Новая категория"], 0)


if __name__ == "__main__":
    unittest.main()

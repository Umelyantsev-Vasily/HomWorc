from collections import Counter

from typing import List, Dict, Any
import re



def finder_inf(list_data: List[Dict[str, Any]], input_str: str) -> List[Dict[str, Any]]:
    """Фильтрует список банковских операций по заданной строке"""
    try:
        pattern = re.compile(re.escape(input_str), re.IGNORECASE)  # Экранируем спецсимволы
        filtered_list = []

        for item in list_data:
            # Проверяем все строковые значения в словаре
            for value in item.values():
                if isinstance(value, str) and pattern.search(value):
                    filtered_list.append(item)
                    break
                elif isinstance(value, dict):
                    # Рекурсивно проверяем вложенные словари
                    for sub_value in value.values():
                        if isinstance(sub_value, str) and pattern.search(sub_value):
                            filtered_list.append(item)
                            break

        return filtered_list
    except Exception as e:
        print(f"Ошибка при фильтрации: {e}")
        return []


def coun_description(transcription_list, list_description):
    """Подсчитывает количество операций в каждой заданной категории."""
    count = dict(Counter())
    for list_descr in list_description:
        count[list_descr] = 0
        for transcription in transcription_list:
            description = transcription.get('description', '').lower()
            if description == list_descr.lower():
                count[list_descr] += 1


    return count
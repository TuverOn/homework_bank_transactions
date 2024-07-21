from typing import Dict, List


def filter_by_state(my_dictionary: List[Dict], state: str) -> List[Dict]:
    """принимает список словарей и возвращает новый список по значению ключа state"""
    filtered_dictionary = []
    for dictionary in my_dictionary:
        if dictionary.get("state") == state.upper():
            filtered_dictionary.append(dictionary)
    return filtered_dictionary


def sort_by_date(my_dictionary: List[Dict], reverse: bool = True) -> List[Dict]:
    """сортирует принимаемый список по дате"""
    if reverse is True:
        sorted_dictionary = sorted(my_dictionary, key=lambda item: item["date"])
        return sorted_dictionary
    else:
        sorted_dictionary = sorted(
            my_dictionary, key=lambda item: item["date"], reverse=True
        )
        return sorted_dictionary

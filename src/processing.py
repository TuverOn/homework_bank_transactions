def filter_by_state(list_state_id: list, state: str = "EXECUTED") -> list:
    """Функция, которая принимает на вход список словарей и значение для ключа state
    и возвращает новый список, содержащий только те словари, у которых ключ state
    содержит переданное в функцию значение."""


    list_id = list(filter(lambda el: el["state"] == state, list_state_id))
    return list_id


list_state_id = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
]
print(filter_by_state(list_state_id))
print(filter_by_state(list_state_id,'CANCELED'))

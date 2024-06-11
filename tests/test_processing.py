from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(dict_fixture_1):
    assert filter_by_state(dict_fixture_1, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(dict_fixture_1, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_sort_by_date_1(dict_fixture_1):
    assert sort_by_date(dict_fixture_1) == [
        {"id": 41428829, "state": "EXECUTED", "date": "03-07-2019"},
        {"id": 615064591, "state": "CANCELED", "date": "14-10-2018"},
        {"id": 594226727, "state": "CANCELED", "date": "12-09-2018"},
        {"id": 939719570, "state": "EXECUTED", "date": "30-06-2018"},
    ]


def test_sort_by_date_2(dict_fixture_2):
    assert sort_by_date(dict_fixture_2, reverse=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "30-06-2018"},
        {"id": 594226727, "state": "CANCELED", "date": "12-09-2018"},
        {"id": 615064591, "state": "CANCELED", "date": "14-10-2018"},
        {"id": 41428829, "state": "EXECUTED", "date": "03-07-2019"},
    ]

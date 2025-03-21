from src.processing import filter_by_state,sort_by_date

import pytest


@pytest.mark.parametrize("x, expected",[
    ([
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}
], [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ([], [])
])

def test_filter_by_state(x, expected):
    assert filter_by_state(x) == expected

@pytest.mark.parametrize("z, title_expected",[
    ([
    {"id": 41428829, "state": "", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "", "date": "2018-09-12T21:27:25.241689"}
], ValueError),
    ([{}], ValueError)
    
])

def test_invalid_filter_by_state(z, title_expected):
    with pytest.raises(ValueError):
        assert filter_by_state(z) == title_expected


@pytest.mark.parametrize("data, new_expected",[
    ([
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
],[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),


])

def test_sort_by_date(data, new_expected):
    assert sort_by_date(data) == new_expected

@pytest.mark.parametrize("data_new, date_expected",[
    ([
    {"id": 41428829, "state": "EXECUTED", "date": "dgsha-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "fgahh-06-30T02:08:58.425572"}],ValueError ),
([
    {"id": 41428829, "state": "EXECUTED", "date": "*()?;;№-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": ",ЮБ(??:;№-06-30T02:08:58.425572"}],ValueError ),
([
    {"id": 41428829, "state": "EXECUTED", "date": ""},
    {"id": 939719570, "state": "EXECUTED", "date": ""}],ValueError )
])

def test_invalid_sort_by_date(data_new, date_expected):
    with pytest.raises(ValueError):
        assert sort_by_date(data_new) == date_expected

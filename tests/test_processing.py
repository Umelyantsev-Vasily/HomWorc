import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_filter_by_state_1(state: list[dict], expected: list[dict]) -> None:
    assert filter_by_state(state) == expected


def test_filter_by_state_2(by_state_list: list[dict], by_state_list_2: list[dict]) -> None:
    assert filter_by_state(by_state_list) == by_state_list_2


@pytest.mark.parametrize(
    "list_data, title_expected",
    [
        (
            [
                {"id": 41428829, "state": "", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "", "date": "2018-09-12T21:27:25.241689"},
            ],
            ValueError,
        ),
        ([{""}], ValueError),
    ],
)
def test_invalid_filter_by_state(list_data: list[dict], title_expected: type) -> None:
    with pytest.raises(ValueError):
        assert filter_by_state(list_data) == title_expected


@pytest.mark.parametrize(
    "state, state_expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        ("CANCELED", [{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]),
        ("dgdherh", []),
        ("", []),
    ],
)
def test_invalid_filter_by_state_state(state_list_info: list[dict], state: str, state_expected: list[dict]) -> None:
    assert filter_by_state(state_list_info, state) == state_expected


# Тест для sort_by_date
@pytest.mark.parametrize(
    "bul_value, new_expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_sort_by_date(by_state_test_list: list[dict], bul_value: bool, new_expected: list[dict]) -> None:
    assert sort_by_date(by_state_test_list, bul_value) == new_expected


@pytest.mark.parametrize(
    "data_new, date_expected",
    [
        ([""], ValueError),
        ([{"hdghf"}], ValueError),
        ([{"id": 41428829, "state": "EXECUTED", "date": "gfdsgT18:35:29.512364"}], ValueError),
    ],
)
def test_invalid_sort_by_date(data_new: list[dict], date_expected: type) -> None:
    with pytest.raises(ValueError):
        assert sort_by_date(data_new) == date_expected

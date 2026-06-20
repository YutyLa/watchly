from project import find_shows, count_completed, get_completion_rate


def test_find_shows():
    shows = [{"Title": "Death Note"}, {"Title": "Death Parade"}, {"Title": "Naruto"}]
    assert len(find_shows(shows, "death")) == 2


def test_count_completed():
    shows = [{"Status": "Completed"}, {"Status": "Completed"}, {"Status": "To Watch"}]

    assert count_completed(shows) == 2


def test_get_completion_rate():
    shows = [{"Status": "Completed"}, {"Status": "Completed"}, {"Status": "To Watch"}]

    assert get_completion_rate(shows) == 66.67

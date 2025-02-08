def get_random_users(n_users: int) -> dict[str, int]:
    pass


def test_users1():
    users = get_random_users(10)
    assert len(users) == 10


def test_users_type():
    users = get_random_users(1)
    assert isinstance(users, dict)
    assert isinstance(list(users.keys())[0], str)
    assert isinstance(list(users.values())[0], int)


def test_users_large_number():
    users = get_random_users(1000)
    assert len(users) == 1000


def test_users_unique_keys():
    users = get_random_users(5)
    assert len(set(users.keys())) == 5


def test_users_negative():
    try:
        get_random_users(-1)
        assert False
    except ValueError:
        assert True


def test_users_value_range():
    users = get_random_users(5)
    for value in users.values():
        assert 0 <= value <= 100


def test_users_different_calls():
    users1 = get_random_users(3)
    users2 = get_random_users(3)
    assert users1 != users2


if __name__ == '__main__':
    pass

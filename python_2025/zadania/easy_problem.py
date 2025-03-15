def easy_problem(n: int) -> int:
    solutions = 0
    for b in range(1, 10000):
        a = n - b
        if a > 0:
            solutions += 1
        else:
            return solutions


def easy_problem_fast(n: int) -> int:
    return n - 1


def test_n0():
    assert easy_problem(2) == 1
    assert easy_problem(4) == 3
    assert easy_problem(6) == 5


if __name__ == '__main__':
    for n in range(1, 1000):
        print(n, easy_problem(n))

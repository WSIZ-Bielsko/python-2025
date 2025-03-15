def sum_digits(num: int) -> int:
    digits = [int(x) for x in str(num)]  # python's "comprehension"
    return sum(digits)


def test_sum0():
    assert sum_digits(0) == 0
    assert sum_digits(1) == 1
    assert sum_digits(11) == 2
    assert sum_digits(112) == 4
    assert sum_digits(1234) == 10
    assert sum_digits(1000000001) == 2


def find_number(x: int, y: int) -> int:
    """
    Szukamy liczby, której suma cyfr wynosi "x", a suma cyfr liczby o 1 większej wynosi y
    :param x:
    :param y:
    :return: szukana liczba lub -1 jeśli taka liczba nie istnieje
    """

    # hint: zrobić pętlę 1...10**6 ..powinno przejść w 1sek... i dla każdej takiej liczby sprawdzamy sumę cyfr....

    for num in range(1, 10 ** 4):
        xx = sum_digits(num)
        yy = sum_digits(num + 1)

        if xx == x and yy == y:
            return num
    return -1


def test_zero():
    assert find_number(4, 5) == 4


def test_one():
    assert find_number(1, 2) == 1


if __name__ == '__main__':
    for x in range(2, 140):
        for y in range(1, 140):
            if find_number(x, y) > -1 and y != x + 1:
                print(x, y, abs(x - y))

from datetime import datetime
from random import randint

from python_2025.common import measure_ram


def gen_unique_ints(n_numbers: int) -> list[int]:
    """
    Generates `n_numbers` unique integers.
    :param n_numbers:
    :return:
    """
    numbers = []
    for i in range(n_numbers):
        numbers.append(i)

    return numbers


def gen_unique_ints2(n_numbers: int) -> list[int]:
    """
    Generates `n_numbers` unique integers.
    :param n_numbers:
    :return:
    """
    numbers = []
    for i in range(n_numbers):
        numbers.append(randint(0, 10 ** 30))
    # problem: not guaranteed to generate enough numbers....
    return numbers


def gen_unique_ints3(n_numbers: int) -> list[int]:
    """
    Generates `n_numbers` unique integers.
    :param n_numbers:
    :return:
    """
    numbers = []
    while len(numbers) < n_numbers:
        x = randint(0, 10 ** 9)
        if x not in numbers:
            numbers.append(x)

    return numbers


def gen_unique_ints4(n_numbers: int) -> list[int]:
    """
    Generates `n_numbers` unique integers.
    :param n_numbers:
    :return:
    """
    numbers = set()  # !! szybka struktura danych....

    while len(numbers) < n_numbers:
        x = randint(0, 10 ** 9)
        if x not in numbers:
            numbers.add(x)

    return list(numbers)


def ts():
    return datetime.now().timestamp()

@measure_ram
def performance_generation(n_numbers: int):
    n = n_numbers
    st = ts()
    x = gen_unique_ints2(n)
    en = ts()
    n_n_numbers = len(set(x))
    print(f'generated {n=} (true: {n_n_numbers=}) in {en - st:.3f}s')


if __name__ == '__main__':
    performance_generation(10 ** 5)

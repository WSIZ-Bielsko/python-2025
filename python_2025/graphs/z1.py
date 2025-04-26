from collections import Counter

from pip._internal.models import candidate


def find_isolated_elements(data: list[int]) -> list[int]:
    counts = Counter(data)
    return [element for element in counts.keys() if counts[element] == 1]


def find_people_voting_fore(votes: dict[str, int], candidate: int) -> list[str]:
    # znaleźć wszystkie osoby które głosowały na kandydata o numerze `candidate`
    pass


if __name__ == '__main__':
    w = [1, 2, 7, 7, 3, 2, 1, 10]  # dane
    # znalezc unikalne liczby w `w`
    # posortować malejaco
    # ff = find_isolated_elements(w)
    # print(ff)
    # "comprehension"

    # zz = [a ** 2 for a in w if a > 5]
    # print(zz)

    votes: dict[str, int] = {'Joe': 12, 'Xi': 4, 'Willy': 7, 'Frank': 2, 'Jimmy': 4}
    print(find_people_voting_fore(votes, 4))  # ['Xi', 'Jimmy']

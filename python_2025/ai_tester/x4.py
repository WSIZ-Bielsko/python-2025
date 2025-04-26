from copy import copy, deepcopy

if __name__ == '__main__':
    w = [[1, 2], [3, 4]]
    print(w)
    new_w = deepcopy(w)   # tworzymy nową listę
    new_w[0][0] = 111
    print(new_w)
    print(w)


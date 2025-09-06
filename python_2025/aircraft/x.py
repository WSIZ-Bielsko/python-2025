if __name__ == '__main__':
    # sets (zbiory)
    s = set()
    s.add(12)
    s.add(13)
    s.add(20)
    s.add(12)
    print(s)
    print(len(s))
    print(12 in s)
    s.remove(12)
    print(s)

    # dictionaries

    m: dict[int, str] = dict()

    m[1] = 'abra'
    m[2] = 'kadabra'
    m[100100100100] = 'klamka'
    print(m)
    print(m[2])

if __name__ == '__main__':
    dd = dict()

    # writing
    dd[1] = 12
    dd['kadabra'] = 18
    dd[10 ** 9 + 18] = 101
    dd[(1, 2)] = 21

    # dd[key] = value

    print(dd)

    # reading
    print(dd['kadabra'])  # 18
    print((1, 2) in dd)  # True
    dd[1] += 1  # works; now dd[1] = 13
    print(dd[1])

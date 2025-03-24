def solve(board: str) -> str:
    if 'xxx' in board:
        return 'x'
    elif 'ooo' in board:
        return 'o'
    else:
        return 'draw'


def test_solve1():
    assert solve('xo') == 'draw'


def test_solve2():
    assert solve('xxx') == 'x'


def test_solve9():
    assert solve('ooo') == 'o'


def test_solve3():
    assert solve('xxxo') == 'x'


def test_solve4():
    assert solve('xxxooo') == 'x'


def test_solve5():
    assert solve('ooooooooxxxooo') == 'x'


def test_solve5():
    assert solve('xxooxxooxxooxxoo') == 'draw'

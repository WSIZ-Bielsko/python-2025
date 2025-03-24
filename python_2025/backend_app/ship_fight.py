def shot(board: str, position: int) -> tuple[str, str]:
    """
    board = '.....ooo....ooo....'

    po trafieniu zamieniamy 'o' na '.'

    :returns : result, new_board
    """
    if board[position] == 'o':
        n_board = board[:position] + '.' + board[position + 1:]
        return 'hit', n_board

    if position == 0:
        if board[1] == 'o':
            return 'near', board
    if position == len(board) - 1:
        if board[-2] == 'o':
            return 'near', board

    if board[position - 1] == 'o' or board[position + 1] == 'o':
        return 'near', board

    return 'miss', board


def test_zero():
    assert shot('.....ooo....ooo....', 0)[0] == 'miss'


def test_zero1():
    assert shot('.ooo....ooo....', 0)[0] == 'near'


def test_zero2():
    assert shot('ooo....ooo....', 0)[0] == 'hit'


def test_shot_in_the_middle():
    assert shot('ooo....ooo....', 3)[0] == 'near'


def test_hit_removes_ship():
    assert shot('ooo....ooo....', 1)[1] == 'o.o....ooo....'


def test_hit_last():
    board = 'ooo....ooo..oo'
    n = len(board)
    assert shot(board, n-1)[0] == 'hit'
    assert shot(board, n-1)[1] == 'ooo....ooo..o.'

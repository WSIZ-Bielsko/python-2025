def is_winner_ez(board: list[list[str]], player: str) -> bool:
    pattern = [player] * 3
    if any(board[i] == pattern for i in range(3)):
        return True
    if [board[i][i] for i in range(3)] == pattern:
        return True
    if [board[i][2-i] for i in range(3)] == pattern:
        return True
    return False


def is_winner(board: list[list[str]], player: str) -> bool:
    if is_winner_ez(board, player) or is_winner_ez(transpose(board), player):
        return True
    return False


def transpose(board: list[list[str]]) -> list[list[str]]:
    res = [['.'] * 3 for _ in range(3)]  # empty board
    for r in range(3):
        for c in range(3):
            res[r][c] = board[c][r]
    return res


def print_board(board: list[list[str]]):
    for row in board:
        print('|'.join(row))





if __name__ == '__main__':
    board: list[list[str]] = [[".", "o", "z"], [".", "x", "."], [".", ".", "x"]]
    print_board(board)
    board_t = transpose(board)
    print('----')
    print_board(board_t)

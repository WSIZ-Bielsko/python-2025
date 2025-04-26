from python_2025.ai_tester.a import is_winner


# Test 1: Horizontal win (top row)
def test_horizontal_win_top():
    board = [
        ["x", "x", "x"],
        [".", "o", "."],
        ["o", ".", "."]
    ]
    assert is_winner(board, "x") == True
    assert is_winner(board, "o") == False


# Test 2: Vertical win (left column)
def test_vertical_win_left():
    board = [
        ["o", "x", "."],
        ["o", ".", "x"],
        ["o", ".", "."]
    ]
    assert is_winner(board, "o") == True
    assert is_winner(board, "x") == False


# Test 3: Diagonal win (top-left to bottom-right)
def test_diagonal_win_main():
    board = [
        ["x", "o", "."],
        [".", "x", "o"],
        ["o", ".", "x"]
    ]
    assert is_winner(board, "x") == True
    assert is_winner(board, "o") == False


# Test 4: Diagonal win (top-right to bottom-left)
def test_diagonal_win_secondary():
    board = [
        [".", "o", "x"],
        [".", "x", "o"],
        ["x", ".", "."]
    ]
    assert is_winner(board, "x") == True
    assert is_winner(board, "o") == False


# Test 5: No winner (partial board)
def test_no_winner_partial():
    board = [
        [".", "o", "."],
        [".", "x", "."],
        [".", ".", "x"]
    ]
    assert is_winner(board, "x") == False
    assert is_winner(board, "o") == False


# Test 6: Full board with no winner
def test_no_winner_full():
    board = [
        ["x", "o", "x"],
        ["o", "x", "o"],
        ["o", "x", "o"]
    ]
    assert is_winner(board, "x") == False
    assert is_winner(board, "o") == False


# Test 7: Middle row win
def test_horizontal_win_middle():
    board = [
        ["o", ".", "x"],
        ["x", "x", "x"],
        [".", "o", "."]
    ]
    assert is_winner(board, "x") == True
    assert is_winner(board, "o") == False

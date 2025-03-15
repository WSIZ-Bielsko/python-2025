def reverse_window(a: str) -> str:
    pass


def test_easy():
    assert reverse_window('w') == 'w'
    assert reverse_window('qw') == 'wp'
    assert reverse_window('qwq') == 'pwp'
    assert reverse_window('pppq') == 'pqqq'

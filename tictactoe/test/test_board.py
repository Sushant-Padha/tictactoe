from .. import board
import pytest

n = 3
default_value = 'X'
board_state = [['X', 'X', 'X'],
               ['X', 'X', 'X'],
               ['X', 'X', 'X']]
board_obj = board.Board(n=n, value=default_value)
index = 6  # 2, 0
i1, i2 = 2, 0
value = 'O'


def test_state():
    assert board_obj.state == board_state


def test_str():
    try:
        print(board_obj)
    except:
        assert False
    assert True


def test_convert_index():
    assert board_obj.convert_index(index) == (i1, i2)


def test_update():
    new_board_state = [['X', 'X', 'X'],
                       ['X', 'X', 'X'],
                       ['O', 'X', 'X']]
    new_board_obj = board.Board(n=n, value=default_value)
    new_board_obj.update(6, value)
    assert new_board_obj.state == new_board_state


def test_update_exception():
    new_board_obj = board.Board(n=n, value=default_value)
    try:
        new_board_obj.update(9, value)  # should raise IndexError
    except:
        assert True
        return
    assert False

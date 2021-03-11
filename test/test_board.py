from tictactoe.board import Board
import pytest

n = 3
board_state = [['X', 'X', 'X'],
               ['X', 'X', 'X'],
               ['X', 'X', 'X']]
board_obj = Board(n=n, state=board_state)
index = 6  # 2, 0
i1, i2 = 2, 0
value = 'O'
out_of_range_index = 9


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
    new_board_obj = Board(n=n, state=board_state)
    new_board_obj.update(index, value)
    assert new_board_obj.state == new_board_state
    assert index in new_board_obj.updates


def test_update_exception():
    new_board_obj = Board(n=n, state=board_state)
    try:
        new_board_obj.update(out_of_range_index, value)  # raise IndexError
    except:
        assert True
        return
    assert False

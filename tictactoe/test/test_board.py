from .. import board
import pytest

n = 3
value = 'X'
board_array = [['X', 'X', 'X'],
               ['X', 'X', 'X'],
               ['X', 'X', 'X']]
board_obj = board.Board(n=n, value=value)


def test_board():
    assert board_obj.board == board_array


def test_str():
    try:
        print(board_obj)
    except:
        assert False
    assert True

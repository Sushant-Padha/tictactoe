from tictactoe.board import Board
from tictactoe.player import Player
import pytest

marker = 'X'
name = 'Alex'
board = Board()
index = 5
player = Player(marker=marker, name=name, board=board)


def test_player():
    assert player.name == name
    assert player.marker == marker
    assert player.board == board


def test_play():
    player.play(index)
    assert board.get_value(index) == player.marker
    assert index in player.moves

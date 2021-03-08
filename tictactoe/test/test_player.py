from tictactoe.board import Board
from tictactoe.player import Player
import pytest

marker = 'X'
name = 'Alex'
board = Board()
index = 6
player = Player(marker=marker, name=name, board=board)


def test_player():
    assert player.name == name
    assert player.marker == marker
    assert player.board == board


def test_play():
    player.play()

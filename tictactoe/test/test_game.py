from tictactoe.player import Player
from tictactoe.board import Board
from tictactoe.console import Console
from tictactoe.game import Game


marker1, marker2 = 'X', 'O'
name1, name2 = 'Adam', 'Eve'

player1_winner_board = [['O', 'X', ' '],
                        ['X', 'X', 'O'],
                        ['O', 'X', 'X']]

vertical_board = [['O', 'O', 'X'],
                  ['X', 'O', 'X'],
                  ['O', 'X', 'X']]

horizontal_board = [['O', 'O', 'X'],
                    ['X', 'X', 'X'],
                    ['O', 'X', 'O']]

diagonal_board = [['O', 'O', 'X'],
                  ['O', 'X', 'X'],
                  ['X', 'X', 'O']]

valid_line = ['X', 'X', 'X']
invalid_line_1 = [' ', ' ', ' ']
invalid_line_2 = ['X', 'O', 'X']

valid_move = 8
invalid_move_1 = -1
invalid_move_2 = 'Seriously?'
invalid_move_3 = 9

invalid_marker = ' '

board = Board()
console = Console()
player1 = Player(marker=marker1, name=name1, board=board)
player2 = Player(marker=marker2, name=name2, board=board)
game = Game(player1=player1, player2=player2, board=board, console=console)


def test_winner():
    new_board = Board(state=player1_winner_board)
    new_game = Game(player1=player1, player2=player2,
                    board=new_board, console=console)
    assert new_game.winner() == player1
    assert game.winner() is None


def test_vertical():
    new_board = Board(state=vertical_board)
    new_game = Game(player1=player1, player2=player2,
                    board=new_board, console=console)
    assert new_game.vertical() == marker1


def test_horizontal():
    new_board = Board(state=horizontal_board)
    new_game = Game(player1=player1, player2=player2,
                    board=new_board, console=console)
    assert new_game.horizontal() == marker1


def test_diagonal():
    new_board = Board(state=diagonal_board)
    new_game = Game(player1=player1, player2=player2,
                    board=new_board, console=console)
    assert new_game.diagonal() == marker1


def test_valid_line():
    assert game.valid_line(valid_line)
    assert not game.valid_line(invalid_line_1)
    assert not game.valid_line(invalid_line_2)


def test_valid_move():
    assert game.valid_move(valid_move)
    assert not game.valid_move(invalid_move_1)
    assert not game.valid_move(invalid_move_2)
    assert not game.valid_move(invalid_move_3)


def test_find_player_by_marker():
    assert game.find_player_by_marker(marker1) == player1
    assert game.find_player_by_marker(marker2) == player2
    assert game.find_player_by_marker(invalid_marker) is None


def test_play(play_cmdopt):
    if play_cmdopt:
        print("Get ready to play tictactoe (for testing purposes) ...")
        game.play()

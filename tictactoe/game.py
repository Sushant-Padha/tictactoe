from typing import Iterable
from tictactoe.board import Board
from tictactoe.player import Player


class Game:
    '''Defines new tictactoe game
    '''
    # list of all moves
    moves = []

    # whether the last move was valid or not
    last_move_invalid = False

    def __init__(self, player1: Player, player2: Player,
                 board: Board = Board()) -> None:
        '''Instantiate new game class

        Args:
            player1 (Player): player 1
            player2 (Player): player 2
            board (Board): board. Defaults to Board()
        '''
        self.player1 = player1
        self.player2 = player2
        self.board = board

    def winner(self):
        for line in self.vertical(), self.horizontal(), self.diagonal():
            if line is not None:
                return line
        return None

    def vertical(self):
        for i in range(self.board.n):
            col = [row[i] for row in self.board.state]
            if self.valid_line(col):
                return col[0]
        return None

    def horizontal(self):
        for row in range(self.board.state):
            if self.valid_line(row):
                return row[0]
        return None

    def diagonal(self):
        n = self.board.n
        diag1 = [self.board.state[a][a] for a in range(n)]
        diag2 = [self.board.state[a][n - 1 - a] for a in range(n)]
        for diag in (diag1, diag2):
            if self.valid_line(diag):
                return diag[0]
        return None

    def valid_line(self, iter: Iterable):
        '''Return true if all items are equal and a marker

        Args:
            iter (Iterable): iterable to check

        Returns:
            bool: whether iter is a valid line or not
        '''
        markers = (self.player1.marker, self.player2.marker)
        reduced = set(iter)
        if len(reduced) == 1 and reduced[0] in markers:
            return True
        else:
            return False

    def play(self):
        winner = None
        i = 0
        while winner is None:
            i += 1
            # alternate between players
            if self.last_move_invalid:
                player = player
            else:
                player = self.player1 if i % 2 != 0 else self.player2
            print(self.board)
            move = input(f"'{player.name}' make your move: ")
            if self.valid_move(move):
                print('Invalid move. Please try again.')
                self.last_move_invalid = True
                continue
            self.last_move_invalid = False
            move = int(move)
            player.play(move)
            winner = self.winner()
        else:
            print(f"Congratulations '{player.name}'! You have won the game.")
            print("Thanks for playing the game!")
            feedback = input("Please leave some feedback for improvment: ")
            print("Thank you for your feedback.")
            print("Your feedback will be promptly ignored.")
            print("Peace ✌")

    def valid_move(self, move: str):
        try:
            move = int(move)
        except:
            return False
        if self.board.n**2 - 1 < move < 0:
            return False
        if move in self.moves:
            return False
        return True

from typing import Iterable
from board import Board
from player import Player
from console import Console


class Game:
    '''Defines new tictactoe game
    '''
    # list of all moves
    moves = []

    # whether the last move was valid or not
    last_move_invalid = False

    def __init__(self, player1: Player, player2: Player,
                 board: Board = Board(), console: Console = Console()) -> None:
        '''Instantiate new game class

        Args:
            player1 (Player): player 1
            player2 (Player): player 2
            board (Board): board. Defaults to Board()
            console (Console): console. Defaults to Console()
        '''
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.console = console

    def winner(self):
        for line in self.vertical(), self.horizontal(), self.diagonal():
            if line is not None:
                marker = line
                return self.find_player_by_marker(marker)
        return None

    def vertical(self):
        for i in range(self.board.n):
            col = [row[i] for row in self.board.state]
            if self.valid_line(col):
                return col[0]
        return None

    def horizontal(self):
        for row in self.board.state:
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
        if len(reduced) == 1 and reduced.pop() in markers:
            return True
        else:
            return False

    def play(self):
        console = self.console
        winner = None
        i = 0
        while winner is None:
            i += 1
            # alternate between players
            if self.last_move_invalid:
                player = player
            else:
                player = self.player1 if i % 2 != 0 else self.player2
            console.print(self.board)
            move = console.input(f"'{player.name}' make your move: ")
            if not self.valid_move(move):
                console.print('Invalid move. Please try again.')
                self.last_move_invalid = True
                console.clear()
                continue
            move = int(move)
            self.last_move_invalid = False
            self.moves.append(move)
            player.play(move)
            winner = self.winner()
        else:
            console.print(f"Congratulations '{player.name}'! " +
                          "You have won the game.")
            console.print("Thanks for playing the game!")
            feedback = console.input(
                "Please leave some feedback for improvment: ")
            console.print("Thank you for your feedback.")
            console.print("Your feedback will be promptly ignored.")
            console.print("Peace ✌")

    def valid_move(self, move: str):
        try:
            move = int(move)
        except:
            return False
        if move > self.board.n**2 - 1 or move < 0:
            return False
        if move in self.moves:
            return False
        return True

    def find_player_by_marker(self, marker: str):
        players = self.player1, self.player2
        for p in players:
            if p.marker == marker:
                return p

from tictactoe.board import Board


class Player:
    '''Defines new tictactoe player
    '''

    def __init__(self, marker: str, name: str = 'NewPlayer',
                 board: Board = Board()):
        '''Instantiate new player instance

        Args:
            marker (str): marker of player. either X or O
            name (str, optional): name of player. Defaults to 'NewPlayer'.
            board (Board, optional): board to use for play. Defaults to Board()
        '''
        self.marker = marker
        self.name = name
        self.board = board

    def play(self, index: int):
        '''Play a move on board if it hasn't been played before

        Args:
            index (int): index to change

        Raises:
            ValueError: the move has already been made
            IndexError: index is invalid for board
        '''
        # check if this move has been made
        if index in self.board.updates:
            raise ValueError("The move has already been made")
        try:
            self.board.update(index, self.marker)
        except:
            raise IndexError("index is invalid for board")

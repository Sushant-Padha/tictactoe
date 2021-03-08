from typing import Any
import numpy as np

global box_drawing
box_drawing = ['┛', '┫', '┓', '┳', '┏', '┣', '┗', '┻', '━', '┃', '╋']


class Board:
    '''Defines new board to play tictactoe
    '''

    def __init__(self, n: int, value: str = ''):
        '''Instantiate new board instance

        Args:
            n (int): dimension of board
            value (str): value to fill the board with
        '''
        self.n = n
        self.state = [[value for _ in range(n)].copy() for _ in range(n)]

    def __str__(self):
        '''Pretty representation of board
        '''
        # for i, row in enumerate(self.board):
        #     if i == 0:
        #         print()
        #     for j, col in enumerate(row):
        #         pass
        return np.array(self.state).__str__()

    def update(self, index: int, value: str):
        '''Update board state

        Args:
            index (int): index of position to update
            value (str): value to update to
        '''
        pass

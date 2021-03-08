from typing import Any
import numpy as np

box_drawing = ['┛', '┫', '┓', '┳', '┏', '┣', '┗', '┻', '━', '┃', '╋']


class Board:
    '''Defines new board to play tictactoe
    '''
    # list of all prior updates to board state
    updates = []

    def __init__(self, n: int = 3, value: str = ''):
        '''Instantiate new board instance

        Args:
            n (int): dimension of board
            value (str): value to fill the board with
        '''
        self.n = n
        self.value = value
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

        Raises:
            IndexError: invalid index for board
        '''
        i1, i2 = self.convert_index(index)
        try:
            self.state[i1][i2] = value
        except:
            raise IndexError('Invalid index for board')
        self.updates.append(index)

    @staticmethod
    def convert_index(index: int):
        '''Convert index to two indices for 2d array

        Args:
            index (int): index

        Returns:
            tuple: two indices
        '''
        i1 = index // 3
        i2 = index % 3
        return i1, i2

    def get_value(self, index: int):
        '''Get the value at index

        Args:
            index (int): index

        Raises:
            IndexError: invalid index for board
        '''
        i1, i2 = self.convert_index(index)
        try:
            value = self.state[i1][i2]
        except:
            raise IndexError('Invalid index for board')
        return value

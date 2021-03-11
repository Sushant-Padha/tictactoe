from typing import Any, Iterable
import numpy as np

box_drawing = ['┛', '┫', '┓', '┳', '┏', '┣', '┗', '┻', '━', '┃', '╋']


class Board:
    '''Defines new board to play tictactoe
    '''
    # list of all prior updates to board state
    updates = []

    def __init__(self, n: int = 3, state: Iterable[Iterable[str]] = None):
        '''Instantiate new board instance

        Args:
            n (int): dimension of board. Defaults to 3
            state (Iterable[Iterable[str]]): data structure representing
                structure and state of board. Defaults to None
        '''
        if state is None:
            state = [['' for _ in range(n)].copy() for _ in range(n)]
        self.n = n
        self.state = state

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

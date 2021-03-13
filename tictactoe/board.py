from typing import Any, Iterable

box_drawing = ['┛', '┫', '┓', '┳', '┏', '┣', '┗', '┻', '━', '┃', '╋']
"""
┏━━━┳━━━┳━━━┓
┃ X ┃ X ┃ X ┃
┣━━━╋━━━╋━━━┫
┃ X ┃ X ┃ X ┃
┣━━━╋━━━╋━━━┫
┃ X ┃ X ┃ X ┃
┗━━━┻━━━┻━━━┛
"""


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
            state = [[' ' for _ in range(n)].copy() for _ in range(n)]
        self.n = n
        self.state = state

    def __str__(self):
        '''Pretty representation of board
        '''
        c = box_drawing
        n = self.n
        last = len(self.state)
        formatted_str = ""
        for i, row in enumerate(self.state):
            # make top edge
            if i == 0:
                formatted_str += c[4]
                formatted_str += (c[8] * 3 + c[3]) * n
                formatted_str = formatted_str[:-1] + c[2]
            # make internal edge
            else:
                formatted_str += c[5]
                formatted_str += (c[8] * 3 + c[10]) * n
                formatted_str = formatted_str[:-1] + c[1]
            formatted_str += '\n'
            formatted_str += c[9]
            for j, col in enumerate(row):
                col = str(col)
                formatted_str += col.center(3, ' ') + c[9]
            formatted_str += '\n'
        # make bottom edge
        formatted_str += c[6]
        formatted_str += (c[8] * 3 + c[7]) * n
        formatted_str = formatted_str[:-1] + c[0]
        return formatted_str

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

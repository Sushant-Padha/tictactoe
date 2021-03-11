import sys
import os


class Console:
    '''Defines new Console object for I/O
    '''

    def __init__(self):
        '''Instantiate new Console instance
        '''
        pass

    @staticmethod
    def clear():
        os.system('cls')

    @staticmethod
    def print(*args, **kwargs):
        return print(*args, **kwargs)

    @staticmethod
    def input(*args, **kwargs):
        return input(*args, **kwargs)

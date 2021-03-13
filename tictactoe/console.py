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
        if sys.platform in ('win32', 'win64'):
            os.system('cls')
        else:
            os.system('clear')

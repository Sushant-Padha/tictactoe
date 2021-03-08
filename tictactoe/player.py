class Player:
    '''Defines new tictactoe player
    '''
    def __init__(self, marker: str, name: str = 'NewPlayer'):
        '''Instantiate new player instance

        Args:
            marker (str): marker of player. either X or O
            name (str, optional): name of player. Defaults to 'NewPlayer'.
        '''
        self.marker = marker
        self.name = name
        return
    def play(self):
        pass

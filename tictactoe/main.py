from console import Console
from .board import Board
from .player import Player
from .game import Game


def main():
    print("Welcome to tictactoe!")
    print("These are your instructions:")
    print_instructions()
    board_state = [[' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]
    board = Board(n=3, state=board_state)
    console = Console()
    marker1, marker2 = 'X', 'O'
    name1 = input("Player 1 (with marker X) please enter your name: ")
    name2 = input("Player 2 (with marker O) please enter your name: ")
    player1 = Player(marker=marker1, name=name1, board=board)
    player2 = Player(marker=marker2, name=name2, board=board)
    game = Game(player1=player1, player2=player2, board=board, console=console)
    print("The game begins! Good luck.")
    winner = game.play()
    console.print(f"Congratulations '{winner.name}'! " +
                  "You have won the game.")
    console.print("Thanks for playing the game!")
    play_again = console.input("Would you like to play again? " +
                               "(leave empty for no)")
    if play_again:
        main()
    else:
        console.print("Bye 👋")


def print_instructions():
    print("\tTo select a unit for making a move, write its index," +
          "starting from 0 in the top left corner, increasing by one" +
          "as we go to the next column and skip to the beginning of the" +
          "next row.")


if __name__ == '__main__':
    main()

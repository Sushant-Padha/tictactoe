#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tictactoe.console import Console
from tictactoe.board import Board
from tictactoe.player import Player
from tictactoe.game import Game


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
    input("\nThe game begins! Good luck. [Press Enter to start]")
    console.clear()
    winner = game.play()
    print(f"\nCongratulations '{winner.name}'! " +
          "You have won the game.")
    print("Thanks for playing the game!")
    play_again = input("Would you like to play again? " +
                       "(leave empty for no)")
    if play_again:
        main()
    else:
        print("Bye 👋")


def print_instructions():
    print("\tTo select a unit for making a move, write its index, " +
          "starting from 0 in the top left corner, increasing by one " +
          "as we go to the next column and skip to the beginning of the " +
          "next row.\n")


if __name__ == '__main__':
    main()

import math
import time
from datetime import datetime as dtdt
from typing import List, Tuple

from modules.data_structures import tupify
from modules.general import funcerror, num_check
from modules.pretty_printers import (delay_print, delay_print_lines,
                                     display_grid)
from modules.string import name_exclusive_check
from modules.terminal import clear_output

# ! IMPORTANT NOTE
# apart from the stuff needed for this program, this program contains many
# generally useful functions like
# print characters with a delay, clear screen in terminal,
# check if a name is allowed (like checking passwords),
# obtain all items in a nested structure, of varying depth (recursively)

# 👉 Actually, they are imported from general_useful_stuff.py in
# 👉 C:\\Users\\HP\\Documents\\MyPythonModules

# * COMMON STUFF

invalid_input = '\n  Invalid input. Please try again.'

# * for a generalized tictactoe, with a d*d board
# * if u plan on changing up the game like making it 4*4,
# * please first change this
# ! NOTE: You can't change num of people playing, or set a rectangular board

# * d ∈ INTEGERS ; d >= 3
d = 3

# * here set the markers to be used by the players
real_markers = ['X', 'O']
real_markers = set([x.upper() for x in list(
    real_markers)])  # type: ignore[assignment]

# * Chars for making an AWESOME LOOKIN' TABLE!!
# 👉 use UTF8
table_corners = ['┏', '┗', '┛', '┓']
table_intersects = ['┣', '┻', '┫', '┳']
table_lines_cross = ['━', '┃', '╋']


def even(x: float):
    '''Return bool :whether x is even'''
    return (x % 2 == 0) and isinstance(x, int)


def number_check(n, low=0, high=d, int_only=True,
                 low_equal=True, high_equal=False):
    '''Return bool: whether n is between low and high, with some extra params'''
    return num_check(n, low, high, int_only, low_equal, high_equal)


def r_u(n):
    '''Return ceil() of n'''
    try:
        isinstance(n, (float, int))
    except TypeError:
        funcerror('r_u')
    else:
        return math.ceil(n)


def r_d(n):
    '''*Return floor() of n'''
    try:
        isinstance(n, (float, int))
    except TypeError:
        funcerror('r_u')
    else:
        return math.floor(n + 0.000000000000000001)


# 👉 function to print the board


def display_board(grid, markers=list(real_markers), corners=table_corners,
                  inter=table_intersects, hori=table_lines_cross[0],
                  verti=table_lines_cross[1], cross=table_lines_cross[2]):
    '''Return str: formatted so that it looks like a table'''
    return display_grid(grid, markers, corners, inter, hori, verti, cross)


# 👉 get players started


def getting_started(markers=real_markers):
    '''Return tup: markers and names of the players taken via input()'''
    marker1 = '@#$%^&$$'
    player1, player2 = '⌡§', '⌐╒'  # put some weird characters here

    def check_name(x):
        return name_exclusive_check(x, '_-', lowercase_letters=True,
                                    uppercase_letters=True, whole_numbers=True)

    while not(check_name(player1)):
        player1 = input('Player 1, what name would you prefer? \
\n(name must only contain alphabets, underscores, hyphens and numbers) : ')
        if not(check_name(player1)):
            print(invalid_input)
    clear_output()

    while not(check_name(player2)) or player2 == player1:
        player2 = input('Player 2, what name would you prefer? \
\n(name must only contain alphabets, underscores, hyphens and numbers) : ')
        if not(check_name(player2)) or player2 == player1:
            print(invalid_input)
    clear_output()
    print(f'Hello, {player1} and {player2}')

    while marker1 not in markers:
        marker1 = input(f"{player1}, choose your marker (either \
'{list(real_markers)[0]}' or '{list(real_markers)[1]}') : ").upper()
        if marker1 not in markers:
            clear_output()
            print(invalid_input)
    marker2 = list(markers.difference(marker1))[0]
    clear_output()
    print(f'Markers are as follows\n\nPlayer 1 : {player1} : {marker1}\
\nPlayer 2 : {player2} : {marker2}')
    return (marker1.upper(), marker2.upper()), (player1, player2)


# 👉 set position of marker

def set_position(player='player1', marker=list(real_markers)[0], n=d) -> int:
    '''
    Return the index of the marker based on
    the input given by user

    set_position(player='player1', marker='X', n=d)

    Input is given in the form an index, where the index can be any
    integer from 0 to (n*n) (inclusive)
    '''
    index = -1  # type: ignore[no-redef]
    while number_check(index, 0, n * n) is False:
        try:
            index = int(input(f'\
				{player}, enter the value : ').strip())  # type: ignore[assignment]
        except (TypeError, ValueError):
            index = -1
        if number_check(index, 0, n * n) is False:
            print(invalid_input)
    return index


# 👉 check if some items are equal

def equal_iters(tups, param='any') -> bool:  # type: ignore[return]
    '''
    Check if each item in each tuple, is equal
    to all other items in the same tuple, where
    a sequence of tuples is given

    equal_items(tups, param=any)

    param can take the following values:
            any: returns True if any one is True
            all: returns True only if all are True
    '''
    out = []
    for itm in tupify(tups):
        x = True if len(set(tupify(itm))) == 1 else False
        out.append(x)
    if param not in ['any', 'all']:
        funcerror("equal_iters")
        return False
    else:
        if param == 'any':
            return any(out)
        elif param == 'all':
            return all(out)

# 👉 find out if someone has won


def winner(rows, n=d, markers=list(real_markers)) -> bool:
    '''
    Return whether the player has won.
    winner(rows, n=d, markers=['X', 'O'])

    check1: all in a row(horizontal) or all in a column(vertical)
    check2: all in a diagonal (top-left to bottom-right) or
                                    the other diagonal (top-right to bottom-left)
    '''
    def valid_marker(x, marker_list=markers):
        return bool(x in marker_list)
    check1, check2 = [False] * 2
    for i in range(n):
        horizontal = rows[i]
        vertical = []
        for row in rows:
            vertical.append(row[i])
        if equal_iters([horizontal, vertical], param='any') and valid_marker(
                rows[i][i]):
            check1 = True
    diag1 = [rows[a][a] for a in range(n)]
    diag2 = [rows[a][n - 1 - a] for a in range(n)]
    if (equal_iters([diag1, diag2],
                    param='any') and valid_marker(rows[r_d(n / 2)][r_d(n / 2)])):
        check2 = True

    checks = [check1, check2]
    return any(checks)


# 💡💡 FINAL WORKING

try:
    d = int(input("Set the dimension of the board.\n\n\
If you did not get what this means, just leave this empty\n : "))
    if 35 < d < 1:
        raise ValueError
except (TypeError, ValueError):
    d = 3
else:
    print(f"You will play on a {d} x {d} board.")

grid = [['' for _ in range(d)].copy() for _ in range(d)]

clear_output()

print('\n\
+---+---+---+\n\
| O       O |\n\
+           +\n\
|(         )|\n\
+           +\n\
|     ︶    |\n\
+---+---+---+\n')
intro = f'Hello!!! Welcome to this interactive Tic Tac Toe game\n\
The board will look something like this:\n{display_board(grid)}\n\
This game can be played by two people of any age.\n\
Both players will choose a name for themselves.\n\
And, a marker (either \'{list(real_markers)[0]}\' or \
\'{list(real_markers)[1]}\').\n\
Then, the game begins.\n\
Each player will enter a row and column to mark with their marker.\n\
Rows are the horizontal lines, and columns are vertical.\n\
They both start at 0 and go to {d-1} (inclusive).\n\
Rows start from the top, while columns start from the left\n\
The players will take turns doing so.\n\
With every move, the program will check if a player has won.\n\
That\'s all.\n\
ENJOY!!!'
delay_print_lines(intro, 0.007, 0.02)
input('[Press Enter]')

finish = True

while finish:
    clear_output()
    markerinfo, playerinfo = getting_started()
    marker1, marker2, player1, player2 = (markerinfo[0], markerinfo[1],
                                          playerinfo[0], playerinfo[1])
    empty = ['' for _ in range(d)]
    grid1 = [empty.copy() for _ in range(d)]
    grid2 = grid1.copy()

    board0 = (('', '', ''), ('', 'X', ''), ('', '', 'O'))

    specify_position = ('\nHow to specify a position on \
the board.\n\n')
    pos_methods = [f'index : \n\tEvery point has one number to \
specify its position, its index. Index is 0 for the top-right corner \
and, {d * d - 1} for bottom-left corner. \
It increases by 1 if u move to the left (next column), \
and by {d} if u move down (next row).\nEG: marker \'X\' on index 4, and \
marker \'O\' on index 8  on a 3 * 3 board will look like :\n\
{display_board(board0)}',
                   f'NOTE: Index start at 0 and go to {d * d - 1}\n\nCHOOSE WISELY!!!']
    delay_print_lines(specify_position, 0.02, 0.3)
    print(pos_methods[0])
    time.sleep(1)
    delay_print_lines(pos_methods[1], 0.01, 0.1)
    input('[Press Enter]')
    clear_output()
    end = True
    print('This is where the game begins.\nGOOD LUCK 👍')

    count = 0

    game_won = False
    indices_markers: List[Tuple[int, str]] = []
    print(display_board(grid))
    while game_won is False:
        indices = [x[0] for x in indices_markers]
        p, m = (player1, marker1) if even(count) else (player2, marker2)
        index = set_position(p, m, d)
        while index in indices:
            print(display_board(grid))
            print(invalid_input)
            index = set_position(p, m, d)
            clear_output()
        clear_output()
        indices_markers.append((index, m))
        for i, mark in indices_markers:
            row, col = r_d(i / d), i % d
            grid[row][col] = mark.upper()
        game_won = winner(grid, d)
        print(display_board(grid))

        count += 1
    else:
        print('\nCONGRATS!!!\n')
        delay_print('The game has been won by\n', 0.1)
        delay_print('.\n' * 6, 1.0)
        time.sleep(2)
        print(playerinfo[markerinfo.index(m)])
        input('[Press Enter]')
        f = 60 * 60 * 24 * 365.2
        age = r_d((dtdt.today() - dtdt(2006, 5, 26)).total_seconds() / f)
        github_link = '<coming soon :D>'
        credits = (f'This game was coded by Sushant Padha, a {age}-year \
old boy.\nIt has been written in Python using only Sublime Text 3\
(UNREGISTERED) \nand some Python skills.\n\
Its source code can be found at\n\n{github_link}\n\n\
If u can, please provide feedback to improve this program.\n\
It is a beginner\'s take at making a character-based interactive\n\
generalized Tic Tac Toe game.')

        delay_print_lines(credits, 0.05, 0.3)

    finish = bool(input(
        '\nDo you want to play again? \
(type anything for yes. leave it blank for no) : '))

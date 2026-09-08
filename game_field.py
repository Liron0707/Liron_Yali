import random

import consts

game_board = []


# prints the game board
def print_matrix(game_board):
    for i in game_board:
        for j in i:
            print(j, end=" ")
        print()


# creates the list of rows
def create_rows(game_board):
    for i in range(consts.BOARD_ROWS):
        game_board.append([])


# create the board - adds list to the rows of rhe list
def create_board(game_board):
    create_rows(game_board)
    for i in range(consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS):
            game_board[i].append(consts.EMPTY)


def set_flag_on_board(game_board):
    flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
    flag_col = consts.BOARD_COLS - consts.FLAG_COLS
    for row in range(flag_row, consts.BOARD_ROWS):
        for col in range(flag_col, consts.BOARD_COLS):
            game_board[row][col] = consts.FLAG

# marks the mine in the board
def mark_mine_on_board(game_board, mine_cell):
    for row in range(mine_cell[0], mine_cell[0] + consts.MINE_ROWS):
        for col in range(mine_cell[1], mine_cell[1] + consts.MINE_COLS):
            game_board[row][col] = consts.MINE


# sets the mines on the board
def set_mines_on_board(game_board):
    mine_marked = 0
    while mine_marked < consts.MINES_COUNT:
        row = random.randint(0, consts.BOARD_ROWS - consts.FLAG_ROWS - 1)
        col = random.randint(0, consts.BOARD_COLS - consts.FLAG_COLS -  1)
        if row + consts.MINE_ROWS < consts.BOARD_ROWS and col + consts.MINE_COLS < consts.BOARD_COLS:
            mark_mine_on_board(game_board, [row, col])
            mine_marked+=1
            print([row, col])
        else:
            print("BAD",[row, col])



#def is_touching_flag()

create_board(game_board)
set_flag_on_board(game_board)
set_mines_on_board(game_board)
print_matrix(game_board)

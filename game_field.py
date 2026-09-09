import random

import consts

mine_list = []


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


# sets the flag in the board
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


# sets the mines on the board and returns the list of mine starting cells
def set_mines_on_board(game_board):
    mine_marked = 0
    while mine_marked < consts.MINES_COUNT:
        row = random.randint(0, consts.BOARD_ROWS - consts.FLAG_ROWS - 1)
        col = random.randint(0, consts.BOARD_COLS - consts.FLAG_COLS - 1)
        if row + consts.MINE_ROWS < consts.BOARD_ROWS and col + consts.MINE_COLS < consts.BOARD_COLS:
            mark_mine_on_board(game_board, [row, col])
            mine_list.append([row, col])
            mine_marked += 1


# returns true if the soldier touches the flag
def is_touching_flag(game_board, soldier_cell):
    for row in range(soldier_cell[0],
                     soldier_cell[0] + consts.SOLDIER_BODY_ROWS):
        for col in range(soldier_cell[1],
                         soldier_cell[1] + consts.SOLDIER_COLS):
            if game_board[row][col] == consts.FLAG:
                return True


# returns true if the soldier touches a mine
def is_touching_mine(game_board, soldier_cell):
    for row in range(soldier_cell[0] + consts.SOLDIER_BODY_ROWS, soldier_cell[
                                                                     0] + consts.SOLDIER_BODY_ROWS + consts.SOLDIER_FEET_ROWS):
        for col in range(soldier_cell[1],
                         soldier_cell[1] + consts.SOLDIER_COLS):
            if game_board[row][col] == consts.MINE:
                return True
    return False



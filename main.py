import pygame

import consts
import game_field
import screen
import night_screen
import solider

state = {
    "is_window_open" : True,
    "state": consts.RUNNING_STATE,
}



def main():
    game_board = []
    game_field.create_board(game_board)
    game_field.set_flag_on_board(game_board)
    game_field.set_mines_on_board(game_board)

    while state["is_window_open"] and state["state"] == consts.RUNNING_STATE:
        screen.create_screen(state)
        player_touch_flag = game_field.is_touching_flag(game_board,solider.solider_place_tuple(solider.player))
        player_touch_mine = game_field.is_touching_mine(game_board, solider.solider_place_tuple(solider.player))
        if player_touch_mine:
            state["state"] = consts.LOSE_STATE
            print(state["state"])
        elif player_touch_flag:
            state["state"] = consts.WIN_STATE
            print(state["state"])


main()
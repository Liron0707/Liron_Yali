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
    mines_list = game_field.set_mines_on_board(game_board)
    print(mines_list)

    while state["is_window_open"] and state["state"] == consts.RUNNING_STATE:
        screen.create_screen()
        player_touch = game_field.is_touching_flag(game_board,solider.solider_place_tuple())
        if player_touch:
            state["state"] = consts.LOSE_STATE
            state["is_window_open"] = False

main()
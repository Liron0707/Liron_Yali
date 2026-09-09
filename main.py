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

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # user click the x button
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:  # key was pressed
            if event.key == pygame.K_UP and solider.player.y - consts.CELL_SIZE >= 0:
                solider.player.y -= consts.CELL_SIZE  # y is used to move objects
            if event.key == pygame.K_DOWN and solider.player.y + consts.PLAYER_HEIGHT + consts.CELL_SIZE <= consts.WINDOW_HEIGHT:
                solider.player.y += consts.CELL_SIZE
            if event.key == pygame.K_LEFT and solider.player.x - consts.CELL_SIZE >= 0:
                solider.player.x -= consts.CELL_SIZE
            if event.key == pygame.K_RIGHT and solider.player.x + consts.PLAYER_WIDTH + consts.CELL_SIZE <= consts.WINDOW_WIDTH:
                solider.player.x += consts.CELL_SIZE
            if event.key == pygame.K_SPACE:
                night_screen.create_screen()

def main():
    game_board = []
    game_field.create_board(game_board)
    game_field.set_flag_on_board(game_board)
    game_field.set_mines_on_board(game_board)

    while state["is_window_open"] and state["state"] == consts.RUNNING_STATE:
        event_handler()
        screen.create_screen(state)
        player_touch_mine = game_field.is_touching_mine(game_board, solider.solider_place_tuple(solider.player))
        player_touch_flag = game_field.is_touching_flag(game_board,solider.solider_place_tuple(solider.player))
        if player_touch_mine:
            print("mine")
            screen.draw_lose_message()
            state["state"] = consts.LOSE_STATE
        elif player_touch_flag:
            print("flag")
            screen.draw_win_message()
            state["state"] = consts.WIN_STATE


main()
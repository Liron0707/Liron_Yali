import consts
import game_field
import screen

state = {
    "is_window_open" : True,
    "state": consts.RUNNING_STATE,
}

def main():
    game_board = []
    game_field.create_board(game_board)

    while state["is_window_open"] and state["state"] == consts.RUNNING_STATE:
        screen.create_screen()

main()
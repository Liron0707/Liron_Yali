from codecs import backslashreplace_errors
from xml.dom.pulldom import PROCESSING_INSTRUCTION

import pygame
from sys import exit
import os
import consts
import game_field
import solider
import random

pygame.init()

window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("מפתיעים את ראש הממשלה")
clock = pygame.time.Clock()

mine_image = pygame.image.load(os.path.join("bin", "mine.PNG"))
mine_image = pygame.transform.scale(mine_image,
                                     (consts.MINE_WIDTH, consts.MINE_HEIGHT))


class Mine(pygame.Rect):
    def __init__(self, x, y, ):
        pygame.Rect.__init__(self, x, y, consts.MINE_WIDTH,
                             consts.MINE_HEIGHT)
        self.image = mine_image


# the func draw on the board the objects
def draw(mine_list):
    window.fill("pink")

    for row in range(consts.BOARD_ROWS):
        pygame.draw.line(window, "black", (0, row * consts.CELL_SIZE),
                         (consts.WINDOW_WIDTH, row * consts.CELL_SIZE))

    for col in range(consts.BOARD_COLS):
        pygame.draw.line(window, "black", (col * consts.CELL_SIZE, 0),
                         (col * consts.CELL_SIZE, consts.WINDOW_HEIGHT))

    draw_mines(mine_list)




def draw_mines(mine_list):
    for mine in mine_list:
        mine_to_screen= Mine(mine[1]*consts.CELL_SIZE, mine[0]*consts.CELL_SIZE)
        window.blit(mine_image, mine_to_screen)


def create_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # user click the x button
                pygame.quit()
                exit()


            draw(game_field.mine_list)
            pygame.display.update()
            # clock.tick(60)

from codecs import backslashreplace_errors
from xml.dom.pulldom import PROCESSING_INSTRUCTION

import pygame
from sys import exit
import os

import time

import consts
import night_screen
import solider
import random


pygame.init()

window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("מפתיעים את ראש הממשלה")
clock = pygame.time.Clock()

flag_image = pygame.image.load(os.path.join("bin", "sara.PNG"))
flag_image = pygame.transform.scale(flag_image,
                                    (consts.FLAG_WIDTH, consts.FLAG_HEIGHT))

spray_image = pygame.image.load(os.path.join("bin", "spray.PNG"))
spray_image = pygame.transform.scale(spray_image,
                                     (consts.GRASS_WIDTH, consts.GRASS_HEIGHT))



class Spray(pygame.Rect):
    def __init__(self, x, y, ):
        pygame.Rect.__init__(self, x, y, consts.GRASS_WIDTH,
                             consts.GRASS_HEIGHT)
        self.image = spray_image



# the func returns a list of tuples for where to put the "grass"
def choose_random_place_grass():
    places = []
    counter = 0
    while counter < consts.MINES_COUNT:
        row = random.randint(0 , consts.WINDOW_WIDTH)
        col = random.randint(0,consts.WINDOW_HEIGHT)
        while True:
            if row > consts.PLAYER_HEIGHT and col > consts.PLAYER_WIDTH and row < consts.WINDOW_WIDTH - consts.GRASS_HEIGHT and col < consts.WINDOW_HEIGHT - consts.GRASS_WIDTH and row != consts.WINDOW_WIDTH-consts.FLAG_WIDTH and col != consts.WINDOW_HEIGHT-consts.FLAG_HEIGHT:
                places.append((row, col))
                counter +=1
                break
            else:
                row = random.randint(0, consts.WINDOW_WIDTH)
                col = random.randint(0, consts.WINDOW_HEIGHT)
    return places


places = choose_random_place_grass()


# the func draw on the board the objects
def draw():
    window.fill("lightpink")
    window.blit(solider.player_image, solider.player)
    window.blit(flag_image, (consts.WINDOW_WIDTH - consts.FLAG_WIDTH,
                             consts.WINDOW_HEIGHT - consts.FLAG_HEIGHT))

    for i in places:
        spray = Spray(i[0], i[1])
        window.blit(spray_image, spray)


def draw_lose_message():
    lose_sound = pygame.mixer.Sound(
        "C:\\Users\jbt\PycharmProjects\Liron_Yali\sound\lose_sound.ogg")
    pygame.mixer.Sound.play(lose_sound)
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    win_sound = pygame.mixer.Sound(
            "C:\\Users\jbt\PycharmProjects\Liron_Yali\sound\win_sound.ogg")
    pygame.mixer.Sound.play(win_sound)
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    window.blit(text_img, location)
    pygame.display.update()
    time.sleep(5)


def create_screen(game_state):
        if game_state["state"] == consts.LOSE_STATE:
            draw_lose_message()
        if game_state["state"] == consts.WIN_STATE:
            draw_win_message()


        draw()
        pygame.display.update()
            # clock.tick(60)
            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_LEFT]:
            #     player.x -= consts.CELL_SIZE
            # if keys[pygame.K_RIGHT]:
            #     player.x += consts.CELL_SIZE
            # if keys[pygame.K_UP]:
            #     player.y -= consts.CELL_SIZE
            # if keys[pygame.K_DOWN]:
            #     player.y += consts.CELL_SIZE
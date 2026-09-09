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
            if row > consts.PLAYER_HEIGHT and col > consts.PLAYER_WIDTH and row < consts.WINDOW_WIDTH - consts.GRASS_HEIGHT and col < consts.WINDOW_HEIGHT - consts.GRASS_WIDTH:
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

def create_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # user click the x button
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:  # key was pressed
                if event.key == pygame.K_UP and solider.player.y -consts.CELL_SIZE>=0:
                    solider.player.y -= consts.CELL_SIZE  # y is used to move objects
                if event.key == pygame.K_DOWN and solider.player.y + consts.PLAYER_HEIGHT + consts.CELL_SIZE<=consts.WINDOW_HEIGHT:
                    solider.player.y += consts.CELL_SIZE
                if event.key == pygame.K_LEFT and solider.player.x -consts.CELL_SIZE>=0:
                    solider.player.x -= consts.CELL_SIZE
                if event.key == pygame.K_RIGHT and solider.player.x + consts.PLAYER_WIDTH+consts.CELL_SIZE<=consts.WINDOW_WIDTH:
                    solider.player.x += consts.CELL_SIZE
                if event.key == pygame.K_SPACE:
                    night_screen.create_screen()


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
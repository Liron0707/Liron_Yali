from codecs import backslashreplace_errors

import pygame
from sys import exit

import consts

pygame.init()

window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
player = pygame.Rect(50,50,consts.PLAYER_WIDTH,consts.PLAYER_HEIGHT) #pygame object for storing rectangular coordinates
pygame.display.set_caption("Yali and Liron for the win")
clock = pygame.time.Clock()



def draw():
    window.fill("lightpink")
    pygame.draw.rect(window,(71, 7, 7),player)

def create_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #user click the x button
                pygame.quit()
                exit()


            if event.type == pygame.KEYDOWN: #key was pressed
                if event.key == pygame.K_UP:
                    player.y -= consts.CELL_SIZE #y is used to move objects
                if event.key == pygame.K_DOWN:
                    player.y += consts.CELL_SIZE
                if event.key == pygame.K_LEFT:
                    player.x -= consts.CELL_SIZE
                if event.key == pygame.K_RIGHT:
                    player.x += consts.CELL_SIZE
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]:
        #     player.x -= consts.CELL_SIZE
        # if keys[pygame.K_RIGHT]:
        #     player.x += consts.CELL_SIZE
        # if keys[pygame.K_UP]:
        #     player.y -= consts.CELL_SIZE
        # if keys[pygame.K_DOWN]:
        #     player.y += consts.CELL_SIZE

            draw()
            pygame.display.update()
            clock.tick(60)


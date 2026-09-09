import pygame
from sys import exit
import os
import consts


player_image = pygame.image.load(os.path.join("bin","bibi.PNG"))
player_image = pygame.transform.scale(player_image, (consts.PLAYER_WIDTH, consts.PLAYER_HEIGHT))

pygame.display.set_icon(player_image)

class Player(pygame.Rect): #חייבת להבין מה קורה פה
    def __init__(self):
        pygame.Rect.__init__(self,0,0,consts.PLAYER_WIDTH,consts.PLAYER_HEIGHT) #pygame object for storing rectangular coordinates
        self.image = player_image

player = Player()

def solider_place_tuple(self):
    return self.x//20, self.y//20


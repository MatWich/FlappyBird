import pygame
from config import *

class Base:
    def __init__(self, y):
        self.image = BASE_IMG
        self.rect = self.image.get_rect()
        self.y = y
        self.imageWidth = self.image.get_width()

        # two bases
        self.x1 = 0
        self.x2 = self.imageWidth

    def move(self):
        self.x1 -= GAME_VEL
        self.x2 -= GAME_VEL

        # if first base is out of screen
        if self.x1 + self.imageWidth < 0:
            self.x1 = self.x2 + self.imageWidth
        
        # if second base is out of screen
        if self.x2 + self.imageWidth < 0:
            self.x2 = self.x1 + self.imageWidth
    
    def draw(self, screen):
        screen.blit(self.image, (self.x1, self.y))
        screen.blit(self.image, (self.x2, self.y))
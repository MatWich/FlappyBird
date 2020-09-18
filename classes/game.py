import pygame
pygame.init()
from config import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.run = True

    # method to call
    def mainLoop(self):
        while self.run:
            self.clock.tick(FPS)
            self.events()
            pygame.display.update()

    # setting up all game objects
    def setUp(self):
        pass

    # function contains eg. collision detection
    def events(self):
        self.drawBg()
        self.controls()
        

    """Drawings"""
    def drawBg(self):
        self.screen.blit(BG_IMGS[0], (0,0))

        # key controls
    def controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
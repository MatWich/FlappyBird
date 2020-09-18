import pygame
pygame.init()
from config import *
from classes.base import Base
from classes.bird import Bird

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.run = True

    # method to call
    def mainLoop(self):
        self.setUp()
        while self.run:
            self.clock.tick(FPS)
            self.events()
            pygame.display.update()

    # setting up all game objects
    def setUp(self):
        self.score = 0
        self.base = Base(BASE_Y)
        self.bird = Bird(int(WIDTH/2), int(HEIGHT/2))

    # function contains eg. collision detection
    def events(self):
        self.update()
        self.controls()
        self.movements()
        

    # this method will handle all obj movements
    def movements(self):
        # Base
        self.base.move()

    """Drawings"""
    def update(self):
        self.drawBg()
        self.drawBase()
        self.drawBird()

    def drawBird(self):
        self.bird.draw(self.screen)

    def drawBg(self):
        self.screen.blit(BG_IMGS[0], (0,0))

    def drawBase(self):
        self.base.draw(self.screen)

    # key controls
    def controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
import pygame

# Screen variables
SCREEN_SIZE = (WIDTH, HEIGHT) = (400, 600)
FPS = 60
TITLE = "Flappy Birdo"

BG_VEL = 1
BASE_Y = 530

"""IMGS"""
# BG
BG1 = pygame.transform.scale(pygame.image.load("imgs/background-day.png"), SCREEN_SIZE)
BG2 = pygame.transform.scale(pygame.image.load("imgs/background-night.png"), SCREEN_SIZE)
BG_IMGS = [BG1, BG2]

BASE_IMG = pygame.image.load("imgs/base.png")
BIRD_RED_IMGS = [pygame.image.load("imgs/redbird" + str(x) + ".png" ) for x in range(1, 3)]
BIRD_YELLOW_IMGS = [pygame.image.load("imgs/yellowbird" + str(x) + ".png" ) for x in range(1, 3)]
BIRD_BLUE_IMGS = [pygame.image.load("imgs/bluebird" + str(x) + ".png" ) for x in range(1, 3)]
PIPE_IMGS = [pygame.image.load("imgs/pipe-green.png"), pygame.image.load("imgs/pipe-green.png")]

# Menu
MENU_IMG = pygame.image.load("imgs/message.png")
GAME_OVER_IMG = pygame.image.load("imgs/gameover.png")
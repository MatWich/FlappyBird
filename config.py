import pygame

# Screen variables
SCREEN_SIZE = (WIDTH, HEIGHT) = (400, 600)
FPS = 60
TITLE = "Flappy Birdo"

GAME_VEL = 1
BASE_Y = 530

"""IMGS"""
# BG
BG1 = pygame.transform.scale(pygame.image.load("imgs/background-day.png"), SCREEN_SIZE)
BG2 = pygame.transform.scale(pygame.image.load("imgs/background-night.png"), SCREEN_SIZE)
BG_IMGS = [BG1, BG2]

BASE_IMG = pygame.image.load("imgs/base.png")
BIRD_RED_IMGS = [pygame.image.load("imgs/redbird" + str(x) + ".png" ) for x in range(1, 4)]
BIRD_YELLOW_IMGS = [pygame.image.load("imgs/yellowbird" + str(x) + ".png" ) for x in range(1, 4)]
BIRD_BLUE_IMGS = [pygame.image.load("imgs/bluebird" + str(x) + ".png" ) for x in range(1, 4)]

# Pipes
PipeWidth = 70
PipeHeight = HEIGHT - 100
PIPE_IMGS = [pygame.transform.scale(pygame.image.load("imgs/pipe-green.png"), (PipeWidth, PipeHeight)), pygame.image.load("imgs/pipe-green.png")]

# Bird
MAX_ROTATION = 25
ROTATION_VEL = 20
ANIMATION_TIME = 5

# Menu
MENU_IMG = pygame.image.load("imgs/message.png")
GAME_OVER_IMG = pygame.image.load("imgs/gameover.png")

'''
for i, phote in enumerate(BIRD_BLUE_IMGS):
    print(i)
    '''
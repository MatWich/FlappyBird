import pygame
from config import *

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tickCount = 0
        self.vel = 0
        self.height = self.y
        self.imgCount = 0
        self.imgs = BIRD_BLUE_IMGS
        self.image = self.imgs[0]

    def jump(self):
        self.vel = - 10.5
        self.tickCount = 0
        self.height = self.y

    def move(self):
        self.tickCount += 1

        displacemnt = self.vel * self.tickCount + 1.5 * self.tickCount**2

        if displacemnt >= 16:
            displacemnt = 16

        if displacemnt < 0:
            displacemnt -= 2
        
        self.y += displacemnt

        if displacemnt < 0 or self.y < self.height + 50:
            if self.tilt < MAX_ROTATION:
                self.tilt = MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= ROTATION_VEL

    def draw(self, win):
        self.imgCount += 1
        
        if self.imgCount < ANIMATION_TIME:
            self.image = self.imgs[0]
        elif self.imgCount < ANIMATION_TIME * 2:
            self.image = self.imgs[1]
        elif self.imgCount < ANIMATION_TIME * 3:
            self.image = self.imgs[2]
        elif self.imgCount < ANIMATION_TIME * 4:
            self.image = self.imgs[1]
        elif self.imgCount < ANIMATION_TIME * 4 + 1:
            self.image = self.imgs[0]
            self.imgCount = 0
        
        # zeby spadalo pod katem prostym
        if self.tilt <= -80:
            self.image = self.imgs[1]
            self.imgCount = ANIMATION_TIME*2

        rotated_img = pygame.transform.rotate(self.image, self.tilt)
        new_rect = rotated_img.get_rect(center=self.image.get_rect(topleft= (self.x, self.y)).center)
        win.blit(rotated_img, new_rect.topleft)

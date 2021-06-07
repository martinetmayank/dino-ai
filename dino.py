import pygame
import os
from time import sleep
DINO_IMG_PATH = 'img/dino'
DINO_IMG = [
    pygame.image.load(
        os.path.join(DINO_IMG_PATH, 'dino_1.png')
    ),
    pygame.image.load(
        os.path.join(DINO_IMG_PATH, 'dino_2.png')
    ),
    pygame.image.load(
        os.path.join(DINO_IMG_PATH, 'dino_3.png')
    ),
]

BASE = 0


class Dino:
    IMG = DINO_IMG
    ANIMATION_TIME = 5
    FACTOR = 0.7
    JUMPING = False
    FALLING = False

    def __init__(self, x) -> None:
        self.x = x
        self.image_count = 0
        self.tick_count = 0
        self.velocity = 0
        self.image = self.IMG[0]
        self.get_bottom_pos()

    def get_bottom_pos(self):
        global BASE
        mask = pygame.mask.from_surface(self.image)
        height = mask.get_size()
        self.bottom = 780 - height[1]
        BASE = 780 - height[1]

    def jump(self):
        self.velocity = -10
        self.tick_count = 0
        self.JUMPING = True
        print('JUMP TRIGGERED')

    def move(self):
        if self.JUMPING is True and self.FALLING is False:
            self.tick_count += 1
            displacement = (self.velocity*self.tick_count) + \
                (self.FACTOR * self.tick_count**2)

            if displacement < 0:
                self.bottom += displacement

            if displacement >= 0:
                self.tick_count = 0
                self.JUMPING = False
                self.FALLING = True

            print(f'jumping {self.bottom}, {displacement}')

        if self.JUMPING is False and self.FALLING is True:

            self.tick_count += 1
            displacement = (self.velocity*self.tick_count) + \
                (self.FACTOR * self.tick_count**2)

            if displacement < 0:
                self.bottom -= displacement

            if displacement >= 0:
                self.tick_count = 0
                self.bottom = BASE
                self.JUMPING = False
                self.FALLING = False
            print(f'falling {self.bottom}, {displacement}')

    def draw(self, window):
        self.image_count += 1

        if self.image_count % self.ANIMATION_TIME == 0:
            self.image = self.IMG[0]
        elif self.image_count % self.ANIMATION_TIME == 1:
            self.image = self.IMG[1]
        elif self.image_count % self.ANIMATION_TIME == 2:
            self.image = self.IMG[2]

        window.blit(self.image, (self.x, self.bottom))

    def get_mask(self):
        return pygame.mask.from_surface(self.image)

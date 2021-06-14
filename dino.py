import pygame
import os

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


class Dino:
    BASE = 780 - 94
    IMG = DINO_IMG
    ANIMATION_TIME = 5
    FACTOR = 0.7
    JUMPING = False
    FALLING = False
    CAN_JUMP = False
    LOCK_JUMP = False

    def __init__(self, x) -> None:
        self.x = x
        self.image_count = 0
        self.tick_count = 0
        self.velocity = 0
        self.image = self.IMG[0]
        self.get_bottom_pos()

    def get_bottom_pos(self):
        mask = pygame.mask.from_surface(self.image)
        height = mask.get_size()
        self.bottom = self.BASE

    def jump(self):
        self.velocity = -10
        self.tick_count = 0
        if self.CAN_JUMP is True:
            self.JUMPING = True
            self.CAN_JUMP = False

        if self.LOCK_JUMP is False:
            self.LOCK_JUMP = True
            self.CAN_JUMP = True
            self.JUMPING = True

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

        if self.JUMPING is False and self.FALLING is True:
            self.tick_count += 1
            displacement = (self.velocity*self.tick_count) + \
                (self.FACTOR * self.tick_count**2)

            if displacement < 0:
                self.bottom -= displacement

            if displacement >= 0:
                self.tick_count = 0
                self.bottom = self.BASE
                self.JUMPING = True
                self.FALLING = False

            if self.bottom > self.BASE:
                self.tick_count = 0
                self.bottom = self.BASE
                self.JUMPING = True
                self.FALLING = False

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

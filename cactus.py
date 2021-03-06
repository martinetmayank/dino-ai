import pygame
import os
import random

CACTUS_IMG_PATH = 'img/cactus'
CACTUS_IMG = [
    # pygame.image.load(
    #     os.path.join(CACTUS_IMG_PATH, 'group.png')
    # ),
    # pygame.image.load(
    #     os.path.join(CACTUS_IMG_PATH, 'large_1.png')
    # ),
    # pygame.image.load(
    #     os.path.join(CACTUS_IMG_PATH, 'large_2.png')
    # ),
    pygame.image.load(
        os.path.join(CACTUS_IMG_PATH, 'small_1.png')
    ),
    # pygame.image.load(
    #     os.path.join(CACTUS_IMG_PATH, 'small_2.png')
    # ),
    # pygame.image.load(
    #     os.path.join(CACTUS_IMG_PATH, 'small_3.png')
    # ),
]


class Cactus:
    IMG = CACTUS_IMG
    GAP = [200, 250, 300]
    VEL = 5

    def __init__(self, x) -> None:
        self.x = x
        self.bottom = 0
        self.passed = False
        self.width = 0
        self.height = 0
        self.get_img()
        self.get_bottom_pos()

    def move(self):
        self.x -= self.VEL

    def get_img(self):
        index = random.randint(0, len(self.IMG) - 1)
        self.image = self.IMG[index]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def get_bottom_pos(self):
        mask = pygame.mask.from_surface(self.image)
        height = mask.get_size()
        self.bottom = 780 - height[1]

    def draw(self, window):
        window.blit(self.image, (self.x, self.bottom))

    def collide(self, dino):
        dino_mask = dino.get_mask()
        cactus_mask = pygame.mask.from_surface(self.image)
        offset = (self.x - dino.x, self.bottom - round(dino.bottom))

        contact_point = dino_mask.overlap(cactus_mask, offset)

        if contact_point:
            return True

        return False

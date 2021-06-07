from dino import Dino
from cactus import Cactus
from ground import Ground
import pygame
import os


WIN_WIDTH = 1000
WIN_HEIGHT = 800
FLOOR = 770
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

BG_IMG = pygame.transform.scale2x(
    pygame.image.load(
        os.path.join('img', 'bg.png')
    )
)


def draw_window(window, ground, dinos, cactuses):
    window.blit(BG_IMG, (0, 0))

    ground.draw(window)

    for cactus in cactuses:
        cactus.draw(window)

    for dino in dinos:
        dino.draw(window)

    pygame.display.update()


def main():
    ground = Ground(FLOOR)
    cactuses = [Cactus(700)]
    dinos = [Dino(100)]
    i = 0
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        i += 1
        for dino in dinos:
            dino.move()
            if i == 80:
                dino.jump()
            # print(dino.bottom)

        ground.move()

        for cactus in cactuses:
            cactus.move()

        draw_window(WIN, ground, dinos, cactuses)


if __name__ == "__main__":
    main()

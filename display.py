import pygame
import os

WIN_WIDTH = 1000

BG_IMG = pygame.transform.scale2x(
    pygame.image.load(
        os.path.join('img', 'bg.png')
    )
)

pygame.font.init()
SCORE_FONT = pygame.font.SysFont('comicsans', 50)


def draw_window(window, ground, dinos, cactuses, score, gen):
    window.blit(BG_IMG, (0, 0))

    ground.draw(window)

    for cactus in cactuses:
        cactus.draw(window)

    for dino in dinos:
        dino.draw(window)

    text = SCORE_FONT.render(f'Score {score}', 1, (0, 0, 255))
    window.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    curr_gen = SCORE_FONT.render(f'Generation {gen}', 1, (255, 0, 255))
    window.blit(curr_gen, (10, 10))

    current_pop = SCORE_FONT.render(
        f'Current Population {len(dinos)}', 1, (0, 255, 0))
    window.blit(current_pop, (10, 50))

    pygame.display.update()

from dino import Dino
from cactus import Cactus
from ground import Ground
from display import draw_window

import pygame
import neat

WIN_WIDTH = 1000
WIN_HEIGHT = 800
FLOOR = 770
GEN = 0

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


def eval_genomes(genomes, config):
    global GEN
    GEN += 1

    nets = []
    ge = []
    dinos = []

    cactuses = [Cactus(700)]
    ground = Ground(FLOOR)
    score = 0

    clock = pygame.time.Clock()

    for _, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        dinos.append(Dino(100))
        ge.append(genome)

    run = True
    while run and len(dinos):
        clock.tick(1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        cactus_index = 0
        if len(dinos) > 0:
            if len(cactuses) > 1 and dinos[0].x > cactuses[0].x + cactuses[0].width:
                cactus_index = 1

        # TO CHECK HERE FOR NEURAL NETWORK
        for x, dino in enumerate(dinos):
            ge[x].fitness += 0.1
            dino.move()
            output = nets[dinos.index(dino)].activate((
                dino.bottom,
                abs(dino.bottom - cactuses[cactus_index].bottom)
            ))

            if output[0] > 0.8:
                dino.jump()

        ground.move()

        add_cactus = False
        rem = []
        for cactus in cactuses:
            cactus.move()

            for dino in dinos:

                if cactus.collide(dino):
                    ge[dinos.index(dino)].fitness -= 1
                    nets.pop(dinos.index(dino))
                    ge.pop(dinos.index(dino))
                    dinos.pop(dinos.index(dino))

                if not cactus.passed and cactus.x < dino.x:
                    cactus.passed = True
                    add_cactus = True

            if cactus.x + cactus.width < 0:
                rem.append(cactus)

        if add_cactus:
            score += 1
            for genome in ge:
                genome.fitness += 1
            cactuses.append(Cactus(700))

        for r in rem:
            cactuses.remove(r)

        for dino in dinos:
            if dino.bottom - dino.image.get_height() <= 0:
                nets.pop(dinos.index(dino))
                ge.pop(dinos.index(dino))
                dinos.pop(dinos.index(dino))

        draw_window(WIN, ground, dinos, cactuses, score, GEN)

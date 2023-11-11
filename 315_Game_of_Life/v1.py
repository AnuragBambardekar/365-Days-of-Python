import pygame
from random import randint
from copy import deepcopy

RES = WIDTH, HEIGHT = 1600,900
TILE = 20 # 50
W,H = WIDTH//TILE, HEIGHT//TILE
FPS = 10

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

next_field = [[0 for i in range(W)] for j in range(H)]
current_field = [[randint(0,1) for i in range(W)] for j in range(H)]

def check_cell(current_field, x, y):
    count = 0
    for j in range(y-1, y+2):
        for i in range(x-1, x+2):
            if current_field[j][i]:
                count += 1

    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1 # alive
        return 0 # dead
    else:
        if count == 3:
            return 1 # alive
        return 0 # dead

while True:
    surface.fill(pygame.Color('black'))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    # Draw Grid
    [pygame.draw.line(surface, pygame.Color('darkslategray'),(x,0),(x,HEIGHT)) for x in range(0, WIDTH, TILE)]
    [pygame.draw.line(surface, pygame.Color('dimgray'),(0,y),(WIDTH, y)) for y in range(0, HEIGHT, TILE)]

    # Draw life
    for x in range(1, W-1):
        for y in range(1, H-1):
            if current_field[y][x]:
                pygame.draw.rect(surface, pygame.Color('forestgreen'), (x*TILE+2, y*TILE+2, TILE-2, TILE-2))
            next_field[y][x] = check_cell(current_field, x, y)
    current_field = deepcopy(next_field)



    pygame.display.flip()
    clock.tick(FPS)
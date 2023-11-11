# Gliders

# using numba to accelerate
# rule-based game of life - instead of random assignments

import pygame
from random import randint, randrange
from copy import deepcopy
import numpy as np
from numba import njit

RES = WIDTH, HEIGHT = 1600,900
TILE = 5
W,H = WIDTH//TILE, HEIGHT//TILE
FPS = 0

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

next_field = np.array([[0 for i in range(W)] for j in range(H)])
current_field = np.array([[0 for i in range(W)] for j in range(H)])

def set_glider_SE(current_field, x, y):
    pos = [(x,y),(x+1,y+1),(x-1,y-2),(x,y+2),(x-1,y+2)]
    for i,j in pos:
        current_field[j][i]=1
    return current_field

def set_glider_NW(current_field, x, y):
    pos = [(x,y),(x-2,y-1),(x-2,y),(x-2,y+1),(x-1,y-1)]
    for i,j in pos:
        current_field[j][i]=1
    return current_field

for _ in range(500):
    i0,j0 = randrange(TILE, W//2 + W//4, TILE), randrange(TILE, H//2)
    current_field = set_glider_SE(current_field, i0, j0)
    i1,j1 = randrange(W//2 - W//4, W - TILE), randrange(H//2, H - TILE)
    current_field = set_glider_NW(current_field, i1, j1)

@njit(fastmath=True)
def check_cells(current_field, next_field):
    res=[]

    for x in range(1, W-1):
        for y in range(H): # 1, H-1
            count=0
            for j in range(y-1, y+2):
                for i in range(x-1, x+2):
                    if current_field[j%H][i%W]==1: # if current_field[j][i]==1:
                        count +=1
            if current_field[y][x] == 1:
                count -=1
                if count == 2 or count == 3:
                    next_field[y][x]=1
                    res.append((x,y))
                else:
                    next_field[y][x]=0
            else:
                if count == 3:
                    next_field[y][x]=1
                    res.append((x,y))
                else:
                    next_field[y][x] = 0
    return next_field, res



# def check_cell(current_field, x, y):
#     count = 0
#     for j in range(y-1, y+2):
#         for i in range(x-1, x+2):
#             if current_field[j][i]:
#                 count += 1

#     if current_field[y][x]:
#         count -= 1
#         if count == 2 or count == 3:
#             return 1 # alive
#         return 0 # dead
#     else:
#         if count == 3:
#             return 1 # alive
#         return 0 # dead

while True:
    surface.fill(pygame.Color('black'))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                exit()

    # Draw Grid
    # [pygame.draw.line(surface, pygame.Color('darkslategray'),(x,0),(x,HEIGHT)) for x in range(0, WIDTH, TILE)]
    # [pygame.draw.line(surface, pygame.Color('dimgray'),(0,y),(WIDTH, y)) for y in range(0, HEIGHT, TILE)]

    # Draw life
    # for x in range(1, W-1):
    #     for y in range(1, H-1):
    #         if current_field[y][x]:
    #             pygame.draw.rect(surface, pygame.Color('orange'), (x*TILE+2, y*TILE+2, TILE-2, TILE-2))
    #         next_field[y][x] = check_cell(current_field, x, y)
    # current_field = deepcopy(next_field)

    # Draw life
    next, res = check_cells(current_field, next_field)
    [pygame.draw.rect(surface, pygame.Color('darkorange'), (x*TILE+1, y*TILE+1, TILE-1, TILE-1)) for x,y in res]
    current_field = deepcopy(next_field)

    pygame.display.flip()
    clock.tick(FPS)
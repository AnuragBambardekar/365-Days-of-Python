# using numba to accelerate
# rule-based game of life - instead of random assignments

import pygame
from random import randint
from copy import deepcopy
import numpy as np
from numba import njit

RES = WIDTH, HEIGHT = 1600,900
TILE = 5
W,H = WIDTH//TILE, HEIGHT//TILE
FPS = -1

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

next_field = np.array([[0 for i in range(W)] for j in range(H)])
# current_field = [[randint(0,1) for i in range(W)] for j in range(H)]
# current_field = [[1 if not i%33 else 0 for i in range(W)] for j in range(H)]
# current_field = [[1 if not (4*i+j)%4 else 0 for i in range(W)] for j in range(H)]
# current_field = np.array([[1 if not (i*j)%22 else 0 for i in range(W)] for j in range(H)])
# current_field = np.array([[0 for i in range(W)] for j in range(H)])
# for i in range(H):
#     current_field[i][i+(W-H)//2] = 1
#     current_field[H-i-1][i+(W-H)//2] = 1
current_field = np.array([[1 if i ==W//2 or j==H//2 else 0 for i in range(W)] for j in range(H)])



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
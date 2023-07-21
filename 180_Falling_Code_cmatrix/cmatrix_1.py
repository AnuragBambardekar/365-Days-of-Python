import os
import pygame as pg
from random import choice, randrange


class Symbol:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.value = choice(green_symbols)
        self.interval = randrange(5, 30) # because we dont want static characters

    def draw(self): # draw symbols at random intervals
        frames = pg.time.get_ticks()
        if not frames % self.interval:
            self.value = choice(green_symbols)
        surface.blit(self.value, (self.x, self.y))


RES = WIDTH, HEIGHT = 1600, 900
FONT_SIZE = 140


pg.init() #initialize pygame module
surface = pg.display.set_mode(RES)
clock = pg.time.Clock() # to set the number of frames

symbols = [chr(int('0x30a0', 16) + i) for i in range(96)]

font = pg.font.Font('180_Falling_Code_cmatrix/MS Mincho.ttf', FONT_SIZE, bold=True) # font is MS Micho
green_symbols = [font.render(char, True, pg.Color('green')) for char in symbols]

symbol = Symbol(WIDTH//2 - FONT_SIZE//2, HEIGHT//2 - FONT_SIZE//2)

while True:
    surface.fill(pg.Color('black'))

    symbol.draw()

    [exit() for i in pg.event.get() if i.type == pg.QUIT]
    pg.display.flip()
    clock.tick(60) # 60fps
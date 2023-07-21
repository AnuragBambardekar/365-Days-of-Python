import os
import pygame as pg
from random import choice, randrange


class Symbol:
    def __init__(self, x, y, speed):
        self.x, self.y = x, y
        self.speed = speed
        self.value = choice(green_symbols)
        self.interval = randrange(5, 30) # because we dont want static characters

    def draw(self): # draw symbols at random intervals
        frames = pg.time.get_ticks()
        if not frames % self.interval:
            self.value = choice(green_symbols)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE
        surface.blit(self.value, (self.x, self.y))

class SymbolColumn:
    def __init__(self, x, y):
        self.column_height = randrange(8, 24)
        self.speed = randrange(3, 7)
        self.symbols = [Symbol(x, i, self.speed) for i in range(y, y - FONT_SIZE * self.column_height, -FONT_SIZE)]

    def draw(self):
        [symbol.draw() for symbol in self.symbols]

RES = WIDTH, HEIGHT = 1600, 900
FONT_SIZE = 50


pg.init() #initialize pygame module
surface = pg.display.set_mode(RES)
clock = pg.time.Clock() # to set the number of frames

symbols = [chr(int('0x30a0', 16) + i) for i in range(96)]

font = pg.font.Font('180_Falling_Code_cmatrix/MS Mincho.ttf', FONT_SIZE, bold=True) # font is MS Micho
green_symbols = [font.render(char, True, pg.Color('green')) for char in symbols]

symbol_column = SymbolColumn(WIDTH//2 - FONT_SIZE//2, HEIGHT//2 - FONT_SIZE//2)

while True:
    surface.fill(pg.Color('black'))

    symbol_column.draw()

    [exit() for i in pg.event.get() if i.type == pg.QUIT]
    pg.display.flip()
    clock.tick(60) # 60fps
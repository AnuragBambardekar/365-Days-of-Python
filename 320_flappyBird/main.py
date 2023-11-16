import pygame
from pygame.locals import *

# initialization
pygame.init()
clock = pygame.time.Clock()
fps =60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

# define game variables
ground_scroll = 0
scroll_speed = 4 # 4 pixels
flying = False
game_over = False

# load images
bg = pygame.image.load('img/bg.png')
ground_img = pygame.image.load('img/ground.png')

# Add bird
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1,4):
            img = pygame.image.load(f'img/bird{num}.png')
            self.images.append(img)

        self.image = self.images[self.index]
        # self.image = pygame.image.load('img/bird1.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

        # velocity
        self.vel = 0

        # single mouse click
        self.clicked = False

    def update(self):

        if flying == True:
            # increase velocity
            self.vel += 0.5
            # add limit - gravity
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)
        
        if game_over == False:
            # jumping on click mouse event and release
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # left click
                # give negative velocity
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            # update bird - handle the animation
            self.counter += 1
            flap_cooldown = 5

            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            # rotate the bird relative to velocity
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
        else:
            # bird is dead
            self.image = pygame.transform.rotate(self.images[self.index], -90)

bird_group = pygame.sprite.Group()
flappy = Bird(100, int(screen_height/2))
bird_group.add(flappy)

# Run Game
run = True
while run:
    # Run at 60 fps
    clock.tick(fps)

    # draw background
    screen.blit(bg, (0,0))

    # add bird
    bird_group.draw(screen)
    bird_group.update()

    # draw the ground
    screen.blit(ground_img, (ground_scroll, 768))

    # bird collision with ground?
    if flappy.rect.bottom > 768:
        game_over = True
        flying = False

    if game_over == False:
        # draw and scroll the ground
        # screen.blit(ground_img, (ground_scroll, 768))
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over==False:
            flying = True

    pygame.display.update()

pygame.quit()
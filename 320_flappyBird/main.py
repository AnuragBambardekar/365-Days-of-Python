import pygame
from pygame.locals import *
import random

# initialization
pygame.init()
clock = pygame.time.Clock()
fps =60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

# font and color
font = pygame.font.SysFont('Bauhaus 93', 60)
white = (255,255,255)

# define game variables
ground_scroll = 0
scroll_speed = 4 # 4 pixels
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 1500 # in milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

# load images
bg = pygame.image.load('img/bg.png')
ground_img = pygame.image.load('img/ground.png')
button_img = pygame.image.load('img/restart.png')

# Add text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

# Reset Game
def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_height/2)
    score = 0
    return score

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

# Add pipes
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/pipe.png')
        self.rect = self.image.get_rect()

        # position 1 is from the top, -1 is from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x,y - int(pipe_gap/2)]
        if position == -1:
            self.rect.topleft = [x,y + int(pipe_gap/2)]
        # self.rect.topleft = [x,y] 

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0: # < 200 to check pipe being killed
            self.kill()

# Button
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        action = False
        
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check if mouse is over the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        # Draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height/2))
bird_group.add(flappy)

# bottom_pipe = Pipe(300, int(screen_height/2), -1)
# top_pipe = Pipe(300, int(screen_height/2), 1)
# pipe_group.add(bottom_pipe)
# pipe_group.add(top_pipe)

# create restart button instance
button = Button(screen_width//2-50, screen_height//2-100, button_img)

# Run Game - Main game loop
run = True
while run:
    # Run at 60 fps
    clock.tick(fps)

    # draw background
    screen.blit(bg, (0,0))

    # add bird
    bird_group.draw(screen)
    bird_group.update()

    # add pipe
    pipe_group.draw(screen)
    # pipe_group.update()

    # draw the ground
    screen.blit(ground_img, (ground_scroll, 768))

    # check the score
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and pass_pipe==False:
            pass_pipe = True
        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False
    # print(score)

    draw_text(str(score), font, white, int(screen_width/2), 20)

    # look for collision with pipe
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        game_over = True

    # bird collision with ground?
    if flappy.rect.bottom >= 768:
        game_over = True
        flying = False

    if game_over == False and flying == True:
        # generate new pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            # random pipes
            pipe_height = random.randint(-100,100)

            bottom_pipe = Pipe(screen_width, int(screen_height/2) + pipe_height, -1)
            top_pipe = Pipe(screen_width, int(screen_height/2) + pipe_height, 1)
            pipe_group.add(bottom_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

        # draw and scroll the ground
        # screen.blit(ground_img, (ground_scroll, 768))
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0
        pipe_group.update()

    # check for game over and reset
    if game_over == True:
        if button.draw() == True:
            # print("Clicked")
            game_over = False
            score = reset_game()


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over==False:
            flying = True

    pygame.display.update()

pygame.quit()
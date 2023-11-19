import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Initialize ball, paddles, and scores
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [3, 3]

left_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

paddle_speed = 5

left_score = 0
right_score = 0
font = pygame.font.Font(None, 36)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += paddle_speed

    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += paddle_speed

    # Move the ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Bounce the ball off the walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Bounce the ball off the paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed[0] = -ball_speed[0]

    # Check for scoring
    if ball.left <= 0:
        right_score += 1
        ball.x = WIDTH // 2 - BALL_RADIUS
        ball_speed[0] = -ball_speed[0]
    elif ball.right >= WIDTH:
        left_score += 1
        ball.x = WIDTH // 2 - BALL_RADIUS
        ball_speed[0] = -ball_speed[0]

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)

    # Draw scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (3 * WIDTH // 4 - right_text.get_width(), 20))

    # Update the display
    pygame.display.flip()

    # Check for game over and restart
    if left_score >= 5 or right_score >= 5:
        pygame.time.delay(2000)  # Pause for 2 seconds
        left_score = 0
        right_score = 0

    # Set the frames per second
    pygame.time.Clock().tick(60)

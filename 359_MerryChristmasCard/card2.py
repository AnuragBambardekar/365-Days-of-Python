import turtle
import random
import time

# Constants
WIDTH, HEIGHT = 500, 500
SNOWBALL_RATE = (1, 3)
SNOWBALL_SIZE = (5, 15)
WIND_CHANGE = (1, 5)
MAX_WIND = 3
BUTTON_SEPARATION = 25
Y_OFFSET = 10
X_SEPARATION = 15

# Set up the window
window = turtle.Screen()
window.setup(WIDTH, HEIGHT)
window.bgcolor("sky blue")
window.title("Happy Holidays")

# Lists
list_of_snowballs = []

# Create circle-shaped objects
def make_circle(turtle_name, x, y, size, color):
    turtle_name.color(color)
    turtle_name.penup()
    turtle_name.setposition(x, y)
    turtle_name.dot(size)

# Create new snowballs and store in the list
def make_snowball():
    snowball = turtle.Turtle()
    snowball.color("white")
    snowball.penup()
    snowball.setposition(random.randint(-2 * WIDTH, WIDTH / 2), HEIGHT / 2)
    snowball.hideturtle()
    snowball.size = random.randint(*SNOWBALL_SIZE)
    list_of_snowballs.append(snowball)

# Move snowball
def move_snowball(turtle_name, falling_speed=1, wind=0):
    turtle_name.clear()
    turtle_name.sety(turtle_name.ycor() - falling_speed)
    if wind:
        turtle_name.setx(turtle_name.xcor() + wind)
    turtle_name.dot(turtle_name.size)

# Ground
def draw_ground():
    grass = turtle.Turtle()
    grass.fillcolor("forest green")
    grass.penup()
    grass.setposition(-WIDTH / 2, -HEIGHT / 2)
    grass.begin_fill()
    for _ in range(2):
        grass.forward(WIDTH)
        grass.left(90)
        grass.forward(70)
        grass.left(90)
    grass.end_fill()

    ground = turtle.Turtle()
    for x in range(int(-WIDTH / 2), int(WIDTH / 2), int(WIDTH / 200)):
        make_circle(ground, x, -180, random.randint(5, 20), "white")

# Snowman
def draw_snowman():
    snowman = turtle.Turtle()
    x_position = 0
    y_positions = [75, 0, -100]
    size = 75

    for y in y_positions:
        make_circle(snowman, x_position, y, size, "white")
        size = size * 1.5

    button_y_positions = [y_positions[1] - BUTTON_SEPARATION,
                          y_positions[1],
                          y_positions[1] + BUTTON_SEPARATION]
    for y in button_y_positions:
        make_circle(snowman, x_position, y, 10, "black")

    for x in [x_position - X_SEPARATION, x_position + X_SEPARATION]:
        make_circle(snowman, x, y_positions[0] + Y_OFFSET, 20, "green")
        make_circle(snowman, x, y_positions[0] + Y_OFFSET, 10, "black")

    snowman.color("orange")
    snowman.setposition(x_position - 10, y_positions[0] - Y_OFFSET)
    snowman.shape("triangle")
    snowman.setheading(200)
    snowman.turtlesize(0.5, 2.5)

# Display text
def display_text():
    text = turtle.Turtle()
    text.color("red")
    text.penup()
    text.setposition(0, 170)
    text.write("Happy Holidays 2023!!", font=("Apple Chancery", 30, "bold"), align="center")
    text.hideturtle()

# Main function
def main():
    window.tracer(0)

    draw_ground()
    draw_snowman()
    display_text()

    time_delay = 0
    start_time = time.time()
    wind = 0
    wind_delay = 5
    wind_timer = time.time()
    wind_step = 0.1

    while True:
        if time.time() - start_time > time_delay:
            make_snowball()
            start_time = time.time()
            time_delay = random.randint(*SNOWBALL_RATE) / 10

        for snowball in list_of_snowballs:
            move_snowball(snowball, wind=wind)
            if snowball.ycor() < -HEIGHT / 2:
                snowball.clear()
                list_of_snowballs.remove(snowball)

        if time.time() - wind_timer > wind_delay:
            wind += wind_step
            if wind >= MAX_WIND:
                wind_step = -wind_step
            elif wind <= 0:
                wind_step = abs(wind_step)

            wind_timer = time.time()
            wind_delay = random.randint(*WIND_CHANGE) / 10

        window.update()

    turtle.done()

if __name__ == "__main__":
    main()

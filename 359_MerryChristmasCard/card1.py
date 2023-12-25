# from turtle import *
# from random import randint


# def create_rectangle(turtle, color, x, y, width, height):
#     turtle.penup()
#     turtle.color(color)
#     turtle.fillcolor(color)
#     turtle.goto(x, y)
#     turtle.pendown()
#     turtle.begin_fill()

#     turtle.forward(width)
#     turtle.left(90)
#     turtle.forward(height)
#     turtle.left(90)
#     turtle.forward(width)
#     turtle.left(90)
#     turtle.forward(height)
#     turtle.left(90)

#     # fill the above shape
#     turtle.end_fill()
#     # Reset the orientation of the turtle
#     turtle.setheading(0)


# def create_circle(turtle, x, y, radius, color):
#     oogway.penup()
#     oogway.color(color)
#     oogway.fillcolor(color)
#     oogway.goto(x, y)
#     oogway.pendown()
#     oogway.begin_fill()
#     oogway.circle(radius)
#     oogway.end_fill()



# oogway = Turtle()
# # set turtle speed
# oogway.speed(2)
# screen = oogway.getscreen()
# # set background color
# screen.bgcolor(BG_COLOR)
# # set tile of screen
# screen.title("Merry Christmas")
# # maximize the screen
# screen.setup(width=1.0, height=1.0)

# y = -100
# # create tree trunk
# create_rectangle(oogway, "red", -15, y-60, 30, 60)

# # create tree
# width = 240
# oogway.speed(10)
# while width > 10:
#     width = width - 10
#     height = 10
#     x = 0 - width/2
#     create_rectangle(oogway, "green", x, y, width, height)
#     y = y + height

# # create a star a top of tree
# oogway.speed(1)
# oogway.penup()
# oogway.color('yellow')
# oogway.goto(-20, y+10)
# oogway.begin_fill()
# oogway.pendown()
# for i in range(5):
#     oogway.forward(40)
#     oogway.right(144)
# oogway.end_fill()

# tree_height = y + 40

# # create moon in sky
# # create a full circle
# create_circle(oogway, 230, 180, 60, "white")
# # overlap with full circle of BG color to make a crescent shape
# create_circle(oogway, 220, 180, 60, BG_COLOR)

# # now add few stars in sky
# oogway.speed(10)
# number_of_stars = randint(20,30)
# # print(number_of_stars)
# for _ in range(0,number_of_stars):
#     x_star = randint(-(screen.window_width()//2),screen.window_width()//2)
#     y_star = randint(tree_height, screen.window_height()//2)
#     size = randint(5,20)
#     oogway.penup()
#     oogway.color('white')
#     oogway.goto(x_star, y_star)
#     oogway.begin_fill()
#     oogway.pendown()
#     for i in range(5):
#         oogway.forward(size)
#         oogway.right(144)
#     oogway.end_fill()

# # print greeting message
# oogway.speed(1)
# oogway.penup()
# msg = "Merry Christmas 2023!!"
# oogway.goto(0, -200)  # y is in minus because tree trunk was below x axis
# oogway.color("white")
# oogway.pendown()
# oogway.write(msg, move=False, align="center", font=("Arial", 15, "bold"))

# oogway.hideturtle()
# screen.mainloop()

from turtle import *
from random import randint

def create_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()
    turtle.setheading(0)

def create_circle(turtle, x, y, radius, color):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_star(turtle, x, y, size):
    turtle.penup()
    turtle.color('white')
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.pendown()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

def main():
    BG_COLOR = "#000000"
    screen = Screen()
    screen.bgcolor(BG_COLOR)
    screen.title("Merry Christmas")
    screen.setup(width=1.0, height=1.0)

    oogway = Turtle()
    oogway.speed(2)

    draw_tree(oogway)
    draw_moon(oogway)
    draw_stars(oogway)

    oogway.hideturtle()
    screen.mainloop()

def draw_tree(turtle):
    trunk_height = 60
    create_rectangle(turtle, "red", -15, -160, 30, trunk_height)

    tree_height = -100
    width = 240
    turtle.speed(10)
    while width > 10:
        width -= 10
        height = 10
        x = 0 - width/2
        create_rectangle(turtle, "green", x, tree_height, width, height)
        tree_height += height

    draw_star(turtle, -20, tree_height + 10, 40)

def draw_moon(turtle):
    BG_COLOR = "#000000"
    create_circle(turtle, 230, 180, 60, "white")
    create_circle(turtle, 220, 180, 60, BG_COLOR)

def draw_stars(turtle):
    turtle.speed(10)
    number_of_stars = randint(20, 30)

    for _ in range(number_of_stars):
        x_star = randint(-300, 300)
        y_star = randint(-100, 250)
        size = randint(5, 20)
        draw_star(turtle, x_star, y_star, size)

    turtle.penup()
    turtle.color("white")
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.write("Merry Christmas 2023!!", move=False, align="center", font=("Arial", 15, "bold"))

if __name__ == "__main__":
    main()

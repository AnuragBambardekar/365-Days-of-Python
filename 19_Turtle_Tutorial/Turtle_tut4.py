import turtle as t
import random
t.color("white","yellow")

def draw_square(size):
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)

t.getscreen().bgcolor("black")
t.speed(5)

def draw_star(size):
    for _ in range(5):
        t.forward(size)
        t.left(216)

for _ in range(50):
    x,y = random.randint(-300,300),random.randint(-300,300) # center of screen is -ve, we go up and left is -ve
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    draw_star(random.randint(5, 25))
    t.end_fill()


#Clear the screen
t.clear()

#set heading
t.setheading(90)



t.done()
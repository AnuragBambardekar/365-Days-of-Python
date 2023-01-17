import turtle as t
import random
t.color("white","yellow")

t.getscreen().bgcolor("black")
t.speed(5)

def draw_star(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("red","yellow")
    t.begin_fill()

    for _ in range(36):
        t.forward(150)
        t.left(170)

    t.end_fill()

t.speed(100)

draw_star(0,0)

t.done()
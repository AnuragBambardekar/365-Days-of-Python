import turtle as t
t.color("orange","green")

def draw_square(size):
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)

t.begin_fill()
draw_square(200)
t.end_fill()

t.penup()
t.forward(100)
t.pendown()

t.begin_fill()
draw_square(200)
t.end_fill()


t.done()
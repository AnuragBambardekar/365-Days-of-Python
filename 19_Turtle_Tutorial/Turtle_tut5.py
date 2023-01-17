import turtle as t
t.color("black","yellow")

t.begin_poly()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_poly()

square = t.get_poly() #save/define the shape
t.register_shape("Square", square)

#Draw the defined shape
t.penup()
t.goto(-100, -100)
t.pendown()
t.shape("square")


t.done()
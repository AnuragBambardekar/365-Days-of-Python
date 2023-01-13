import turtle as t

colors =["red","yellow","green","blue","violet","orange"]
t.getscreen().bgcolor("black")
t.speed(5000)

for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)

t.done()
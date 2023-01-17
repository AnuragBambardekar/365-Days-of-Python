import turtle as t
t.Screen().bgcolor('black') # background color of the turtle screen is set to black
t.speed(5) # turtle speed is set to 5
t.begin_fill()
t.fillcolor('#1DB954') # spotify green color
t.pencolor('#1DB954')
t.pensize(0)
t.circle(100) # circle of radius 100
t.end_fill()
t.penup()
t.goto(40,50) #goto new position
t.pendown()
t.lt(150) #turn left by 150 degrees
t.fd(0) #move forward by 0 units
t.pensize(15) #pensize 15 to draw the stripes
t.pencolor('black')
t.circle(80,60) #circle of radius 80 and angle 60 degrees
t.penup()

#repeat for stripe at new location
t.goto(50,85) #goto new position
t.pendown()
t.pensize(17)
t.rt(60)
t.fd(0)
t.circle(100,60)

#repeat for stripe at new location
t.penup()
t.goto(60,120)
t.pendown()
t.pensize(20)
t.rt(60)
t.fd(0)
t.circle(120,60)

t.hideturtle()
t.done()
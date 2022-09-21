import turtle
import math

turtle.penup()
turtle.goto(0,-150)
turtle.pendown()

turtle.width(8)
turtle.color('green')

for i in range(2,10):
    if i % 2 == 0:
        turtle.penup()
        turtle.circle(150,45)
    if i % 2 != 0:
        turtle.pendown()
        turtle.circle(150, 45)

turtle.goto(0,150)

turtle.penup()
turtle.goto(-150,0)
turtle.pendown()
turtle.goto(150,0)

turtle.penup()
turtle.goto(-150/math.sqrt(2),150/math.sqrt(2))
turtle.pendown()
turtle.goto(150/math.sqrt(2),-150/math.sqrt(2))

turtle.penup()
turtle.goto(150/math.sqrt(2),150/math.sqrt(2))
turtle.pendown()
turtle.goto(-150/math.sqrt(2),-150/math.sqrt(2))

turtle.done()
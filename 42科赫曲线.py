
import turtle

def Koch_Line(size,n):
    if n==0:
        turtle.forward(size)
    else:
        for xita in [0,60,-120,60]:
            turtle.left(xita)
            Koch_Line(size/3,n-1)

def Koch_Snow(size,n):
    turtle.seth(60)
    for i in range(3):
        Koch_Line(size,n)
        turtle.right(120)

turtle.speed(0)
Koch_Snow(300,3)
turtle.done()





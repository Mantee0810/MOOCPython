import turtle

def Ting_Line(size,n):
    if n==1:
        turtle.fd(size)
    else:
        Ting_Line(size/2,n-1)
        turtle.right(90)
        Ting_Line(size / 2, n - 1)
        turtle.left(90)
        Ting_Line(size / 2, n - 1)
        turtle.left(90)
        Ting_Line(size / 2, n - 1)
        turtle.right(90)
        Ting_Line(size / 2, n - 1)

turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
turtle.speed(0)
Ting_Line(200,4)




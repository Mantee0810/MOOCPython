
import time
import turtle

def Draw_Gap():
    turtle.penup()
    turtle.forward(6)
    turtle.pendown()

def Draw_line(draw):
    Draw_Gap()
    if draw:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.forward(40)
    Draw_Gap()
    turtle.right(90)


def Draw_Single_Tube(num):
    if num in [2,3,4,5,6,8,9]:
        Draw_line(1)
    else:
        Draw_line(0)

    if num in [0,1,3,4,5,6,7,8,9]:
        Draw_line(1)
    else:
        Draw_line(0)

    if num in [0,2,3,5,6,8,9]:
        Draw_line(1)
    else:
        Draw_line(0)

    if num in [0,2,6,8]:
        Draw_line(1)
    else:
        Draw_line(0)

    turtle.left(90)

    if num in [0,4,5,6,8,9]:
        Draw_line(1)
    else:
        Draw_line(0)

    if num in [0,2,3,5,6,7,8,9]:
        Draw_line(1)
    else:
        Draw_line(0)

    if num in [0,1,2,3,4,7,8,9]:
        Draw_line(1)
    else:
        Draw_line(0)

    turtle.seth(0)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()

def Draw_Mutil_Tube(str):
    for i in str:
        if i=='-':
            turtle.write('时', font=('Arial', 18, 'normal'))
            turtle.penup()
            turtle.forward(40)
            turtle.pencolor("red")
        elif i=='=':
            turtle.write('分', font=('Arial', 18, 'normal'))
            turtle.penup()
            turtle.forward(40)
            turtle.pencolor("green")
        elif i=='+':
            turtle.write('秒', font=('Arial', 18, 'normal'))
            turtle.penup()
            turtle.forward(40)
        else:
            Draw_Single_Tube(eval(i))


def Get_Time():
    now = time.localtime()
    now = time.strftime('%H-%M=%S+', now)
    return now

def main():
    while 1:
        turtle.reset()
        turtle. setup(800, 450)
        turtle. penup()
        turtle.fd(-350)
        turtle.pendown( )
        turtle.pensize(10)
        turtle.pencolor("blue")
        turtle.speed(0)

        Draw_Mutil_Tube(Get_Time())

    turtle.hideturtle()
    turtle.done()

if __name__ == '__main__':
    main()


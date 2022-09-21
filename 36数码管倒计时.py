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

def Draw_Num(num):
    num = str(num)
    num = list(num)
    for i in num:
        Draw_Single_Tube(eval(i))
    return num


time = input("输入倒计时时长：")
time = eval(time)

turtle.pencolor('black')


for i in range(time):
    turtle.reset()
    turtle.pensize(15)
    turtle.pencolor('black')
    turtle.speed(0.1)
    Draw_Num(time-i)




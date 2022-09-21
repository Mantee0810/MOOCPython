import turtle
num = input("输入要绘制的同切圆个数：")
num = int(num)
r = input("输入最小圆的半径：")
delta = input("输入不同圆的半径差：")
r = float(r)
delta = float(delta)
for i in range(num):
    r += i*delta
    turtle.circle(r)

import turtle
turtle.begin_fill()
turtle.color('red')
turtle.width(2)
for i in range(5):
    turtle.fd(200)
    turtle.right(144)
turtle.end_fill()
turtle.width(5)
turtle.color('black')
for i in range(5):
    turtle.fd(200)
    turtle.right(144)
turtle.done()
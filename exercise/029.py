import turtle


def fun():
    turtle.speed(2)
    turtle.color('red')
    for i in range(6):
        turtle.forward(100)
        turtle.left(60)
    turtle.done()

fun()
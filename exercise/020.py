"""
题目：要求输出国际象棋棋盘。
"""

import turtle


def fun():
    length = 50
    switch = 1
    turtle.screensize(720, 720)
    turtle.speed(10)
    turtle.penup()
    for i in range(8):
        for j in range(8):
            if switch == 1:
                if j % 2 == 0:
                    color = "black"
                else:
                    color = "white"
            elif switch == -1:
                if j % 2 == 0:
                    color = "white"
                else:
                    color = "black"
            turtle.goto(-4 * length + length * j, 4 * length - length * i)
            drawSquare(color, length)
        switch = -switch
    turtle.done()


# Draw a square

def drawSquare(color, length):
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()


fun()

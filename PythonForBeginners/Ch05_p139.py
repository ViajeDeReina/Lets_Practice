# Ch05 > P.139 - Example 2
# 3 turtles will stray on the screen, and when they meet each other, they stop and become bigger.

import turtle as t
import math
import random as rd

t1, t2, t3 = [None]*3
t1X, t1Y, t2X, t2Y, t3X, t3Y = [0]*6
swidth, sheight = 300, 300

if __name__ == "__main__":
    t.title("거북이 만나기")
    t.setup(width = swidth+50, height = sheight+50)
    t.screensize(swidth,sheight)

    t1 = t.Turtle('turtle'); t1.color("red"); t1.penup()
    t2 = t.Turtle('turtle'); t2.color("blue"); t2.penup()
    t3 = t.Turtle('turtle'); t3.color("green"); t3.penup()

    t1.goto(-100,-100)
    t2.goto(0,0)
    t3.goto(100,100)

    while True:
        angle = rd.randrange(0,360)
        dist = rd.randrange(1,50)
        t1.left(angle); t1.forward(dist)

        angle = rd.randrange(0, 360)
        dist = rd.randrange(1, 50)
        t2.left(angle); t2.forward(dist)

        angle = rd.randrange(0, 360)
        dist = rd.randrange(1, 50)
        t3.left(angle); t3.forward(dist)

        t1X = t1.xcor(); t1Y = t1.ycor()
        t2X = t1.xcor(); t2Y = t1.ycor()
        t3X = t1.xcor(); t3Y = t1.ycor()

        dist12 = math.sqrt((t1X - t2X) ** 2 + (t1Y - t2Y) ** 2)
        dist23 = math.sqrt((t2X - t3X) ** 2 + (t2Y - t3Y) ** 2)
        dist13 = math.sqrt((t1X - t3X) ** 2 + (t1Y - t3Y) ** 2)

        if ((dist12 <=2) | (dist23 <=2) | (dist13 <=2)) :
            t1.turtlesize(3)
            t2.turtlesize(3)
            t3.turtlesize(3)
            break

    t.done()
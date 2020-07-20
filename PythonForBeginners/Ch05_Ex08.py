# Ch05 > Exercise 8
# 3 turtles will stray on the screen, and when they meet each other, they stamps there, and keep moving.

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

    t1 = t.Turtle('turtle'); t1.color("red"); t1.speed(0.5); t1.penup()
    t2 = t.Turtle('turtle'); t2.color("blue"); t2.speed(0.5); t2.penup()
    t3 = t.Turtle('turtle'); t3.color("green"); t3.speed(0.5); t3.penup()

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

        if((t1X<-150) | (t1Y<-150) | (t1X>150) | (t1Y>150)):
            t1.goto(-100, -100)
        if ((t2X < -150) | (t2Y < -150) | (t2X > 150) | (t2Y > 150)):
            t2.goto(-100, -100)
        if ((t3X < -150) | (t3Y < -150) | (t3X > 150) | (t3Y > 150)):
            t3.goto(-100, -100)

        dist12 = math.sqrt(((t1X - t2X) ** 2) + ((t1Y - t2Y) ** 2))
        dist23 = math.sqrt(((t2X - t3X) ** 2) + ((t2Y - t3Y) ** 2))
        dist13 = math.sqrt(((t1X - t3X) ** 2) + ((t1Y - t3Y) ** 2))

        if ((dist12 <=1) | (dist23 <=1) | (dist13 <=1)) :
            t1.stamp()
            t2.stamp()
            t3.stamp()

    t.done()
# Ch06 > Exercise 09
# The tiny turtle will draw a colourful spiral.

import turtle as t
import random as rd

swidth, sheight = 500, 500

t.title("거북 소라 그리기")
t.setup(width = swidth+50, height = sheight+50)
t.screensize(swidth, sheight)
t.shape("turtle")
t.penup()
t.goto(0,0)
t.right(90)
t.pendown()

dist = 5

for i in range(80):
    r = rd.random()
    g = rd.random()
    b = rd.random()
    t.color(r, g, b)
    t.forward(dist)
    t.left(30)
    dist +=1
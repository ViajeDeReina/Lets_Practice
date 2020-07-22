# Ch08 > Exercise 09
# The tiny turtle will write down the strings in the shape of circle.

import turtle as t
import random as rd
from tkinter.simpledialog import *

swidth, sheight = 300, 300

t.title("글자를 쓰는 거북이")
t.shape("turtle")
t.color("green")
t.setup(width = swidth+50, height = sheight+50)
t.screensize(swidth, sheight)
t.penup()
t.goto(0,0)

inStr = askstring("문자열 입력", "거북이가 쓸 문자열을 입력하세요.")

t.forward(100)
t.left(90)
angle = 360/len(inStr)

for ch in inStr:
    t.left(angle)
    dist = 200*3.14*angle/360
    r = rd.random(); g = rd.random(); b = rd.random()
    txtSize = 20
    t.pencolor(r,g,b)
    t.write(ch, font=("arial", txtSize, "bold"))
    t.forward(dist)

t.done()
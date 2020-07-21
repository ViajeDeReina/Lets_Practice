#Ch08 > p.227 - Practice 7
# The tiny turtle will help to print out the strings at random places

import turtle as t
import random as rd
from tkinter.simpledialog import *

inStr = ""
swidth, sheight = 300, 300
tX, tY, txtSize = [0]*3

t.title("거북이 글자 쓰기")
t.shape("turtle")
t.setup(width = swidth+50, height = sheight+50)
t.screensize(swidth, sheight)
t.penup()

inStr = askstring("문자열 입력", "거북이 쓸 문자열을 입력") # POP UP WINDOW !

for ch in inStr:
    tX = rd.randrange(-swidth/2, swidth/2)
    tY = rd.randrange(-sheight/2, sheight/2)
    r = rd.random(); g = rd.random(); b = rd.random()
    txtSize = rd.randrange(10, 50)

    t.goto(tX, tY)
    t.pencolor((r,g,b))
    t.write(ch, font = ("Arial", txtSize, "bold"))
t.done()
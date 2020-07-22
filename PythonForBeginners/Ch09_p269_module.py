# Ch09 > p.269 Practice
# Declare functions

import random as rd
from tkinter.simpledialog import *

def getStr():
    retStr = askstring("문자열 입력", "거북이가 쓸 문자열을 입력하세요")
    return retStr

def getRGB():
    r = rd.random()
    g = rd.random()
    b = rd.random()
    return (r, g, b)

def getXYAS(sw, sh):
    x,y,angle,size = 0,0,0,0
    x = rd.randrange(-sw/2, sw/2)
    y = rd.randrange(-sh/2, sh/2)
    angle = rd.randrange(0, 360)
    size = rd.randrange(10,50)
    return [x, y, angle, size]
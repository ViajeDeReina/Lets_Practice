# Ch09 > p.269 Practice
# Main. This program is basically same as the previous experiment.

from Ch09_p269_module import *
import turtle as t

swidth, sheight = 300, 300
tX, tY, tAngle, txtSize = [0]*4

t.title("거북이가 글자 쓰는 프로그램")
t.shape("turtle")
t.setup(width = swidth+50, height = sheight+50)
t.screensize(swidth, sheight)
t.penup()
t.speed(5)

inStr = getStr()

for ch in inStr:
    tX, tY, tAngle, txtSize = getXYAS(swidth, sheight)
    r,g,b = getRGB()
    t.goto(tX, tY)
    t.left(tAngle)
    t.pencolor((r,g,b))
    t.write(ch, font = ("arial", txtSize, "bold"))

t.done()
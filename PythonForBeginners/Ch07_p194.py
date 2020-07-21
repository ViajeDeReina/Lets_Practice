#Ch07 > p.194 - Practice 7
# Hundres of turtles (some may have different shapes) will pop out from the list.
# The most important part of this program is making a group with each turtle's information as a listed form.

import turtle as t
import random as rd

myTurtle, tX, tY, tColor, tSize, tShape = [None]*6
shapeList = []
playerTurtles = []
swidth, sheight = 500, 500

if __name__ == "__main__":
    t.title("거북 리스트 활용")
    t.setup(width = swidth+50, height = sheight+50)
    t.screensize(swidth, sheight)

    shapeList = t.getshapes()
    for i in range(100):
        rd.shuffle(shapeList)
        myTurtle = t.Turtle(shapeList[0])
        tX = rd.randrange(-swidth/2, swidth/2)
        tY = rd.randrange(-sheight/2, sheight/2)
        r = rd.random(); g = rd.random(); b = rd.random();
        tSize = rd.randrange(1,3)
        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])

    for tList in playerTurtles:
        myTurtle = tList[0]
        myTurtle.color((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4], tList[5], tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.goto(tList[1], tList[2])

    t.done()
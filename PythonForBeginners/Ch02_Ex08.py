import turtle as t
import random as rand

def leftClick (x,y):
    global r,g,b
    r = rand.random()
    g = rand.random()
    b = rand.random()
    t.color((r,g,b))
    t.shapesize(rand.randrange(1,10))
    t.penup()
    t.goto(x,y)
    t.stamp()

t.title("Turtle Stamp!")
t.shape("turtle")

t.onscreenclick(leftClick, 1)

t.done()
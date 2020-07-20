# Ch06 > p.173 - Example 02
# We'll see the turtle helps us to get the multiply table.

import turtle as t
i, k, tX, tY = [0]*4
swidth, sheight = 800, 450

if __name__ == "__main__":
    t.title("거북 구구단")
    t.shape("turtle")
    t.setup(width = swidth+50, height = sheight+50)
    t.screensize(swidth,sheight)
    t.penup()
    tX, tY = -500, 250
    t.goto(tX, tY)

    for i in range(1,10):
        for k in range(2,10):
            t.goto(tX+80*k, tY-40*i)
            mply = str(k) + " x " + str(i) + " = " + str(k*i)
            t.write(mply, font = ("Arial", 12, "bold"))

    t.goto(0,-200)
    t.done()
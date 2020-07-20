import turtle as t

def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)

def polygon2(n,a):
    for x in range(n):
        t.forward(a)
        t.left(360/n)

polygon(3)
polygon(8)

t.penup()
t.forward(100)
t.pendown()


polygon2(4,100)
polygon2(6,150)

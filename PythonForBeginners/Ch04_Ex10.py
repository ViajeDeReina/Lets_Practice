# Ch04 > Exercise 10
# This program will convert decimal int into binary digits, showing with turtles 0 & 1
# when the user inputs 2 decimal int a& b, then it will operate logical "and" operation.

import turtle as t

swidth, sheight = 1000, 300
curX, curY = 0,0

if __name__ == "__main__":
    t.title("거북이 논리곱")
    t.shape("turtle")
    t.setup(width = swidth+50, height = sheight+50)
    t.screensize(swidth,sheight)
    t.penup()
    t.left(90)

    a,b = map(int, input("숫자 2개를 입력하세요 : ").split())
    result_int = a & b
    binary_a = bin(a)
    binary_b = bin(b)

    curX = swidth/2
    curY = 70
    for i in range(len(binary_a)-2):
        t.goto(curX,curY)
        if a&1:
            t.color("red")
            t.turtlesize(2)
        else:
            t.color("blue")
            t.turtlesize(1)
        t.stamp()
        curX -= 50
        a>>= 1 #this means the bit will be shifted by 1

    curX = swidth/2
    curY = 0
    for i in range(len(binary_b)-2):
        t.goto(curX,curY)
        if b&1:
            t.color("red")
            t.turtlesize(2)
        else:
            t.color("blue")
            t.turtlesize(1)
        t.stamp()
        curX -= 50
        b>>= 1

    curX = swidth / 2
    curY = -70

    for i in range(min([len(binary_a),len(binary_b)])-2):
        t.goto(curX,curY)
        if result_int&1:
            t.color("red")
            t.turtlesize(2)
        else:
            t.color("blue")
            t.turtlesize(1)
        t.stamp()
        curX -= 50
        result_int>>= 1
    t.done()
# Ch04 > p.115 - Example02
# This program will convert decimal int into binary digits, showing with turtles 0 & 1

import turtle as t

num = 0
swidth, sheight = 1000, 300
curX, curY = 0,0

if __name__ == "__main__":
    t.title("거북이로 2진수 표현하기")
    t.shape("turtle")
    t.setup(width = swidth+50, height = sheight+50)
    t.screensize(swidth,sheight)
    t.penup()
    t.left(90)

    num = int(input("숫자를 입력하세요 : "))
    binary = bin(num)
    curX = swidth/2
    curY = 0
    for i in range(len(binary)-2):
        t.goto(curX,curY)
        if num&1:
            t.color("red")
            t.turtlesize(2)
        else:
            t.color("blue")
            t.turtlesize(1)
        t.stamp()
        curX -= 50
        num>>=1
    t.done()



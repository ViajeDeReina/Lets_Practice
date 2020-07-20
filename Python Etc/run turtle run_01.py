#Run Turtle Run!

import turtle as t
import random

villian=t.Turtle()
villian.shape("turtle")
villian.color("red")
villian.speed(0)
villian.up() #to avoid any trace after villian moves
villian.goto(0,200) #default position

food=t.Turtle()
food.shape("circle")
food.color("yellow")
food.speed(0)
food.up()
food.goto(0,-200) #default position of food

#now we're setting the key press motion

def turn_right():
    t.setheading(0)

def turn_left():
    t.setheading(180)

def turn_up():
    t.setheading(90)

def turn_down():
    t.setheading(270)

#now we're setting the playing rules

def play():
    t.forward(10)
    ang=villian.towards(t.pos()) #villian will move towards the turtle
    villian.setheading(ang)
    villian.forward(9)
    if t.distance(food)<12:  #when the turtle moves close enough to the food
        starx=random.randint(-230,230)
        stary=random.randint(-230,230) #the food will be reallocated at random position
        food.goto(starx,stary)
    if t.distance(villian)>=12: #when the turtle is far enough from the villian
        t.ontimer(play,100) #function play() will be work after 0.1 sec
    if t.xcor()<=-230:
        t.forward(-10)
    if t.xcor()>=230:
        t.forward(-10)
    if t.ycor()<=-230:
        t.forward(-10)
    if t.ycor()>=230:
        t.forward(-10)
    
#now we're setting the basic gaming condition

t.setup(500,500) #it means the size of the window will be 500x500 pixel size
t.bgcolor("black")
t.shape("turtle")
t.color("white")
t.speed(0)
t.up()

#setting the key press

t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")

t.listen()
play()

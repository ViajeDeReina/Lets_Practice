#turtle canon game

import turtle as t
import random

def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def shoot():
    ang=t.heading() #the angle will be determined by the user after adjusted by up/down keys
    while t.ycor()>0: #this function will go on while it's above the ground y=0
        t.forward(15) #keep moving by distance 15
        t.right(5) #keep turning by 5 degrees

    #warning : we're still in the middle of function shoot()

    d=t.distance(target,0) #calculating the distance between t and the target
    t.sety(random.randint(10,100))
    if d<25: #when the distance <25, it will be considered as success
        t.color("blue")
        t.write("Good",False,"center",("Courier",15))
    else:
        t.color("red")
        t.write("Bad",False,"center",("Courier",15))
    t.color("black") #return back to black colour
    t.goto(-200,10) #let turtle go back to the original position
    t.setheading(ang) #let turtle set back to the original angle

#now the definition of function shoot() is finished

t.goto(-300,0)
t.down()
t.goto(300,0) #the ground will be defined from x==-300 to x==300

#let's set the target point

target=random.randint(50,150)
t.pensize(3) #thicker pensize to be recognized
t.color("red")
t.up() #to avoid the turtle leaves the trace
t.goto(target-25,2)
t.down() #now you can start drawing
t.goto(target+25,2)

#let the turtle go back to the original condition to start the game

t.shape("turtle")
t.color("black")
t.up() #to avoid the turtle leaves the trace
t.goto(-200,10)
t.setheading(20)

#now we're setting the keys to control

t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(shoot,"space")

t.listen()

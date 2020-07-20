#this is upgrade version of Run Turtle Run
#basically everything is same except some details

import turtle as t
import random

t.title("Run Turtle Run")
t.setup(500,500)
t.bgcolor("black")

#tframe for just making frame around the window. turtle will only move within this area

tframe=t.Turtle()
tframe.shape("classic")
tframe.goto(-230,-230)
tframe.color("white")

for x in range(4):
    tframe.forward(460)
    tframe.left(90)

tframe.ht()

#our dear turtle

t.shape("turtle")
t.speed(0)
t.color("white")
t.up()

#adding score variables

score=0 #variable, default
playing=False #variable, default; True when space is pressed

#now we're setting each character

tvill=t.Turtle() #as a villian
tvill.shape("turtle")
tvill.color("red")
tvill.speed(10)
tvill.up()
tvill.goto(0,200) #default position

tfood=t.Turtle() #as food to eat
tfood.shape("circle")
tfood.color("yellow")
tfood.speed(0)
tfood.up()
tfood.goto(0,-200) #default position

#now we define each function for key control

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def start():
    global playing #this means that variable "playing" can be used in other place

    if playing == False:
        playing = True
        t.up()
        t.clear() #delete all previous trace of the turtle
        play()
        
def play():
    global score
    global playing

    if random.randint(1,5)==3:
        ang=tvill.towards(t.pos()) #villian will head towards the turtle with 20% possibility
        tvill.setheading(ang)
    speed=score+5

    if speed>15:
        speed=15 #speed will not exceed 15
    tvill.forward(speed)

    if t.distance(tvill)<12: #when the villian touches our dear turtle
        text="Score : "+str(score)
        message("Game Over",text)
        playing = False
        score=0

    if t.distance(tfood)<12: #when the food is close enough
        score=score+1 #gain 1 point
        t.write(score)
        starx=random.randint(-230,230)
        stary=random.randint(-230,230) #when turtle eats the food, new food will be reallocated
        tfood.goto(starx,stary)

    if playing:
        t.ontimer(play,100) #after 0.1sec, the function play will work (it means keep going)

def message(m1,m2): #this is for score message
    t.clear()
    t.goto(0,100)
    t.write(m1,False,"center",("Courier",20))
    t.goto(0,-100)
    t.write(m2,False,"center",("Courier",20))
    t.goto(0,-150)
    t.write("Press space to play again",False,"center",("Courier",20))
    t.home() #to the original position

#setting key press
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(start,"space")

t.listen()
message("Run Turtle Run","[Space]")

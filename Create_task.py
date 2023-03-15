#imports
import turtle
trtl = turtle
import random
import keyboard
from turtle import *

#setup pac
wn = trtl.Screen()
t=trtl.Turtle()
border=trtl.Turtle()
t.speed(0)




t.penup()
wn.setup(width = 1000, height = 800)
wn.bgpic('grid2.gif')

#creating indiviual borders

border.penup()
border.color("white")
border.setposition(-300, -300)
border.pendown()
border.pensize(7)
for side in range (4):
    border.forward(600)
    border.left(90)
border.hideturtle()



wn.addshape('pac2.gif')
t.shape('pac2.gif')

def up():
    t.setheading(90)
    

def down():
    t.setheading(270)



def left():
    t.setheading(180)



def right():
    t.setheading(0)

turtle.listen()
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

#border control
while True:
    t.forward(5)
    if t.xcor() > 300 or t.xcor() < -300:
        t.right(180)
    wn.update()



turtle.mainloop()



wn.mainloop()

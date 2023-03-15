import turtle
t = turtle.Turtle()
wn = turtle.Screen()

t.color('yellow')
t.pendown()
t.pensize(3)

def up():
    t.setheading(90)
    t.forward(50)
    

def down():
    t.setheading(270)
    t.forward(50)


def left():
    t.setheading(180)
    t.forward(50)


def right():
    t.setheading(0)
    t.forward(50)

turtle.listen()
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

#border control

    


turtle.mainloop()

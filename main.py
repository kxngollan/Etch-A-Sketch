import turtle

myturtle = turtle.Turtle()
myturtle.shape("turtle")

direction = 0

def forward():
    myturtle.forward(10)

def backward():
    myturtle.backward(10)

def counterclockwise():
    global direction
    direction -= 2
    myturtle.setheading(direction)

def clockwise():
    global direction
    direction += 2
    myturtle.setheading(direction)

def no_drawing():
    if myturtle.isdown():
        myturtle.penup()
    else:
        myturtle.pendown()

def clear():
    myturtle.home()
    myturtle.clear()

screen = turtle.Screen()

screen.listen()
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(counterclockwise, "Left")
screen.onkey(clockwise, "Right")
screen.onkey(no_drawing, "space")
screen.onkey(clear, "c")



screen.screensize(canvwidth=600,canvheight=600, bg="white")
screen.exitonclick()
import turtle
import random

# setup the window with a background color
wn = turtle.Screen()
wn.bgcolor("black")

# assign a name to your turtle
elsa = turtle.Turtle()
elsa.speed(1555)

# create a list of colours
sfcolor = ["white"]

# create a function to create different size snowflakes
def snowflake(size):
    # move the pen into starting position
    elsa.pensize(3)
    elsa.penup()
    elsa.forward(10*size)
    elsa.left(45)
    elsa.pendown()
    elsa.color("light green")
    # draw branch 8 times to make a snowflake
    for i in range(8):
        branch(size)
        elsa.left(45)

# create one branch of the snowflake
def branch(size):
    for i in range(3):
        for i in range(3):
            elsa.forward(10.0*size/3)
            elsa.backward(10.0*size/3)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(10.0*size/3)
        elsa.left(45)
    elsa.right(90)
    elsa.forward(10.0*size)
    
# changes starting co-ordinates


x = int(50)
y = int(60)
sf_size = int(6)
elsa.penup()
elsa.goto(x, y)
elsa.pendown()
snowflake(sf_size)

# leave the window open until you click to close
wn.exitonclick() 

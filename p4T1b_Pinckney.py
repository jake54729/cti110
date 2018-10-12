import turtle
wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("grey")
wn.title("J & P")

J = turtle.Turtle()      # Create J and set some attributes
J.color("blue")
J.pensize(5)



P = turtle.Turtle()      # Create P

J.left(180)              #cretes j from top left
J.forward(100)
J.left(180)
J.forward(50)
J.right(90)
J.forward(100)

# arc in j                            
for x in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
    J.right(10)
    J.forward(5)

P = turtle.Turtle()      # Create P and some attributes
P.color("green")
P.pensize(3)


P.forward(45)
for y in [17]:       # arc in P
    P.left(10)
    P.forward(5)
for y in [17]:       # arc in P
    P.right(10)
    P.forward(5)





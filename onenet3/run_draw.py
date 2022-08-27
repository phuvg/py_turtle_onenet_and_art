import turtle
import math

t = turtle.Pen()
s = turtle.Screen()
#s.bgpic("c.gif")
t.pensize(3)
#t.pencolor("white")

def square(x):
    for i in range(0, 4, 1):
        if(i < 3):
            t.forward(x*2)
        else:
            t.forward(x)
        t.right(90)

def rhombus(x):
    for i in range(0, 4, 1):
        if(i == 3):
            t.forward(x/2)
        else:
            t.forward(x)
        t.left(90)

x = 100
t.penup()
t.back(x)
t.left(90)
t.forward(x)
t.right(90)
t.pendown()

square(x)
t.right(45)
rhombus(math.sqrt(pow(x,2)*2))
t.left(45)
square(x/2)
t.right(45)
rhombus(math.sqrt(pow(x/2,2)*2))

t.right(90)
t.forward(math.sqrt(pow(x/2,2)*2)/2)
t.right(135)
t.forward(x/2)
t.left(135)
t.forward(math.sqrt(pow(x,2)*2)/2)
t.right(135)
t.forward(x)

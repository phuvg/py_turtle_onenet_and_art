import turtle
import math

t = turtle.Pen()
s = turtle.Screen()
#s.bgpic("c.gif")
t.pensize(3)
#t.pencolor("white")

x = 40
    
for i in range(0, 4, 1):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(135)
    t.forward(math.sqrt(pow(x,2)*2))
    t.right(135)
    t.forward(x)
    if(i < 3):
        t.right(90)
        t.forward(x)
        t.left(90)
        t.forward(x)
for i in range(0, 4, 1):
    if(i == 3):
        t.forward(x*2)
    else:
        t.forward(x)
    t.left(90)
t.forward(x)

import turtle

t = turtle.Pen()
t.pensize(3)

t.forward(100)

for i in range(0,2,1):
    if(i==0):
        t.left(90)
    else:
        t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(30)

t.left(90)
t.forward(100)
t.right(90)
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
    
    

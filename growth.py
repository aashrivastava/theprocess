import turtle

t = turtle.Turtle()
t.hideturtle()

for i in range(4):
    t.forward(10)
    t.right(90)


t2 = turtle.Turtle()
t2.hideturtle()

t.penup()
t2.penup()

t.goto(10, 10)
t2.goto(10, -10)

t.pendown()
t2.pendown()

for i in range(4):
    t.forward(10)
    t.right(90)
    t2.forward(10)
    t2.right(90)
    
t.penup()
t2.penup()

t.goto(-10, 10)
t2.goto(-10, -10)

t.pendown()
t2.pendown()

for i in range(4):
    t.forward(10)
    t.right(90)
    t2.forward(10)
    t2.right(90)

import turtle
import random

turtle.colormode(255)
t = turtle.Turtle()
t.speed(0)
t.ht()

def randColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r, g, b)

def draw_mandala(color):
    r, g, b = (color[0], color[1], 0)
    for i in range(36):

        b += 255 // 36
        t.color(r, g, b)
        length = 10

        for j in range(3):
            length += 5

            for j in range(4):
                t.forward(length)
                t.right(90)

        t.right(10)

def draw_circles(color, size):
    r, g, b = (color[0], color[1], 0)
    radius = size
    t.speed(20)
    for i in range(36):
        b += 255 // 36
        t.color(r, g, b)
        t.circle(radius)
        t.right(10)

t.goto(0,0)
t.pd()

#draw_mandala(randColor())
radius = 10
for i in range(11):
    draw_circles(randColor(), radius)
    radius += 10


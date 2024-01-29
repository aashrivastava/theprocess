import turtle

turtle.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.ht()

r = 255
g = 100
b = 0

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
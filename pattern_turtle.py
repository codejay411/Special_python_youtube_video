from turtle import *

speed(0)
bgcolor('black')
pensize(3)

for i in range(5):
    for j in ["red", "orange", "green", "yellow", "white", "blue", "cyan"]:
        color(j)
        left(12)
        for k in range(4):
            forward(200)
            left(90)
hideturtle()
done()


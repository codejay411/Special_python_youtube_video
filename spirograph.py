import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

colors = ['red', 'green', 'blue', 'yellow', 'white', 'cyan', 'magenta']

for i in range(6):
    for color1 in colors:
        turtle.color(color1)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()
turtle.done()
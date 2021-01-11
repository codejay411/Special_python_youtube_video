import turtle

color = ["red", "orange", "green", "yellow", "blue", "purple"]
turtle.bgcolor('black')

for i in range(360):
    turtle.pencolor(color[i%6])
    turtle.width(i/100+1)
    turtle.forward(i)
    turtle.left(59)

turtle.done()
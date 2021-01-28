import turtle

sc = turtle.Screen()
pen = turtle.Turtle()

def ranbow(col, rad, val):
    pen.color(col)
    pen.circle(rad, -180)
    pen.up()
    pen.setpos(val, 0)
    pen.down()
    pen.right(180)

color = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
sc.setup(600,600)
sc.bgcolor('black')
pen.right(90)
pen.width(10)
pen.speed(7)

for i in range(7):
    ranbow(color[i], 10*(i+8), -10*(i+1))

pen.hideturtle()
turtle.done()


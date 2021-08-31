import turtle

house = turtle.Turtle()
turtle.bgcolor("sky blue")

house.begin_fill()
house.color("yellow")
for i in range(4):
    house.forward(100)
    house.left(90)
house.left(90)
house.forward(100)
house.end_fill()
house.begin_fill()
house.color("brown")
house.right(30)
house.forward(100)
house.right(120)
house.forward(100)
house.end_fill()
turtle.done()
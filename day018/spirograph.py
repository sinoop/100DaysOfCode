import random
from turtle import Turtle, Screen

turtle = Turtle()
# turtle.width = 1000

s = Screen()
s.colormode(255)
turtle.speed(0)


for sides in range(0, 360, 5):
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    turtle.pencolor(red, blue, green)
    turtle.setheading(sides)
    turtle.circle(100)
    # left_or_right = random.randint(0, 1)
    # if left_or_right == 0:
    #     turtle.right(90)
    # if left_or_right == 1:
    #     turtle.left(90)
    # turtle.forward(side_length)

s.exitonclick()

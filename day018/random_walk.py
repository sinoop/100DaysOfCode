from turtle import Turtle, Screen
import random

turtle = Turtle()
s = Screen()
s.colormode(255)
side_length = 20
left_or_right = 0
turtle.pensize(4)
directions = [0, 90, 180, 270]
for sides in range(1, 200):
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    turtle.pencolor(red, blue, green)
    turtle.setheading(random.choice(directions))
    # left_or_right = random.randint(0, 1)
    # if left_or_right == 0:
    #     turtle.right(90)
    # if left_or_right == 1:
    #     turtle.left(90)
    turtle.forward(side_length)

s.exitonclick()

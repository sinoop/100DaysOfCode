from turtle import Turtle, Screen
import random

t = Turtle()
t.speed(0)
t.penup()
t.goto(0, 300)
t.pendown()
s = Screen()
s.colormode(255)

t.shape("turtle")
user_sides = int(input("Number of shapes desired : "))
side_length = int(input("Side Length : "))
for sides in range(3, 3 + user_sides + 1):
    print(f"Drawing {sides} sided shape out of {3 + user_sides}")
    angle = 360.0 / sides
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    t.pencolor(red,blue, green)
    print(f"angle = {angle}")
    for _ in range(1, sides + 1):
        t.forward(side_length)
        t.right(angle)


s.exitonclick()

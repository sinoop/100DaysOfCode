import random
from turtle import Turtle, Screen

import colorgram

circle_size = 10
width = 500
height = 500

color = colorgram.extract("image.jpg", 30)
rgb_color = []
for c in color:
    if c.rgb.r <= 240 and c.rgb.b < 240 and c.rgb.g < 240:
        rgb_color.append((c.rgb.r, c.rgb.g, c.rgb.b))

turtle = Turtle()

s = Screen()
s.setup(width=width, height=height)
s.colormode(255)
turtle.penup()
turtle.speed("fastest")
turtle.hideturtle()

start_x = (-1 * (width / 2)) + 2 * circle_size
start_y = (-1 * (height / 2)) + 2 * circle_size
for y_range in range(0, int(height / (circle_size * 2 - circle_size))):
    turtle.setx(start_x)
    turtle.sety(start_y)
    for x_range in range(0, int(width / (circle_size * 2))):
        color = random.choice(rgb_color)
        turtle.dot(circle_size, color)
        turtle.forward(circle_size * 2)
    start_y += circle_size * 2

s.exitonclick()

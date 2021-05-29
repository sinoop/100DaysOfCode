import time
from turtle import Screen, Turtle

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
start_position = (0, 0)
start_size = 3
snake_block_size = 20
snake_shape = "circle"
screen_color = "black"
snake_color = "white"

screen = Screen()
screen.setup(width=WINDOW_WIDTH,
             height=WINDOW_HEIGHT)
screen.bgcolor(screen_color)
screen.title("Snake")
screen.tracer(0)

segments = []
x, y = start_position
for _ in range(0, start_size):
    new_segment = Turtle(shape=snake_shape)
    new_segment.color(snake_color)
    new_segment.penup()
    new_segment.goto(x, y)
    segments.append(new_segment)
    x += (-1 * snake_block_size)
screen.update()


def turn_head(segment: Turtle, direction):
    if direction == "right":
        segment.setheading(segment.heading() + 90)
        print(f"Turned Right {segment.heading()}")

    if direction == "left":
        segment.setheading(segment.heading() - 180)
        print(f"Turned Left {segment.heading()}")

    segment.forward(snake_block_size)


def turn_right():
    turn_head(segments[0], "right")


def turn_left():
    turn_head(segments[0], "right")


screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    for index in range(len(segments) - 1, 0, -1):
        segments[index].goto(segments[index - 1].xcor(),
                             segments[index - 1].ycor())
    segments[0].left(90)
    segments[0].forward(snake_block_size)

screen.exitonclick()

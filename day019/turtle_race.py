import json
import random
from turtle import Turtle, Screen

TURTLE_HEIGHT = 40
TURTLE_WIDTH = 40


class TurtleObject:

    def __init__(self, color, name, start_x, start_y, max_x):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.color(color)
        self.turtle_name = name
        self.turtle.setx(start_x)
        self.turtle.sety(start_y)
        self.turtle.shape("turtle")
        self.max_x = max_x

    def move_forward(self):
        self.turtle.forward(random.randint(0, 20))
        if self.turtle.xcor() + TURTLE_WIDTH >= self.max_x:
            return False
        return True


# number_of_turtles = input()


s = Screen()
num_turtles_entered = s.numinput(
    title="NUM",
    prompt="Enter Number of Turtles in race : ",
    default=2
)
num_turtles = 2 if num_turtles_entered is None else int(num_turtles_entered)
s.setup(width=400, height=(num_turtles * TURTLE_HEIGHT * 2) + (2 * TURTLE_HEIGHT))

MIN_X = (-1 * s.window_width() / 2) + TURTLE_WIDTH
MIN_Y = (-1 * s.window_height() / 2) + TURTLE_HEIGHT
MAX_X = s.window_width() / 2

start_x = MIN_X
start_y = MIN_Y

with open("colors.json", "r") as f:
    json_colors = json.load(f)

is_race_on = False
turtle_list = []
random_list = random.sample(range(0, len(json_colors)), len(json_colors))
for i in range(1, num_turtles):
    random_color = json_colors[str(random_list[i])]
    turtle_list.append(TurtleObject(color=random_color["hex"],
                                    name=random_color["name"],
                                    start_x=start_x,
                                    start_y=start_y,
                                    max_x=MAX_X)
                       )
    start_y += (TURTLE_HEIGHT * 2)

is_race_on = True

random_turtle = None
while is_race_on:
    random_turtle = random.choice(turtle_list)
    is_race_on = random_turtle.move_forward()

print(f"{random_turtle.turtle_name} won")

s.exitonclick()

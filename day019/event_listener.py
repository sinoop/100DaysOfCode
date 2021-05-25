from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forward():
    t.forward(100)


def turn_left():
    new_heading = t.heading() + 20
    t.setheading(new_heading)

def turn_right():
    # t.left(20)
    new_heading = t.heading() - 20
    t.setheading(new_heading)

def move_backward():
    t.backward(100)


def clear():
    t.home()
    t.clear()


s.onkey(fun=move_forward, key="w")
# s.onkey(fun=move_backward, key="s")
# s.onkey(fun=turn_left, key="a")
s.onkey(fun=turn_left, key="a")
# s.onkeyrelease(fun=move_forward, key="a")
# s.onkey(fun=turn_right, key="d")
s.onkey(fun=turn_right, key="d")
# s.onkeyrelease(fun=move_forward, key="d")

s.onkeypress(fun=clear, key="c")

s.listen()
s.exitonclick()

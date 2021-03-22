from turtle import Turtle, Screen

t = Turtle()

t.shape("turtle")
draw_flag = True
count = 1

for loop_int in range(0, 1000):
    if count <= 10:
        if draw_flag:
            t.pendown()
        else:
            t.penup()
        count = count + 1
    else:
        draw_flag = not draw_flag
        count = 1

    t.forward(1)

s = Screen()
s.exitonclick()

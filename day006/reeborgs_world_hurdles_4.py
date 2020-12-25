def jump():
    wall_height = 0
    turn_left()
    while wall_on_right():
        move()
        wall_height += 1    
    turn_right()
    move()
    turn_right()     
    while wall_height > 0:
        move()
        wall_height -= 1       
    turn_left()
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while True:
    if at_goal():
        break
    if front_is_clear():
        move()
    if wall_in_front():
        jump()
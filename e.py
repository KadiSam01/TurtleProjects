import turtle

screen = turtle.Screen()

speed = 3
distance = 25
moving = False
pen_up = False


def move_right():
    global moving
    if not moving:
        moving = True
        player.speed(0)
        player.setheading(0)
        player.speed(speed)
        player.forward(distance)
        moving = False


def move_left():
    global moving
    if not moving:
        moving = True
        player.speed(0)
        player.setheading(180)
        player.speed(speed)
        player.forward(distance)
        moving = False


def move_up():
    global moving
    if not moving:
        moving = True
        player.speed(0)
        player.setheading(90)
        player.speed(speed)
        player.forward(distance)
        moving = False


def move_down():
    global moving
    if not moving:
        moving = True
        player.speed(0)
        player.setheading(270)
        player.speed(speed)
        player.forward(distance)
        moving = False


def toggle_draw():
    if player.pen().get('pendown'):
        player.penup()
    else:
        player.pendown()


def toggle_fill():
    if player.filling():
        player.end_fill()
    else:
        player.begin_fill()


def clear_screen():
    player.clear()


player = turtle.Turtle()

turtle.onkeypress(move_left, 'a')
turtle.onkeypress(move_right, 'd')
turtle.onkeypress(move_up, 'w')
turtle.onkeypress(move_down, 's')
turtle.onkeypress(toggle_draw, 'space')
turtle.onkeypress(toggle_fill, 'f')
turtle.onkeypress(clear_screen, 'r')

screen.listen()
screen.mainloop()

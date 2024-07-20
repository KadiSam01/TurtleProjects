import random
import turtle
screen = turtle.Screen()
screen.addshape('line.gif')

font_setup = ('Roboto', 20, 'normal')

font_setup2 = ('Roboto', 15, 'bold')


#establishes all the turtles used
p1 = turtle.Turtle()
p1.speed(0)
p1.shapesize(6, 1, 1)
p1.shape('square')
p1.up()
p1.goto(-325, 0)

p2 = turtle.Turtle()
p2.speed(0)
p2.shapesize(6, 1, 1)
p2.shape('square')
p2.up()
p2.goto(325, 0)

ball = turtle.Turtle()
ball.up()
ball.shape('circle')
ball_speed = 7
ball.dx = 1
ball.dy = 1

score1 = 0
p1_score = turtle.Turtle()
p1_score.speed(0)
p1_score.up()
p1_score.hideturtle()
p1_score.goto(-200, 250)

score2 = 0
p2_score = turtle.Turtle()
p2_score.speed(0)
p2_score.up()
p2_score.hideturtle()
p2_score.goto(200, 250)

bgturtle = turtle.Turtle('line.gif')
bgturtle.up()
bgturtle.speed(0)
bgturtle.goto(27, 0)

instructions = turtle.Turtle()
instructions.up()
instructions.ht()
instructions.goto(25, -275)
instructions.write('P1: USE UP AND DOWN KEYS TO MOVE', font=font_setup2)
instructions.goto(-300, -275)
instructions.write("P2: USE 'W' AND 'S' KEYS TO MOVE", font=font_setup2)

instructions2 = turtle.Turtle()
instructions2.up()
instructions2.ht()
instructions2.goto(-100, 15)
instructions2.write("PRESS 'ENTER' TO START", font=font_setup2)


counter = turtle.Turtle()
counter.hideturtle()

timer = 5
counter_interval = 1000
timer_up = False


#timer for screen update while the ball is moving
def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        timer_up = True
    else:
        timer -= 1
        2counter.getscreen().ontimer(countdown, counter_interval)

#moves the paddles


def move_p1_up():
    if p1.ycor() < 225:
        p1.goto(-325, p1.ycor()+15)


def move_p1_down():
    if p1.ycor() > -225:
        p1.goto(-325, p1.ycor()-15)


def move_p2_up():
    if p2.ycor() < 225:
        p2.goto(325, p2.ycor()+15)


def move_p2_down():
    if p2.ycor() > -225:
        p2.goto(325, p2.ycor()-15)


def start_move():
     #initializes movement of the ball
     global instructions2
      instructions2.clear()
       global ball_move
        ball.speed(3)
        ball_heading = random.randint(1, 360)
        ball.setheading(ball_heading)
        move_ball()


def update_p1_score():
     #updates player 1 scoreboard
     global score1
      score1 += 1
       p1_score.clear()
        p1_score.write(score1, font=font_setup)


def update_p2_score():
     #updates player 2 scoreboard
     global score2
      score2 += 1
       p2_score.clear()
        p2_score.write(score2, font=font_setup)


def move_ball():
     #continous movement of the ball
     global ball_move
      global ball_speed
       while True:
             screen.update()
              angle = ball.heading()
               ball_y = ball.ycor()
                ball_x = ball.xcor()
                p1_y = p1.ycor()
                p1_x = p1.xcor()
                p2_y = p2.ycor()
                p2_x = p2.xcor()
                ball.forward(ball_speed)
                #boundry line for the top and bottom of the window
                if ball_y > 270 or ball_y < -270:
                     ball.speed(0)
                       new_angle = (360-angle) % 360
                        ball.setheading(new_angle)
                        ball.speed(3)
                        ball.forward(40)

                #score zone for players
                if ball_x > 325:
                     ball.speed(0)
                      ball.goto(0, 0)
                       p1.goto(-325, 0)
                        p2.goto(325, 0)
                        update_p1_score()
                        start_move()
                if ball_x < -325:
                     ball.speed(0)
                      ball.goto(0, 0)
                       p1.goto(-325, 0)
                        p2.goto(325, 0)
                        update_p2_score()
                        start_move()
                #paddle detection for the ball
                if ball.distance((p1_x+10, p1_y-60)) < 20:
                     ball.speed(0)
                       new_angle = (180-angle) % 360
                        ball.setheading(new_angle)
                        ball.speed(3)
                        ball.forward(30)
                if ball.distance((p1_x-10, p1_y-30)) < 20:
                     ball.speed(0)
                       new_angle = (180-angle) % 360
                        ball.setheading(new_angle)
                        ball.forward(30)
                if ball.distance((p1_x-10, p1_y+30)) < 20:
                     ball.speed(0)
                       new_angle = (180-angle) % 360
                        ball.setheading(new_angle)
                        ball.forward(30)
                if ball.distance((p1_x, p1_y)) < 20:
                     ball.speed(0)
                       new_angle = (180-angle) % 360
                        ball.setheading(new_angle)
                        ball.forward(30)
                if ball.distance((p1_x-10, p1_y+60)) < 20:
                     ball.speed(0)
                       new_angle = (180-angle) % 360
                        ball.setheading(new_angle)
                        ball.forward(30)
                if ball.distance((p2_x-10, p2_y-60)) < 20:
                     ball.speed(0)
                       new_angle = (180-angle) % 360
                        ball.setheading(new_angle)
                        ball.forward(30)
                if ball.distance((p2_x, p2_y)) < 20:
                     ball.speed(0)
                       new_angle = (180-angle) % 360
                        ball.setheading(new_angle)
                        ball.forward(30)
                if ball.distance((p2_x-10, p2_y+60)) < 20:
                     ball.speed(0)
                       new_angle = (180-angle) % 360
                        ball.setheading(new_angle)
                        ball.forward(30)
                if ball.distance((p2_x-10, p2_y+30)) < 20:
                     ball.speed(0)
                       new_angle = (180-angle) % 360
                        ball.setheading(new_angle)
                        ball.forward(30)
                if ball.distance((p2_x-10, p2_y-30)) < 20:
                     ball.speed(0)
                       new_angle = (180-angle) % 360
                        ball.setheading(new_angle)
                        ball.forward(30)


screen.onkeypress(move_p1_up, 'w')
screen.onkeypress(move_p1_down, 's')
screen.onkeypress(move_p2_up, 'Up')
screen.onkeypress(move_p2_down, 'Down')

screen.onkeypress(start_move, 'Return')


screen.ontimer(countdown, counter_interval)
screen.listen()
screen.mainloop()

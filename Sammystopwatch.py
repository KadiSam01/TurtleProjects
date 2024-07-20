import turtle
from tkinter import BooleanVar, DoubleVar

is_running = BooleanVar()
elasped_time = DoubleVar()


def start_timer(x,y):
    print('starting timer')
    if not is_running.get():
        screen.ontimer(increment_time,100)
    else:
        is_running.set(True)


def stop_timer(x,y):
    print('the timer has being stoped')
    screen.ontimer(increment_time,0)
    is_running.set(False)

def reset_timer(x,y):
    print('the timer has being reseted')
    elasped_time.set(0)
    pen.clear()
    pen.write(f'{elapsed_time.get():.1f}', font=('Arial', 30, 'normal'))


def increment_time():
    print('the timer is being incrmeented')
    elasped_time.set(elasped_time.get()+.1)
    pen.clear()
    pen.write(f'{elasped_time.get():.1f}',font=('Arial',20,'normal'))
    if is_running.get():
        screen.ontimer(increment_time,100)


start_turtle = turtle.Turtle(shape='circle')
start_turtle.penup()
start_turtle.fillcolor('green')
start_turtle.shapesize(3)
start_turtle.goto(-100, 0)

stop_turtle = turtle.Turtle(shape='circle')
stop_turtle.penup()
stop_turtle.shapesize(3)
stop_turtle.fillcolor('red')


reset_turtle = turtle.Turtle(shape='circle')
reset_turtle.penup()
reset_turtle.shapesize(3)
reset_turtle.fillcolor('yellow')
reset_turtle.goto(100, 0)


screen = turtle.Screen()
start_turtle.onclick(start_timer)
stop_turtle.onclick(stop_timer)
reset_turtle.onclick(reset_timer)
#screen.onclick(start_timer)
#screen.onclick(stop_timer)

pen = turtle.Turtle()
pen.penup()
pen.goto(100,200)
pen.hideturtle()

screen.mainloop()

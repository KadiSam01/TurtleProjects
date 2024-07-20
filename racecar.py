import turtle,random
turtles = []
for num in range(10):
    turtles.append(turtle.Turtle(shape='turtle'))

startx = 200
starty = 200

for t in turtles:
    t.penup()
    t.goto(startx,starty)
    starty -= 50
    t.pendown()


for num in range(10):
    finish = turtle.Turtle()
    finish.penup()
    finish.goto(200, 200)
    finish.pendown()
    finish.goto(200, -150)
    finish.hideturtle()

for num in range(10):
    for t in turtles:
        t.forward(random.randint(1,20))
screen = turtle.Screen()

screen.mainloop()
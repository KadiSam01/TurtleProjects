### I just edited the the other polygon code but I included while loop this time. 
import turtle as trtl

painter = trtl.Turtle()
painter.width(10)
#def num_side():
#number_side = int(input("Number of sides for the shape?"))
#def side_legnth():
#side_length = int(input("What should the length be?"))
##def color_choice():
    ##color_option = input("What color do you desire?")

#painter.begin_fill()
#painter.end_fill()

painter.penup()
painter.pendown()
painter.pensize(25)
painter.speed(50)

side_length_option = True
option2 = True

while option2 == True:
    try:
        number_side = int(input("\nHow many sides do you want your shape to have? (must be above 2): "))
        if number_side > 2:
            angle_side = ((number_side-2) * 180)/number_side
            option2 = False
        else:
            print("Invalid, please try again")
    except ValueError:
        print("Error isn't an interger.")

##if number_side.isdigit() == False:
    ##print("You need to enter a number")
    ##num_side()

while side_length_option == True:
    try:
        length = int(input("\nWhat should the length be: "))
        side_length_option = False
    except ValueError:
        print("\You need to enter an interger number\n")
print("\nYour shape should be printed in any momment. \n")


drawing = 1

while drawing <= number_side:
    painter.forward(length)

    painter.right(abs(angle_side-180))
    drawing += 1



##painter.penup()

# ask user for a color (such as red, green, blue, pink, purple)


# ask user for the radius of a circle


# draw a circle with the radius and line color entered by the user


# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()
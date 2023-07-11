from turtle import Turtle,Screen
import random


screen=Screen()
screen.setup(width=500,height=400)
colors = ["red","orange","yellow","Green","blue","indingo","violet"]
user_bet= screen.textinput(title="make your bet", prompt="Which turtle will win the race? enter color: ")
y_position = [-100,-50,0,50,100]
all_turtles = []

is_race_on =False
for turtle_index in range(0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)
   
if user_bet:
    is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor()>230:
                is_race_on =False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print("You have won! {winning_color} is the winner")
                else:
                     print("You have lost! {winning_color} is the winner")

            random_distance =random.randint(0,10)
            turtle.forward(random_distance)

           






#tom = Turtle(shape="turtle")
#jim = Turtle(shape="turtle")
#Ed = Turtle(shape="turtle")
#Eve = Turtle(shape="turtle")
#
#def remove_turtle_line():
#    tim.penup()
#    tom.penup()
#    jim.penup()
#    Ed.penup()
#    Eve.penup()
#remove_turtle_line()
#
#def turtle_colors():
#    tim.color("Red")
#    tom.color("Green")
#    jim.color("Blue")
#    Ed.color("Purple")
#    Eve.color("Yellow")
#
#
#turtle_colors()
#
#def turtle_start_position():
#    tim.goto(x=-230,y=50)
#    tom.goto(x=-230,y=0)
#    jim.goto(x=-230,y=-50)
#    Ed. goto(x=-230,y=-100)
#    Eve.goto(x=-230,y=100)
#
#turtle_start_position()
#
##def start_race():
##    while True:
#        tim.forward(random.randint(1,400))
#        tom.forward(random.randint(1,400))
#        jim.forward(random.randint(1,400))
#        Ed.forward(random.randint(1,400))
#        Eve.forward(random.randint(1,400))
#
#        if tim.xcor() >= 400:
#            print("Red turtle wins")
#            break
#        elif tom.xcor() >= 400:
#            print("Green Turtle looses") 
#            break 
#        elif jim.xcor() >= 400: 
#            print("Blue turtle wins")
#            break
#        elif Ed.xcor() >= 400:
#            print("Purple turtle wins ")
#            break
#        else:
#            print("Yellow turtle wins")
#
#start_race()
#
screen.exitonclick()
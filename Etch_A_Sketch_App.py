from turtle import Turtle, Screen

tim = Turtle()
tim.pensize(5)
tim.color("red")
screen=Screen()
screen.listen()
def move_forward():
    tim.forward(5)
    screen.onkeypress(move_forward, 'w')

move_forward()

def  move_backwards():
    tim.backward(3)
    tim.forward(10)
    screen.onkeypress(move_backwards,'s')

move_backwards()

def move_counter_clockwise():
    tim.left(10)
    tim.forward(90)
    screen.onkeypress(move_counter_clockwise,'a')
move_counter_clockwise()

def move_right():
    tim.right(15)
    screen.onkeypress(move_right,'d')
move_right()
screen.exitonclick()
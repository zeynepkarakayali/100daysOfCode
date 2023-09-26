from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def moveForwards():
    tim.forward(10)

def moveBackwards():
    tim.backward(10)

def counterClockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clearScreen():
    tim.clear()
    tim.penup()
    tim.home()

screen.listen()
screen.onkey(key = "w", fun = moveForwards)
screen.onkey(key = "s", fun = moveBackwards)
screen.onkey(key = "a", fun = counterClockwise)
screen.onkey(key = "d", fun = clockwise)
screen.onkey(key = "c", fun = clearScreen)
screen.exitonclick()
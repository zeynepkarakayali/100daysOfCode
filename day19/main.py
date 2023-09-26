from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=700, height=500)
is_race_on = False
user_bet = screen.textinput(title="MAKE YOUR BET", prompt="Which turtule will win the race? Enter a color:")
y_positions = [125, 75, 25, -25, -75, -125]
colors = ["red","blue","green","yellow","orange", "pink"]
all_turtles = []

for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(-320, y_positions[turtle_index])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if(turtle.xcor() >= 330):
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"!!!YOU WON!!! The {winning_color} turtle is the winner! ")
            else:
                print(f"You lost! The {winning_color} turtle is the winner! ")

        speed = random.randint(0,10)
        turtle.forward(speed)

screen.exitonclick()
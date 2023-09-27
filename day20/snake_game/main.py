from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (-40,0)]
segments = []

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    for segment in segments:
        segment.forward(20)
        screen.update()

screen.exitonclick()
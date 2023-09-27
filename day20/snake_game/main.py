from turtle import Turtle,Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (-40,0)]
snake = Snake()

screen.listen()
screen.onkey("Up")
screen.onkey("Down")
screen.onkey("Left")
screen.onkey("Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
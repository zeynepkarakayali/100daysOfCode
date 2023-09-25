from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.pensize(5)
timmy.speed("fastest")

colors = ["cornflower blue", "medium aquamarine", "yellow green", "indian red", 
          "dark slate blue", "rosy brown", "goldenrod", "light slate gray", 
          "powder blue", "deep pink", "crimson", "dark orange"]

directions = [0, 90, 180, 270]

for _ in range(800):
    timmy.forward(random.randint(0,50))
    timmy.pensize(random.randint(3,10))
    timmy.color(random.choice(colors))
    timmy.setheading(random.choice(directions))
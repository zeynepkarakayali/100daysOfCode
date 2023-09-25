from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.pensize(5)
#timmy.shape("square")
# screen = Screen()

# screen.exitonclick()
colors = ["cornflower blue", "medium aquamarine", "yellow green", "indian red", 
          "dark slate blue", "rosy brown", "goldenrod", "light slate gray", 
          "powder blue", "deep pink", "crimson", "dark orange"]

def drawShape(num_sides):
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(360/num_sides)

for shape_side_n in range(3,11):
    timmy.color(random.choice(colors))
    drawShape(shape_side_n)
    
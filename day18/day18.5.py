# Spirograph

import turtle as t
import random

timmy = t.Turtle()
#t.colormode(255)
timmy.speed("fastest")
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    #color = (r, g, b)
    return f"#{r:02X}{g:02X}{b:02X}"
    #return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)

draw_spirograph(3)

screen = t.Screen()
screen.exitonclick()

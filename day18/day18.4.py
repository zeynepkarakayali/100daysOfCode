import turtle as t
import random

timmy = t.Turtle()
#t.colormode(255)
timmy.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return f"#{r:02X}{g:02X}{b:02X}"

directions = [0, 90, 180, 270]

for _ in range(800):
    timmy.pensize(random.randint(3,10))
    timmy.color(random_color())
    timmy.forward(random.randint(0,50))
    timmy.setheading(random.choice(directions))
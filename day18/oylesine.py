import turtle as t
import random

timmy = t.Turtle()
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return f"#{r:02X}{g:02X}{b:02X}"

directions = [0, 90, 180, 270]

# Get the screen (window) to determine its boundaries
screen = t.Screen()
screen_width = screen.window_width()
screen_height = screen.window_height()

for _ in range(1200):
    timmy.pensize(random.randint(3, 10))
    timmy.color(random_color())
    distance = random.randint(0, 50)
    timmy.forward(distance)

    # Check if the cursor is out of bounds
    if abs(timmy.xcor()) > screen_width / 2 or abs(timmy.ycor()) > screen_height / 2:
        timmy.penup()
        timmy.goto(0, 0)  # Reset the cursor to the center
        timmy.pendown()

    timmy.setheading(random.choice(directions))

# Keep the window open until the user closes it
t.exitonclick()

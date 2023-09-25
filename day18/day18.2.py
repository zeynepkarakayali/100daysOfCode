from turtle import Turtle, Screen

timmy = Turtle()
#timmy.shape("square")
# screen = Screen()

# screen.exitonclick()

def drawShape(num_sides):
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(360/num_sides)

for shape_side_n in range(3,11):
    drawShape(shape_side_n)
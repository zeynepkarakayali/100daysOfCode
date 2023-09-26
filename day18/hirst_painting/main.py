import colorgram
import random
from turtle import Turtle, Screen

timmy = Turtle()
colors = colorgram.extract("/Users/zeynep/Desktop/100daysOfCode/day18/hirst_painting/hirstPainting.jpg", 65)

# colors_list = []
# for color in colors:
#     #print(i)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = f"#{r:02X}{g:02X}{b:02X}"
#     colors_list.append(new_color)

colors_list = ['#FDFDFC', '#F2F4F7', '#F1F7F3', '#904C32', '#BCA575', '#F8F4F6', '#A69924', '#0E2E55', '#8BB9B0', 
 '#923851', '#2A6E88', '#3B7863', '#91AAB1', '#57231E', '#4098A9', '#DCD15D', '#6E251F', '#64916F', '#A56383', 
 '#5B7AAC', '#9E8A9E', '#B16852', '#373455', '#CEB6C3', '#44303F', '#493347', '#ADC9C2', '#AFC6C9', '#D5B6B0', 
 '#252F2D', '#0E656D', '#BCBEC9', '#0B7068', '#41423A']

timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

# def skip_line():
#     timmy.setheading(90)
#     timmy.forward(50)
#     timmy.setheading(180)
#     timmy.forward(500)
#     timmy.setheading(0)

# def draw_line():
#     for _ in range(10):
#         timmy.dot(20, random.choice(colors_list))
#         timmy.forward(50)

# for _ in range(10):
#     draw_line()
#     skip_line()

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(colors_list))
    timmy.forward(50)

    if dot_count%10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()
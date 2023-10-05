import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "day25/us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

statesCsv = pandas.read_csv("day25/us-states-game/50_states.csv")
states_name = statesCsv["state"].to_list()
#print(states_name)

guessed_states = []
while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states) }/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states_name:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("day25/us-states-game/missing_states.csv")
        break

    if (answer_state in states_name):
        guessed_states.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = statesCsv[answer_state == statesCsv.state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, align="center", font=("Helvetica",8, "normal"))
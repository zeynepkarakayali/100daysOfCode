from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto((-280, 260))
        self.write(f"SCORE: {self.score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=FONT)
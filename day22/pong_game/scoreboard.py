from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Helvetica", 18, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto((0, 270))
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write(f"{self.l_score} : SCORES : {self.r_score}",align=ALIGNMENT, font=FONT)

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.write(f"{self.l_score} : SCORES : {self.r_score}",align=ALIGNMENT, font=FONT)

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.write(f"{self.l_score} : SCORES : {self.r_score}",align=ALIGNMENT, font=FONT)

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self, shape = "square", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 550)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} {" " * 10} | {" " * 10} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()


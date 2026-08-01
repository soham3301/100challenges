
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, left_player, right_player):
        super().__init__()
        self.left_player = left_player
        self.right_player = right_player
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 400)
        self.write(f"{self.left_player}: {self.left_score}", align="center", font=("Courier", 30, "normal"))
        self.goto(200, 400)
        self.write(f"{self.right_player}: {self.right_score}", align="center", font=("Courier", 30, "normal"))

    def left_point(self):
        self.left_score += 1

    def right_point(self):
        self.right_score += 1
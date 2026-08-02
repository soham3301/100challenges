
from turtle import Turtle
STARTING_POSITION = (0, -570)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 570


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def goto_starting_position(self):
        self.goto(STARTING_POSITION)

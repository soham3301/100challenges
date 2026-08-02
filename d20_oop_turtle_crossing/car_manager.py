
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 1.05


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.color(random.choice(COLORS))
        self.starting_y_cor = random.randint(-530, 530)
        self.starting_move_distance = 5
        self.goto(470, self.starting_y_cor)

    def move(self):
        self.goto(self.xcor() - self.starting_move_distance, self.starting_y_cor)

    def speed_up(self):
        self.starting_move_distance *= MOVE_INCREMENT

from turtle import Turtle, Screen
import random

class Food(Turtle):
    def __init__(self, shape = "circle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-460, 460)
        random_y = random.randint(-570, 570)
        self.goto(random_x, random_y)




from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_cor_value = 10
        self.y_cor_value = 10

    def move(self):
        new_x = self.xcor() + self.x_cor_value
        new_y = self.ycor() + self.y_cor_value
        self.goto(new_x, new_y)

    def bounce_verticle(self):
        self.y_cor_value = -self.y_cor_value

    def bounce_horizontal(self):
        self.x_cor_value = -self.x_cor_value

    def reset_position(self):
        self.goto(0, 0)
        self.x_cor_value = 10
        self.y_cor_value = 10
        self.bounce_horizontal()

    def speed_up(self):
        self.x_cor_value *= 1.05
        self.y_cor_value *= 1.05

from turtle import Screen
from puddle import Puddle

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)

puddle_right = Puddle(450)

puddle_left = Puddle(-450)

screen.listen()

screen.onkey(puddle_right.go_up, "Up")
screen.onkey(puddle_right.go_down, "Down")

screen.onkey(puddle_left.go_up, "w")
screen.onkey(puddle_left.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()



















screen.exitonclick()
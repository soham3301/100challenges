
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)

left_player_name = input("Enter First Player Name: ").title()
right_player_name = input("Enter Second Player Name: ").title()

paddle_right = Paddle(450)
paddle_left = Paddle(-450)
ball = Ball()
scoreboard = Scoreboard(left_player_name, right_player_name)

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    #? Detect Up and Down Wall Collision
    if ball.ycor() > 570 or ball.ycor() < -570:
        ball.bounce_verticle()

    #? Detect Collision with Paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 430 or ball.distance(paddle_left) < 50 and ball.xcor() < -430:
        ball.bounce_horizontal()
        ball.speed_up()

    #? Detect Right Side Paddle Misses
    if ball.xcor() > 470:
        ball.reset_position()
        scoreboard.left_point()
        scoreboard.update_scoreboard()

    #? Detect Left Side Paddle Misses
    if ball.xcor() < -470:
        ball.reset_position()
        scoreboard.right_point()
        scoreboard.update_scoreboard()
        
    



















screen.exitonclick()
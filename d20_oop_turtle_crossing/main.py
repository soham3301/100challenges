import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)

player = Player()
score_baord = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

all_cars = []

car_generator_counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_generator_counter += 1

    if car_generator_counter % 6 == 0:
        all_cars.append(CarManager())

    if all_cars:
        for car in all_cars:
            car.move()

    if all_cars:
        for car in all_cars:
            if car.distance(player) < 20:
                score_baord.game_over()
                game_is_on = False

    if player.ycor() > 570:
        score_baord.score_up()
        score_baord.update_scoreboard()
        player.goto_starting_position()
        for cars in all_cars:
            cars.speed_up()

            
screen.exitonclick()

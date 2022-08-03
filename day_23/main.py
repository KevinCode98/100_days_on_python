import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
car = CarManager()
cars = [car]
player = Player()
CARS = 8

screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if random.randint(0, CARS) == 1:
        car = CarManager()
        cars.append(car)

    for car in cars:
        car.move()

    # Detect collision with a wall.
    if player.ycor() > 280:
        scoreboard.pass_level()
        player.move_start()
        car.pass_level()
        if random.randint(0, 1) == 1:
            CARS -= 1

    # Detect collision with car.
    for car in cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

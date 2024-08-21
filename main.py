import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_mgr = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    if loop_count % 6 == 0:
        car_mgr.create_car()

    car_mgr.move_cars()

    for game_car in car_mgr.cars:
        if player.distance(game_car) < 25:
            # at distance = 33, the game stops at first contact with turtle body
            game_is_on = False
            scoreboard.game_over()

        if player.reach_finish_line():
            player.reset_position()
            car_mgr.increase_speed()
            scoreboard.level_up()
    loop_count += 1
    screen.update()

screen.exitonclick()

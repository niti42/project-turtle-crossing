from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.moving_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle(shape="square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto((300, random.choice(range(-250, 250))))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.moving_distance)
            # if car reaches -300 on the x axis, remove it from the list self.cars
            if car.xcor() < -300:
                # Remove the car from the list
                self.cars.remove(car)
                # Optionally, you can also clear the car from the screen:
                car.hideturtle()

    def increase_speed(self):
        self.moving_distance += MOVE_INCREMENT

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color("black")
        self.goto((-295, 250))
        self.hideturtle()
        self.update_scoreboard()

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", font=FONT, align='left')

    def game_over(self):
        self.goto((0, 0))
        self.write("GAME OVER", align='center', font=FONT)

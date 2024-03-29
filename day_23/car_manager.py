from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = -10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(280, random.randint(-230, 230))

    def move(self):
        new_x = self.xcor() + random.randint(MOVE_INCREMENT, -1)
        self.goto(new_x, self.ycor())

    def pass_level(self):
        global MOVE_INCREMENT
        MOVE_INCREMENT -= 5

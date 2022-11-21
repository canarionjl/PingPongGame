from turtle import Turtle
import random

HORIZONTAL_POSITION = 25
VERTICAL_POSITION = 25

ORIENTATIONS = [45, 315, 135, 225]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.angle = None
        self.define_ball()

    def define_ball(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("white")
        self.generate_location()

    def generate_location(self):
        self.goto(random.randint(-HORIZONTAL_POSITION, HORIZONTAL_POSITION),
                  random.randint(-VERTICAL_POSITION, VERTICAL_POSITION))
        self.angle = (random.choice(ORIENTATIONS))
        self.setheading(self.angle)

    def move(self):
        self.change_heading(False)
        self.forward(10)

    def collapse(self):
        self.change_heading(True)
        self.forward(10)

    def change_heading(self, collapse):
        if self.heading() == 45:
            if self.ycor() >= 245:
                self.angle = 315
            elif collapse:
                self.angle = 135
        elif self.heading() == 315:
            if self.ycor() <= -245:
                self.angle = 45
            elif collapse:
                self.angle = 225
        elif self.heading() == 225:
            if self.ycor() <= -245:
                self.angle = 135
            elif collapse:
                self.angle = 315
        elif self.heading() == 135:
            if self.ycor() >= 245:
                self.angle = 225
            elif collapse:
                self.angle = 45
        self.setheading(self.angle)

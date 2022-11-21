from turtle import Turtle

PADDLE_LENGTH = 3


class Paddle:

    def __init__(self, location):
        self.paddle = []
        self.create_paddle(location)

    def create_paddle(self, location):
        location_ = location.lower()
        detour = int(PADDLE_LENGTH / 2)
        y_cor = 20 * detour
        x_cor = 370
        if location_ == "left":
            x_cor *= -1
        elif location_ != "right":
            pass
        for i in range(0, PADDLE_LENGTH):
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(x_cor, y_cor)
            new_turtle.shape("square")
            y_cor -= 20
            self.paddle.append(new_turtle)

    def up(self):
        if self.paddle[0].ycor() < 210:
            self.move(1)

    def down(self):
        if self.paddle[-1].ycor() > -210:
            self.move(-1)

    def move(self, up_or_down):
        for square in self.paddle:
            square.sety(square.ycor() + up_or_down * 40)

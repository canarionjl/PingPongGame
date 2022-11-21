from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time


def configure_screen(screen_):
    screen_.setup(width=900, height=700)
    screen_.bgcolor("black")
    screen_.title("Ping Pong Game")
    screen_.tracer(0)
    create_border_square()


def create_border_square():
    sign = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    hor_border_value = 400
    ver_border_value = 250
    border = Turtle()
    border.color("white")
    border.penup()
    border.goto(hor_border_value * sign[-1][0], ver_border_value * sign[-1][1])
    border.pendown()
    for sign_ in sign:
        border.goto(hor_border_value * sign_[0], ver_border_value * sign_[1])
    border.penup()
    border.goto(0, 245)
    border.right(90)
    while border.ycor() > -250:
        border.pendown()
        border.forward(10)
        border.penup()
        border.forward(10)
    border.hideturtle()


screen = Screen()
configure_screen(screen)

screen.listen()
scoreboard = Scoreboard()
left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball = Ball()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "W")
screen.onkey(left_paddle.down, "S")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.05)

    # Detect collision between paddle and ball
    for square in left_paddle.paddle:
        if square.distance(ball) <= 15:
            ball.collapse()
    for square in right_paddle.paddle:
        if square.distance(ball) <= 15:
            ball.collapse()

    # Detect if someone scores
    scorer = ""
    score = False
    if ball.xcor() > 390:
        scorer = "right"
        score = True
    elif ball.xcor() < -390:
        scorer = "left"
        score = True
    if score:
        ball.generate_location()
        scoreboard.update_score(scorer)
        scoreboard.notify_score(scorer)
        time.sleep(0.1)

    # Detect if someone wins
    if scoreboard.left_score >= 2 or scoreboard.right_score >= 2:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()

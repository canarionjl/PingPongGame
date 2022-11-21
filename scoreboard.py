from turtle import Turtle

FONT = ('Arial', 30, 'bold')
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")

        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 275)
        self.write(f"{self.left_score} : {self.right_score}", move=False, align=ALIGNMENT, font=FONT)

    def notify_score(self, scorer):
        self.goto(0, -315)
        self.write(f"The {scorer} paddle has scored one point", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self, scorer):
        if scorer == "left":
            self.left_score += 1
        elif scorer == "right":
            self.right_score += 1
        self.clear()
        self.notify_score(scorer)
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.update_scoreboard()
        self.goto(0, -315)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)



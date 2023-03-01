from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 15, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write(arg=f"Current score: {self.score}", move=False, align=ALIGN, font=FONT)

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Current score: {self.score}", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game over", move=False, align=ALIGN, font=FONT)
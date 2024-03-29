from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 15, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Current score: {self.score} High score: {self.high_score}", move=False, align=ALIGN, font=FONT)

    def refresh_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            with open("score.txt", mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

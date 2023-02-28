from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.color("dark blue")
        self.refresh()

    def refresh(self):
        cord_x = random.randint(-280, 280)
        cord_y = random.randint(-280, 280)
        self.goto(cord_x, cord_y)

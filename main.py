from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()

scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detects if the snake hits the food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.refresh_score()

    # Detects if the snake hits the wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    # Detects if the snake hits its own tail.
    for seg in snake.segments[1:]:

        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()

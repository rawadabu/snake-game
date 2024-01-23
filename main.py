from turtle import Screen, Turtle

from score_board import ScoreBoard
from food import Food
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game 🐍")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
game_in_on = True
while game_in_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Collusion with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # Collusion with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor(
    ) > 280 or snake.head.ycor() < -280:
        game_in_on = False
        score_board.game_over()

    # Collusion with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_in_on = False
            score_board.game_over()

screen.exitonclick()

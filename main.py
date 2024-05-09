from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)  # update the green every 0 frames
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect food and extend and update score
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect wall collision and change position
    if snake.head.xcor() > 310 or snake.head.xcor() < -310:
        snake.head.goto(-(snake.head.xcor()), snake.head.ycor())
    elif snake.head.ycor() > 310 or snake.head.ycor() < -310:
        snake.head.goto(snake.head.xcor(), -snake.head.ycor())

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.snake_reset()
            screen.update()

screen.exitonclick()

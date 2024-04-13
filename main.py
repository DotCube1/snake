from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 800)
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Scoreboard()
game_on = True

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left_side, "Left")
screen.onkey(snake.right_side, "Right")

while game_on:
    screen.update()
    sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.snake_increase()
        food.refresh()

    if snake.head.xcor() > 385 or snake.head.xcor() < -385 or snake.head.ycor() > 385 or snake.head.ycor() < -385:
        snake.reset()
        score.reset()

    for segments in snake.snake_body:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()

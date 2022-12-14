import time
from turtle import *
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')

screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(snake.goUp, 'Up')
screen.onkey(snake.goDown, 'Down')
screen.onkey(snake.goLeft, 'Left')
screen.onkey(snake.goRight, 'Right')
screen.onkey(bye, 'Escape')

def end_game():
  # game_loop = False
  # scoreboard.game_over()
  scoreboard.reset()
  snake.reset()
  food.spawn()

game_loop = True
while game_loop:
  time.sleep(0.1)
  screen.update()
  snake.move()

  if snake.head.distance(food) < 15:
    snake.eat()
    food.spawn()
    scoreboard.increase_score()

  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    end_game()
  
  if snake.head.distance(snake.tail) < 15:
    end_game()

screen.exitonclick()

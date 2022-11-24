import time
from turtle import *
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title('Why did the turtle cross the road?')
screen.bgcolor('lightgray')
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()
screen.update()

screen.onkey(player.move_forward, 'Up')
screen.onkey(player.move_backward, 'Down')
screen.onkey(bye, 'Escape')
screen.listen()

game_loop = True
while game_loop:
  time.sleep(0.1)
  carManager.start()
  screen.update()

  if player.completed_level():
    player.level_up()
    scoreboard.level_up()
    carManager.level_up()

  for car in carManager.cars:
    if player.distance(car) < 40:
      game_loop = False
      scoreboard.game_over()

screen.exitonclick()

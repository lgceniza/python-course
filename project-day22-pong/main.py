import time
from turtle import *
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

STARTING_POSITION_A = (350, 0)
STARTING_POSITION_B = (-350, 0)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG')

screen.tracer(0)
r_paddle = Paddle(STARTING_POSITION_A)
l_paddle = Paddle(STARTING_POSITION_B)
ball = Ball()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(l_paddle.goUp, 'w')
screen.onkey(l_paddle.goDown, 's')
screen.onkey(r_paddle.goUp, 'Up')
screen.onkey(r_paddle.goDown, 'Down')
screen.onkey(bye, 'Escape')

game_loop = True
while game_loop:
  time.sleep(0.1)
  screen.update()
  ball.move()

  x = ball.xcor()
  y = ball.ycor()

  if y > 275 or y < -275:
    ball.bounce()
  
  if (x > 325 and ball.distance(r_paddle) < 50) or (x < -320 and ball.distance(l_paddle) < 50):
    ball.wall_bounce()

  if x > 380 or x < -380:
    ball.reset_position()
    scoreboard.add_point('r' if x < 0 else 'l')


screen.exitonclick()
from turtle import *

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.color('white')
    self.penup()

    self.x_move = 15
    self.y_move = 15

  def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move

    self.goto(new_x, new_y)

  def bounce(self):
    self.y_move *= -1

  def wall_bounce(self):
    self.x_move *= -1

  def reset_position(self):
    self.goto(0,0)
    self.wall_bounce()

from turtle import *

class Paddle(Turtle):
  def __init__(self, pos):
    super().__init__()
    self.shape('square')
    self.color('white')
    self.shapesize(5,1)
    self.penup()
    self.goto(pos)
  
  def goUp(self):
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)

  def goDown(self):
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)

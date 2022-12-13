from turtle import Turtle

STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 250


class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('turtle')
    self.shapesize(2,2)
    self.color('green')
    self.penup()
    self.seth(90)
    self.goto(STARTING_POSITION)

  def move_forward(self):
    self.forward(MOVE_DISTANCE)

  def move_backward(self):
    self.backward(MOVE_DISTANCE)

  def completed_level(self):
    return self.ycor() > FINISH_LINE_Y
  
  def level_up(self):
    self.goto(STARTING_POSITION)

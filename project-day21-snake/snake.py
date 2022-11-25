from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()

  def add_segment(self, position):
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    self.segments.append(segment)

  def create_snake(self):
    for pos in STARTING_POSITIONS:
      self.add_segment(pos)

    self.head = self.segments[0]    
    self.tail = self.segments[-1]
  
  def reset(self):
    self.segments = [_.reset() for _ in self.segments]
    self.__init__()

  def eat(self):
    old_x = self.segments[-1].xcor()
    old_y = self.segments[-1].ycor()
    self.add_segment((old_x, old_y))

    self.tail = self.segments[-1]

  def move(self):
    for seg in range(len(self.segments)-1, 0, -1):
      new_x = self.segments[seg-1].xcor()
      new_y = self.segments[seg-1].ycor()
      self.segments[seg].goto(new_x, new_y)
    
    self.segments[0].forward(MOVE_DISTANCE)
  
  def goUp(self):
    if self.segments[0].heading() != DOWN:
      self.segments[0].seth(UP)

  def goDown(self):
    if self.segments[0].heading() != UP:
      self.segments[0].seth(DOWN)

  def goLeft(self):
    if self.segments[0].heading() != RIGHT:
      self.segments[0].seth(LEFT)

  def goRight(self):
    if self.segments[0].heading() != LEFT:
      self.segments[0].seth(RIGHT)

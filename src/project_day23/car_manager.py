import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "gray", "blue", "purple"]
Y_POSITIONS = [-200, -150, -100, -50, 0, 50, 100, 150, 200, 250]
HEADINGS = [0, 180]
NUMBERS_OF_CARS = 20
START_MOVEMENT = 5
MOVE_INCREMENT = 10


class Car(Turtle):
  def __init__(self):
    super().__init__('square')
    self.shapesize(2,3.5)
    self.color(random.choice(COLORS))
    self.penup()
    self.seth(random.choice(HEADINGS))
    self.goto(random.randint(-300,300), random.choice(Y_POSITIONS))

    self.move = START_MOVEMENT

  def level_up(self):
    self.goto(random.randint(-300,300), random.choice(Y_POSITIONS))
    self.move += MOVE_INCREMENT


class CarManager():
  def __init__(self):
    self.cars = []

    for _ in range(NUMBERS_OF_CARS):
      car = Car()
      self.cars.append(car)

  def start(self):
    for car in self.cars:
      car.forward(car.move)
      
      if car.xcor() > 270 or car.xcor() < -270:
        car.move *= -1
  
  def level_up(self):
    for car in self.cars:
      car.level_up()

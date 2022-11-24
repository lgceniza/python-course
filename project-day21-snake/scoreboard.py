from turtle import *

FONT = ('Arial', 16, 'normal')


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()

    self.score = 0
    self.color('white')
    self.hideturtle()
    self.penup()
    self.goto(0, 270)
    self.displayScore()
  
  def displayScore(self):
    self.write(arg=f'Score: {self.score}', align='center', font=FONT)

  def increase_score(self):
    self.score += 1
    self.clear()
    self.displayScore()
  
  def game_over(self):
    self.goto((0,0))
    self.write(arg='GAME OVER!', align='center', font=FONT)

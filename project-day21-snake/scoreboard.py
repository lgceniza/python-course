from turtle import Turtle

FONT = ('Arial', 16, 'normal')


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color('white')
    self.hideturtle()
    self.penup()
    self.goto(0, 270)

    self.score = 0
    with open('score.txt') as f:
      self.high_score = int(f.readline())
    self.displayScore()
  
  def displayScore(self):
    self.write(arg=f'Score: {self.score} | High Score: {self.high_score}', align='center', font=FONT)

  def increase_score(self):
    self.score += 1
    self.clear()
    self.displayScore()
  
  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open('score.txt', 'w') as f:
        f.write(str(self.high_score))
    self.score = 0
    self.clear()
    self.displayScore()

  def game_over(self):
    self.goto((0,0))
    self.write(arg='GAME OVER!', align='center', font=FONT)

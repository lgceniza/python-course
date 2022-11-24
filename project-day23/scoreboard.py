from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.hideturtle()

    self.level = 1
    self.displayScore()

  def displayScore(self):
    self.goto(-280, 270)
    self.write(f"Level: {self.level}", align='left', font=FONT)

  def level_up(self):
    self.level += 1
    self.clear()
    self.displayScore()

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER!", align='center', font=FONT)

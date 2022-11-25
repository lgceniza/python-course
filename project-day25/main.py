import time
from turtle import *
import pandas as pd

STATES = 50
STATES_DF = pd.read_csv('50_states.csv')

def checkState(state: str):
  return state in STATES_DF['state'].to_list()

def getCoordinates(state: str):
  x = STATES_DF[STATES_DF['state']==state]['x'].values[0]
  y = STATES_DF[STATES_DF['state']==state]['y'].values[0]
  return int(x), int(y)


screen = Screen()
screen.bgpic('blank_states_img.gif')
screen.setup(725,491)
screen.tracer(0)

screen.listen()
screen.onkey(bye, 'Escape')

time.sleep(1)

correctly_guessed = 0
while correctly_guessed < STATES:
  guess = screen.textinput(f"{correctly_guessed}/{STATES} States Correct", "Give the name of a US state.")
  guess = ' '.join(list(map(lambda _: _.capitalize(), guess.split())))

  if checkState(guess):
    correctly_guessed += 1

    state = Turtle(visible=False)
    state.penup()
    state.goto(getCoordinates(guess))
    state.write(guess, align='center')
    screen.update()
  
  time.sleep(1)

screen.exitonclick()

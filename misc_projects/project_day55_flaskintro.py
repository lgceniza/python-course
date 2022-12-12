import random
from flask import Flask

app = Flask(__name__)

RANDOM_NUMBER = random.randint(0,9)

@app.route('/')
def home():
  return "<h1>Guess a number between 0 and 9</h1>" \
    "<img src='https://media.giphy.com/media/KxiCRZLuQTTaP1aHov/giphy.gif'>"

@app.route("/<int:number>")
def result(number):
  if number < RANDOM_NUMBER:
    html = "Too low, try again!<br><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
  elif number > RANDOM_NUMBER:
    html = "Too high, try again!<br><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'"
  else:
    html = "You found me!<br><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
  return f"<h1>{html}</h1>"

if __name__ == "__main__":
  app.run(debug=True)

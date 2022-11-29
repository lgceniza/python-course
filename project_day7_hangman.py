import random

def print_word(word, guessed, stage):
  print(stage)
  for c in word:
    if c in guessed:
        print(f"{c} ", end='')
    else:
      print('_ ', end='')
  print("\n")

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

letters = len(chosen_word)
guessed = []
lives = 6

print('_ ' for i in range(letters))

print(f"Welcome to Hangman!\n{stages[lives]}")

while letters > 0:
  guess = input("Guess a letter: ")

  if guess in " \t\n":
    continue
  elif guess in chosen_word:
    print('Hit!')
    letters -= chosen_word.count(guess)
    guessed.append(guess)
  else:
    lives -= 1
    if lives > 0:
      print('Try again.')
    else:
      break
  
  print_word(chosen_word, guessed, stages[lives])

if letters == 0:
  print("You win!")
else:
  print_word(chosen_word, guessed, stages[lives])
  print("You lost.")
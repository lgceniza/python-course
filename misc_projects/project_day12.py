import random

MODE_GUESSES = {
  'easy': 10,
  'hard': 5
}

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
guesses = MODE_GUESSES[difficulty]
number = random.randint(1,100)
win = False

while guesses > 0 and not win:
  print(f"You have {guesses} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  guesses -= 1

  if guess == number:
    print(f"The number is {number}! You got it right!")
    win = True
  elif guess > number:
    print("Too high!")
  else:
    print("Too low!")

if not win:
  print("You ran out of attempts! You lose!")
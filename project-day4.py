import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
print(f"{choices[userChoice]}\n")

pcChoice = random.randint(0,2)
print(f"Computer chose:\n{choices[pcChoice]}")

message = "You win"
if userChoice == pcChoice:
  message = "It's a draw"
elif (userChoice == 0 and pcChoice == 1) or (userChoice == 1 and pcChoice == 2) or (userChoice == 2 and pcChoice == 0):
  message = "You lose"

print(message)
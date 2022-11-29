print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossroad1 = input("Do you want to go left or right? ").lower()
if crossroad1 != "left":
  print("You fell into a hole. Game over.")
  exit()

crossroad2 = input("You enter a boat and it moves away from the island. Do you swim or wait? ").lower()
if crossroad2 != "wait":
  print("You were attacked by a trout. Game over.")
  exit()

crossroad3 = input("You explore the boat and see three doors: yellow, red, and blue. Which door do you choose? ").lower()
if crossroad3 == "red":
  print("A gas tank exploded inside the room and you are burned by fire. Game over.")
elif crossroad3 == "blue":
  print("The room is brimming with beasts, and one eats you. Game over.")
elif crossroad3 == "yellow":
  print("You found the treasure! You win!")
else:
  print("A pirate comes up behind you and knocks you out. Game over.")
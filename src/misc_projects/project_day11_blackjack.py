import random, os

def deal_card(cards):
  return random.choice(cards)

def get_score(cards):
  return sum(cards)

def has_ace(cards):
  return 11 in cards

def has_blackjack(cards):
  hasBlackjack = False
  if has_ace(cards) and get_score(cards) == 21:
    hasBlackjack = True
  return hasBlackjack

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def game():
  user = [deal_card(cards) for i in range(2)]
  computer = [deal_card(cards) for i in range(2)]

  user_loop = True
  computer_loop = True
  outcome = False

  if has_blackjack(user):
    print(f"Your cards: {user}")
    print(f"Computer's cards: {computer}")
    if has_blackjack(computer):
      pass
    else:
      outcome = True
    user_loop = False
    computer_loop = False

  while user_loop:
    if get_score(user) > 21 and has_ace(user):
      user.remove(11)
      user.append(1)

    if get_score(user) > 21:
      outcome = False
      computer_loop = False
      break

    print(f"Your cards: {user}")
    print(f"Computer's card (1 hidden): {computer[0]}")
    if input("Do you want to draw another card? Y or N: ") == "Y":
      user.append(deal_card(cards))
    else:
      user_loop = False
  
  while computer_loop:
    print(f"Your cards: {user}")
    print(f"Computer's cards: {computer}")
    if get_score(computer) < 17:
      computer.append(deal_card(cards))
    else:
      computer_loop = False

  if get_score(user) <= 21 and (get_score(computer) > 21 or get_score(user) > get_score(computer)):
    outcome = True
  elif get_score(user) == get_score(computer):
    outcome = "Draw!"

  print(f"Your cards: {user}")
  print(f"Computer's cards: {computer}")

  return outcome

game_loop = True
while game_loop:
  outcome = game()
  print("You win!" if outcome else "You lose!" or outcome)

  if input("\nDo you want to play again? Y or N: ") == "Y":
    os.system('clear')
  else:
    game_loop = False
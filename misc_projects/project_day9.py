import os

bids = {}
loop = True

while loop:
  name = input("What is your name? ")
  bid = int(input("What's your bid? "))

  bids[name] = bid

  loop = True if input("Are there any other bidders? Y or N: ") == "Y" else False
  os.system('clear')

max = 0
key = ""
for bid in bids:
  if bids[bid] > max:
    key = bid
    max = bids[bid]
print(f"The winner is {key} with a bid of ${bids[key]}.")
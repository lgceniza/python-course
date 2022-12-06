print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))/100 + 1
people = int(input("How many people to split the bill? "))

perperson = format((total_bill/people) * tip,'.2f')
print(f"Each person should pay: ${perperson}")
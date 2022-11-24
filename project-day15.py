MENU = {
  "espresso": {
    "ingredients": {
      "water": 50,
      "coffee": 18,
    },
    "cost": 1.5,  
  },
  "latte": {
    "ingredients": {
      "water": 200,
      "milk": 150,
      "coffee": 24,
    },
    "cost": 2.5,
  },
  "cappuccino": {
    "ingredients": {
      "water": 250,
      "milk": 100,
      "coffee": 24,
    },
    "cost": 3.0,
  }
}

RESOURCES_UNIT = {
  "water": 'ml',
  "milk": 'ml',
  "coffee": 'g',
}

resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
}

money = 0
is_sufficient = True

while True:
  coffee = input("What would you like? (espresso/latte/cappuccino): ")

  if coffee == "off":
    break
  elif coffee == "report":
    for resource in resources:
      print(f"{resource.title()}: {resources[resource]}{RESOURCES_UNIT[resource]}")
    print(f"Money: ${money}")
  else:
    ingredients = MENU[coffee]['ingredients']
    for resource in ingredients:
      if resources[resource] < ingredients[resource]:
        is_sufficient = False
        print(f"Sorry, there is not enough {resource}.")
    
    if is_sufficient:
      print("Please insert coins.")
      quarters = int(input("How many quarters? "))
      dimes = int(input("How many dimes? "))
      nickles = int(input("How many nickles? "))
      pennies = int(input("How many pennies? "))

      payment = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
      cost = MENU[coffee]['cost']

      if payment < cost:
        print("Sorry, that's not enough money. Money refunded.")
      else:
        money += payment
        for resource in ingredients:
          resources[resource] -= ingredients[resource]

        print("" if cost == payment else f"Here is ${payment - cost} in change.")
        print(f"Here is your {coffee}. Enjoy!")
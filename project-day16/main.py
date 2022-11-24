from resource import Resource, dictToResources
from coffee import Coffee
from coffee_machine import CoffeeMachine

from constants import RESOURCES, RESOURCES_UNIT, MENU

def start(coffeeMachine):
  coffee = input("What would you like? (espresso/latte/cappuccino): ")

  if coffee == "off":
    coffeeMachine.turnOff()
  elif coffee == "report":
    coffeeMachine.report()
  else:
    coffeeMachine.orderCoffee(coffee)

    if coffeeMachine.checkResources():
      print("Please insert coins.")
      quarters = int(input("How many quarters? "))
      dimes = int(input("How many dimes? "))
      nickles = int(input("How many nickles? "))
      pennies = int(input("How many pennies? "))

      if coffeeMachine.receivePayment(quarters, dimes, nickles, pennies):
        coffeeMachine.makeCoffee()
      else:
        print("Sorry, that's not enough money. Money refunded.")
  
  start(coffeeMachine)


coffeeMachine = CoffeeMachine()
for resource in ['water', 'milk', 'coffee']:
  coffeeMachine.addResource(Resource(resource, RESOURCES[resource], RESOURCES_UNIT[resource]))
for coffee in ['espresso', 'latte', 'cappuccino']:
  ingredients = dictToResources(MENU[coffee]['ingredients'])
  coffeeMachine.addCoffee(Coffee(coffee, ingredients, MENU[coffee]['cost']))


start(coffeeMachine)
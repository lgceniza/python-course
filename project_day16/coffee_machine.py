class CoffeeMachine():
  def __init__(self, money=0):
    self.coffees = {}
    self.resources = {}
    self.money = money
    self.coffee = None

  def addCoffee(self, coffee):
    self.coffees[coffee.name] = coffee
  
  def getCoffee(self, coffeeName):
    return self.coffees[coffeeName]

  def addResource(self, resource):
    self.resources[resource.name] = resource

  def orderCoffee(self, coffeeName):
    self.coffee = self.coffees[coffeeName]

  def turnOff(self):
    exit()
  
  def report(self):
    for resource in self.resources:
      print(self.resources[resource].reportResource())
    print(f"Money: ${self.money}")
  
  def checkResources(self):
    for resource in self.coffee.ingredients:
      if self.resources[resource].amount < self.coffee.getIngredient(resource).amount:
        print(f"Sorry, there is not enough {resource}.")
        return False
    
    return True
  
  def receivePayment(self, q, d, n, p):
    payment = 0.25 * q + 0.10 * d + 0.05 * n + 0.01 * p
    cost = self.coffee.getCost()

    if payment < cost:
      return False
    
    self.money += payment
    print("" if cost == payment else f"Here is ${payment - cost} in change.")
    print(f"Here is your {self.coffee.getName()}. Enjoy!")
    return True
  
  def makeCoffee(self):
    for resource in self.coffee.ingredients:
      self.resources[resource].amount -= self.coffee.getIngredient(resource).amount

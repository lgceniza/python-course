class Coffee():
  def __init__(self, name, ingredients, cost):
    self.name = name
    self.ingredients = ingredients
    self.cost = cost
  
  def getName(self):
    return self.name
  
  def getIngredient(self, ingredientName):
    return self.ingredients[ingredientName]

  def getCost(self):
    return self.cost

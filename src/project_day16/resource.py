from constants import RESOURCES_UNIT

class Resource():
  def __init__(self, name, amount, unit = ''):
    self.name = name
    self.amount = amount
    self.unit = unit
  
  def reportResource(self):
    return f"{self.name}: {self.amount}{self.unit}"

def dictToResources(dic):
  resources = {}
  for key in dic.keys():
    resources[key] = Resource(key, dic[key], RESOURCES_UNIT[key])

  return resources

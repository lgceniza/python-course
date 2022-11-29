def add(a, b):
  return a + b
def subtract(a, b):
  return a - b
def multiply(a, b):
  return a * b
def divide(a, b):
  return a / b

operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide
}

def calculator():
  loop = True
  x = int(input("What's the first number? "))

  while loop:
    y = int(input("What's the second number? "))
    for c in list(operations.keys()):
      print(c)
    op = input("Pick an operation: ")
    result = operations[op](x, y)
    print(f"{x} {op} {y} = {result}")

    loop = True if input("Continue calculating with this result? Y or N: ") == "Y" else False
    x = result
  
  if not loop:
    if input("Do you want to start a new calculation? Y or N: ") == "Y":
      calculator()
    exit()

calculator()
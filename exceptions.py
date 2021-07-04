import sys

try:
  x = int(input("x: "))
  y = int(input("y: "))
except ValueError:      # This is to avoid any string division
  print("Error: Value should be in numbers")
  sys.exit(1)

try:
  result = x / y
except ZeroDivisionError:   # This is to avoid division by 0
  print("Error: Cannot be divided by 0.")
  sys.exit(1)


print(f"{x} / {y} = {result}")
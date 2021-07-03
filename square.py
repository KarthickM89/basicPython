# One method of importing
from functions import square

for i in range(5):
  print(f"The square of {i} is {square(i)}")

# Another method of importing
import functions

for i in range(10):
  print(f"square of {i} is {functions.square(i)}")
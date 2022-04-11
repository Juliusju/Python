# Exceptions in python

import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError as e:
    print("Error: Invalid input", e)
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError as e:
    print("Error!: Cannot divide by 0", e)
    sys.exit(1)


print(f"{x} divided by {y} is {result}  ")

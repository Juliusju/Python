# To use a function that you have written in another code, you just have to import it

from Functions import square

for i in range(6):
    print(f"The square of {i} is {square(i)}")
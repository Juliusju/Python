# A function to print the required timetable to the user

print("The purpose of this program is to help you find the multiplication table of any number")
num = int(input("Please enter any number to find its corresponding timetable: "))
def timesTable(x):
    for y in range(1, 13):
        print(x, "*", y, "=", x * y,)
print(timesTable(num))
""""

# A function to the maximum number among the numbers entered by the user:
#def findMax(x):
  #  num = input("enter a number a to find the max among them: ")
sum = 0
for i in range(1, 12):
    rainfall[i] = float(input("enter the rainfall for the month ",i + 0))
    sum = sum + rainfall[i]
print(f"the total rainfall for the this year is {sum}")


# The lambda function: Syntax lambda a:a
x = lambda a:a
print(x(3))

# A function that doubles the number inputted

def foo(n):
  return lambda a:a * n
doubler = foo(2)
print(doubler(5))

"""

# Classes in Python
# To define a class, use the keyword class to let the compiler know that you using a class

#from _typeshed import Self


class Person:
  def __init__(myName, name, age):
    myName.name = name
    myName.age = age
x = Person("Julius", 23)#creating an object from the person class
print(f"Your name is {x.name} and you are {x.age} years old ")

class myClass:
  pass
 

class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def function(self):
      print(f"Hello my name is {self.name}")
p1 = Person1("serious", 45)
p1.function()

def square(x):
  return x * x

sum = 0
list1 = []
for i in range(1, 13):
    rainfall = float(input(f"enter the rainfall for the {i} month "))
    sum = sum + rainfall
    list1.append(rainfall)
print(f"the total rainfall for the this year is {sum}")  
print(list1)



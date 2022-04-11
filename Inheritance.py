# Inheritance allows to define a class that inherits all the methods and properties fron another class
# Parent class is the class being inherited from  and is also called the base class
# Child class is the class that inherits from another class and is called the derived class

# Example:: Create a class named Person, with lastname and firstname properties and printname method

class Person:
    def __init__(self, lname, fname, year):
        self.lname = lname
        self.fname = fname
        self.graduationyear = year
    def printname(self):
        print(self.fname, self.lname)
p1 = Person("Agbame", "Julius",345) # p1 is the object created from the Person class
p1.printname() # printname method will be executed on the p1 object


# To create a child class that inherits the functionality of another class, send the parent class as a parameter 
# when creating  the child class

class Student(Person):
    def __init__(self, lname, fname, year):# When you add the __init__() function in the child class then it will not inherit the parent's init function 
        super().__init__(self, lname, fname)# To keep the inheritance of the parent's init function, add call to the parent's init function.
        # Or you can also use the super function in the child class to keep the inheritance of the parent class
        # like super().__init__():
        
x = Student("Awagah", "Alimatu", 2034 )
x.printname()

        
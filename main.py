# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

'''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#Dictionary. We use curly braces to let the compiler know that we dealing with dictionary
#dictionary takes a key and value pair. The key is separated from the value with a colon:

myDict = {"Julius":
              {"School":"UCC", "Age" : 25, "Hall":"Nkrumah Hall"},
          "Ben": {"School":"Legon", "Age" : 23, "Hall":"CommonWealth Hall"}}
#print(myDict.values()) #This is one is to let you know the values in the dictionary.
#print(myDict.keys())
#print(myDict.items())
Name = input("please enter your name: ")
print(myDict[Name]["Age"])
#if Name in myDict:
   # print("Welcome Mr.{}".format(Name))
   # NameAdd = input("please would you like to keep your name in our database (y/): ")

Database = {"UserName":"Seriousel", "Password":"serious123"}
Username = input("Please enter your username: ")
Password = input("Please enter your password: ")
if Username or Password in Database.values():
    print("Welcome Mr.{}".format(Username))
else:
    print("Sorry Password or username does not match.\n"
          "******************************************88"
          "Would you like to add your name to our database system")
'''
myDict = {"Julius":
            {"School": "UCC", "Age" : 25, "Hall": "Nkrumah Hall"},
          "Ben": {"School": "Legon", "Age": 23, "Hall": "CommonWealth Hall"},
          "Nathan": {"School": "KNUST", "Age": 24, "Hall": "Casford"},
          "Alima": {"School": "KNUST","Age": 21, "Hall": "Valco"}

          }
Name = input("Enter your name: ").strip()
#print(myDict[Name])

if Name not in myDict:
    print("sorry you are not part of our database")
    Response = input("Would like to join, Y/N: ")
    if Response == 'y' or 'Y':
        Age = int(input("Enter your age: "))
        School = input("Enter your school: ").strip()
        Hall = input("Enter your hall of residence: ").strip()
        myDict[Name] = {"School": School, "Age": Age, "Hall": Hall}
    else:
        print("It seems you don't want to be part of our database")
else:
    print("Welcome Mr. {} ".format(Name))
    Feedback = input("What would like to know about yourself: ")
print(myDict[Name][Feedback])
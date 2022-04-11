print("hi")
x = 5
#while x <= 8:
   # print(x, " ", x**2)
   # x = x + 1

for num in range(1, 100):#This is the syntax for the FOR loop
    if num % 2 != 0:
        print(num)

myList = [x for x in range(1, 10)]
print(myList)

# Using the for loop to add names to a list:
myList1 = []
for i in range(1, 4):
    Elements = int(input("Add elements to your list: "))
    myList1.append(Elements) # The append method takes one argument.
print("This is your list \n",
      myList1, "\n",
      "And it has {} members in the list.".format(len(myList1)))


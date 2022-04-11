list1 = ["banana", "apple", "orange"]
for i in list1:
    if i == "apple":
        break
    print(i)

    if i == "apple":
        continue
    print(i)
import platform
#print(dir(platform))
import datetime

x = datetime.datetime.now()# This gives the current time and date
print(x)
print(x.strftime("%X"))

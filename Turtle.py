'''
Name = input("I would like to know your name: ").strip()
Response = input(f"Hello Mr.{Name}, would you like to play my guessin game: ")


from opcode import hasjabs
import socket
Hostname = socket.gethostname()
ipadd = socket.gethostbyname(Hostname)

print(ipadd)
'''

import turtle

# Creating a window to get started with turtle

s = turtle.getscreen() # To get a screen for the turtle 
t = turtle.Turtle() # Creating a variable to store the turtle


'''
# Creating a rectangle
t.forward(120)
t.rt(90)
t.fd(60)
t.rt(90)
t.forward(120)
t.rt(90)
t.fd(60)

#turtle.bgpic("none")
t.begin_fill()
turtle.pencolor("blue")
t.circle(60)
t.end_fill()

for i in range(4):
    t.fd(100)
    t.rt(90)

x = 1
while x<= 4:  
    t.fd(300)
    t.rt(90)
    x = x+1
   

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)#It is the fastest speed of the turtle
'''
x=1
while x<6:
    for i in range (6):
        for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:
            turtle.color(colors)
            turtle.circle(100)
            turtle.left(10)
    x=x+1



 
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)





 # To stop the screen to display
turtle.mainloop()

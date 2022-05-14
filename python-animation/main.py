#Importing turtle module
import turtle

#changing the background
turtle.bgcolor("black")

#setting the pen size
turtle.pensize(2.5)

#setting the speed
turtle.speed(0.5)

#List of colors for the animation
color = ["red", "green", "yellow", "blue"]

#reapeat the turtle animation using a for loop

for x in range(9):
    for i in color:
        turtle.color(i)
        #drawing a circle
        turtle.circle(150)
        #giving direction
        turtle.left(10)

turtle.mainloop()
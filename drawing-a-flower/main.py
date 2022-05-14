import turtle

turtle.bgcolor("black")
turtle.speed(0)

colors = ["red", "orange", "green", "blue"]

for x in range(170):
    for i in colors:
        turtle.color(i)
        turtle.circle(190-x, 90)
        turtle.left(90)
        turtle.circle(190-x, 90)
        turtle.left(30)

turtle.mainloop()
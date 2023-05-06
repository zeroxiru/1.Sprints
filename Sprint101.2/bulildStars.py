import turtle

def star(color, sides, length, angle, distance):
    galileo = turtle.Turtle()
    galileo.color(color) # colorful
    galileo.width(3)   # width of the star
    galileo.penup()     # make the line invisible
    galileo.left(angle)  # away from the center
    galileo.speed(50)
    galileo.forward(distance)
    galileo.pendown()  # start drawing

    for side in range(sides):
        galileo.forward(length)
        galileo.left(720/sides)
        galileo.hideturtle()


for angle in [180, 135, 90, 45, 0]:
    star("red", 5, 50, angle, 100)

for angle in [180, 135, 90, 45, 0]:
    star("green", 5, 30, angle, 60)

for angle in [180, 135, 90, 45, 0]:
    star("yellow", 5, 10, angle, 30)
    #star("blue", 7, 50, 45, 100)

for angle in [180,  90, 0]:
    star("black", 5, 5, angle, 15)

for angle in [90]:
    star("orange", 5, 10, angle, 5)


import turtle as turtle_module
import random


colors = [(201, 164, 112), (239, 246, 241), (152, 75, 50),
          (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75),
          (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165),
          (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85),
          (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]

turtle_module.colormode(255)

spot = turtle_module.Turtle()
spot.speed("fastest")
spot.hideturtle()
spot.penup()
spot.left(180)
spot.forward(250)
spot.left(90)
spot.forward(200)
spot.left(90)


def draw_dots():
    for _ in range(9):
        spot.dot(20, random.choice(colors))
        spot.forward(50)
        spot.dot(20, random.choice(colors))


def turn_left():
    spot.left(90)
    spot.forward(50)
    spot.left(90)


def turn_right():
    spot.right(90)
    spot.forward(50)
    spot.right(90)


for lines in range(5):
    draw_dots()
    turn_left()
    draw_dots()
    turn_right()


screen = turtle_module.Screen()
screen.exitonclick()

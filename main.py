import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
# tim.color("royal blue")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(20):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)


# ------------------------------------------------------
# My Solution
# ------------------------------------------------------
# tim.color("royal blue")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(180 - 90)
#
# tim.color("red")
# for _ in range(3):
#     tim.forward(100)
#     tim.right(180 - 60)
#
# tim.color("orchid")
# for _ in range(5):
#     tim.forward(100)
#     tim.right(180 - 108)
#
# tim.color("yellow")
# for _ in range(6):
#     tim.forward(100)
#     tim.right(180 - 120)
#
# tim.color("light green")
# for _ in range(7):
#     tim.forward(100)
#     tim.right(180 - 128.57)
#
# tim.color("dark slate blue")
# for _ in range(8):
#     tim.forward(100)
#     tim.right(180 - 135)
#
# tim.color("maroon")
# for _ in range(9):
#     tim.forward(100)
#     tim.right(180 - 140)
#
# tim.color("coral")
# for _ in range(10):
#     tim.forward(100)
#     tim.right(180 - 144)

# ------------------------------------------------------
# Instructor Solution
# ------------------------------------------------------
colors = ["coral", "maroon", "dark slate blue", "light green", "yellow", "orchid", "red", "royal blue"]
tim.speed(2)

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)


for i in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(i)

screen = Screen()
screen.exitonclick()

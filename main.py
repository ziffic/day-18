import random
import turtle as t

tim = t.Turtle()
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
# My Solution - Angles Challenge
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
# Instructor Solution - Angles Challenge
# ------------------------------------------------------
# colors = ["coral", "maroon", "dark slate blue", "light green", "yellow", "orchid", "red", "royal blue"]
# tim.speed(2)


# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.right(angle)
#
#
# for i in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(i)


# ------------------------------------------------------
# My Solution - Random Walk Challenge
# ------------------------------------------------------
# colors = ["coral", "maroon", "dark slate blue", "light green", "yellow", "orchid", "red", "royal blue"]
# distance = 20
# rand_num = 0
#
# tim.pensize(10)
# for _ in range(100):
#     tim.color(random.choice(colors))
#     rand_num = random.randint(1, 3)
#     if rand_num == 1:
#         tim.forward(distance)
#     elif rand_num == 2:
#         tim.right(90)
#     elif rand_num == 3:
#         tim.left(90)
#     # else:
#     #     tim.backward(distance)

# ------------------------------------------------------
# Instructor Solution - Random Walk Challenge
# ------------------------------------------------------
# colors = ["coral", "maroon", "dark slate blue", "light green", "yellow", "orchid", "red", "royal blue"]
# directions = [0, 90, 180, 270]
#
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# ------------------------------------------------------
# My Solution - Random RGBs
# ------------------------------------------------------
# t.colormode(255)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
#
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.pencolor(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# ------------------------------------------------------
# My Solution - Spirograph
# ------------------------------------------------------
# t.colormode(255)
# tim.speed("fastest")
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
#
# for i in range(1, 73):
#     tim.pencolor(random_color())
#     tim.circle(100)
#     tim.right(5)


# ------------------------------------------------------
# Instructor Solution - Spirograph
# ------------------------------------------------------
t.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

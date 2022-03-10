# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from random import choice

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]

turtle.colormode(255)
tim = turtle.Turtle()
tim.hideturtle()
tim.speed(0)
tim.pu()
tim.goto(-250, -200)


# Let's draw a line of dots with 50 steps apart
def draw_dots(dots):
    for _ in range(dots):
        color = choice(color_list)
        tim.dot(20, color)
        tim.forward(50)


# Let's move the turtle up
def move_up(position, stair):
    tim.setpos(position)
    tim.setheading(90)
    tim.forward((stair + 1) * 50)
    tim.setheading(0)


# Let's draw a matrix of dots
def draw_matrix(lines, dots):
    starting_position = tim.pos()
    for line in range(lines):
        draw_dots(dots)
        move_up(starting_position, line)


draw_matrix(10, 10)
screen = turtle.Screen()
screen.exitonclick()

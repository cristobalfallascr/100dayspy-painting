from turtle import Turtle, Screen
from random import randint

mt = Turtle()
mt.penup()
screen = Screen()
screen.colormode(255)
color_list = [(136, 169, 200), (191, 162, 140), (64, 89, 135), (183, 153, 171), (119, 77, 99), (153, 75, 50),
              (55, 118, 94), (220, 228, 87), (113, 115, 181), (45, 52, 105), (37, 44, 59), (129, 194, 143),
              (177, 187, 212), (225, 134, 16), (176, 94, 112), (81, 49, 66), (58, 46, 57), (110, 39, 37),
              (108, 166, 73), (215, 179, 193), (40, 49, 45), (46, 38, 35), (221, 83, 45), (231, 176, 158), (23, 95, 80),
              (148, 206, 214)]
canvas_size_x = 500
canvas_size_y = 500
y_pos = -200
x_pos = -200
mt.setpos(x_pos, y_pos)
mt.speed('fastest')

for _ in range(0, 500, 50):

    for _ in range(0, 500, 50):
        random_color = randint(0, len(color_list) - 1)

        mt.dot(20, color_list[random_color])
        mt.forward(50)

    y_pos += 50
    mt.setpos(x_pos, y_pos)

# TODO 10x10 row sports
# TODO size 20 and space by 50
# TODO paint from left to right, bottom to

screen.exitonclick()

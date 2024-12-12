# CTI 110
# P2LAB2B - Turtles
# Reese
# 10/17


# using lists and loops to draw

import turtle
t = turtle.Turtle()
# remember pensize, pencolor
t.pensize(4)
t.pencolor("Purple")


# simple loop
for length in[100,100,100,100]:
    t.forward(length)
    t.right(90)

#this program will be a loop
# color uses the index of the list
colors = ["darkviolet", "blue", "green", "pink"]
count = 0
for length in [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]:
    color = colors[count % 4] # pick one from the list
    count = count + 1
    t.pencolor(color)
    t.forward(length)
    t.right(90)
# Diamond
t.left(45)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

from turtle import *

def draw_square(size):
    for x in range(4):
        t.forward(size)
        t.right(90)

def draw_circle(radius):
    t.circle(radius)

t = Turtle()
t.hideturtle()
t.pencolor("white")

s = Screen()
s.bgcolor("black")

for i in range(50):
    draw_square(100)
    draw_circle(50)
    t.right(10)

draw_square(100)
draw_circle(50)

s.exitonclick()

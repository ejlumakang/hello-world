
from turtle import *

t = Turtle()
s = Screen()

t.speed(1)

#Rectangle
t.right(90)
t.backward(200)
t.right(90)
t.backward(100)
t.right(90)
t.backward(200)
t.right(90)
t.backward(100)

#Diamond
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)
t.right(60)
t.forward(100)

#Star
t.backward(100)
t.right(36)
t.forward(100)
t.right(72)
t.forward(100)
t.left(144)
t.forward(100)
t.right(72)
t.forward(100)
t.left(144)
t.forward(100)
t.right(72)
t.forward(100)
t.left(144)
t.forward(100)
t.right(72)
t.forward(100)
t.left(144)
t.forward(100)

#Circle
t.circle(100)

#Triangle
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
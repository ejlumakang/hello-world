#TicTacToe

from turtle import *

t = Turtle()
s = Screen()

t.speed(5)
s.setup(800, 800)

# Drawing the board
def draw_board():
    t.pencolor("white")
    t.pensize(10)
    s.bgcolor("black")

    # Rows
    t.up()
    t.goto(-300, -100)
    t.down()
    t.forward(600)

    t.up()
    t.goto(-300, 100)
    t.down()
    t.forward(600)

    # Columns
    t.left(90)
    t.up()
    t.goto(-100, -300)
    t.down()
    t.forward(600)

    t.up()
    t.goto(100,-300)
    t.down()
    t.forward(600)

    # Important
    t.right(90)


def draw_O(x, y):
    t.color("white")
    t.up()

    # Start drawing the circle 75 units down from the y-coordinate
    t.goto(x, y - 75)
    t.down()

    # Draw a circle of 75 units to fit the space well
    t.circle(75)


def draw_X(x, y):
    t.color("white")
    t.up()

    # Sets us up at bottom left corner
    t.goto(x - 75, y - 75)
    t.down()

    # Brings us to top right corner
    t.goto(x + 75, y + 75)
    t.up()

    # Sets us up at top left corner
    t.goto(x - 75, y + 75)
    t.down()

    # Bring to bottom right corner
    t.goto(x + 75, y - 75)


board = ["", "", "",
         "", "", "",
         "", "", ""]
turn = "X"


draw_board()


s.mainloop()
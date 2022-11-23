import turtle


def draw_square(t, sz):
    t.color("hotpink")
    """Make turtle t draw a square of sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.penup()
    t.forward(-10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()


wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle()  # Create alex
alex.pensize(5)
size = 20
for i in range(5):
    draw_square(alex, size)  # Call the function to draw the square
    size = size+20
wn.mainloop()

import turtle


def draw_square(t, sz):
    t.color("blue")
    """Make turtle t draw a square of sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.right(18)



wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle()  # Create alex
alex.pensize(5)
size = 200
for i in range(20):
    draw_square(alex, size)  # Call the function to draw the square
wn.mainloop()

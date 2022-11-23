import turtle


def draw_square(t, sz):
    t.color("blue")
    """Make turtle t draw a square of sz."""
    for i in range(2):
        t.forward(sz)
        t.right(90)
    t.left(3)


wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle()  # Create alex
alex.pensize(5)
size = 10
for i in range(30):
    draw_square(alex, size)  # Call the function to draw the square
    size = size+20
wn.mainloop()

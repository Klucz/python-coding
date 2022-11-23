import turtle


def draw_square(t, sz):
    t.color("hotpink")
    """Make turtle t draw a square of sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.penup()
    t.forward(2*sz)
    t.pendown()


wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle()  # Create alex
alex.pensize(5)
for i in range (5):
    draw_square(alex, 50)  # Call the function to draw the square
wn.mainloop()
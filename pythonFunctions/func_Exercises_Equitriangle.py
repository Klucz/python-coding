import turtle


def draw_poly(t,n, sz):
    t.color("hotpink")
    """Make turtle t draw a square of sz."""
    angle=((n-2)*180)/n
    for i in range(n):
        t.forward(sz)
        t.right(180-angle)


def draw_equitriangle(t,sz):
    draw_poly(t,3,sz)


wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

tess = turtle.Turtle()  # Create alex
tess.pensize(5)

draw_equitriangle(tess,50)  # Call the function to draw the square

wn.mainloop()
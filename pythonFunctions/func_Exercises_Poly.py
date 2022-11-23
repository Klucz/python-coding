import turtle


def draw_poly(t,n, sz):
    t.color("hotpink")
    """Make turtle t draw a square of sz."""
    angle=((n-2)*180)/n
    for i in range(n):
        t.forward(sz)
        t.right(180-angle)



wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

tess = turtle.Turtle()  # Create alex
tess.pensize(5)

draw_poly(tess,8,50)  # Call the function to draw the square

wn.mainloop()
import turtle

def draw_star(t, sz):
    t.color("hotpink")
    """Make turtle t draw a star of sz."""
    for i in range(5):
        t.forward(sz)
        t.right(144)


wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle()  # Create alex
alex.pensize(3)
#alex.left(180)
size = 100
for i in range(5):
    draw_star(alex, size)  # Call the function to draw the star
    alex.penup()
    alex.forward(350)
    alex.right(144)
    alex.pendown()
wn.mainloop()

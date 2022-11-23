import turtle

turtle.setup(400, 500)  # Determine the window size
wn = turtle.Screen()  # Get a reference to the window
wn.title("Handling keypresses!")  # Change the window title
wn.bgcolor("lightgreen")  # Set the background color
tess = turtle.Turtle()  # Create our favorite turtle


# The next four functions are our "event handlers".
def h1():
    tess.forward(30)


def h2():
    tess.left(45)


def h3():
    tess.right(45)


def h4():
    wn.bye()  # Close down the turtle window


def red():
    tess.color("red")


def green():
    tess.color("green")


def blue():
    tess.color("blue")


def size_plus():                        #size memory?
    size = 10
    if size > 20:
        size = 20
    tess.pensize(size + 1)
    print("Size is: {0}".format(size))
    size += 1
    if size > 20:
        size = 20
    return size


def size_minus():
    # response=input("type in size...")
    # size=int(response)
    size = 5
    if size < 1:
        size = 1
    tess.pensize(size - 1)
    size += -1
    if size < 1:
        size = 1
    return size


def shape_circle():
    tess.shape("circle")


def stamp():
    tess.stamp()


# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(red, "r")
wn.onkey(green, "g")
wn.onkey(blue, "b")
wn.onkey(size_plus, "+")
wn.onkey(size_minus, "-")
wn.onkey(shape_circle, "c")
wn.onkey(stamp, "s")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()

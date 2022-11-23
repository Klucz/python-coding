def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()  # Added this line
    t.left(90)
    t.forward(height)
    if height<0:
        t.penup()
        t.forward(-20)
        t.write("  " + str(height))
        t.forward(20)
        t.pendown()
    else:
        t.write("  " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()  # Added this line
    t.penup()
    t.forward(10)
    t.pendown()


import turtle

wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()  # Create tess and set some attributes
# tess.color("blue", "red")
tess.pensize(3)

xs = [48, 117, -200, 240, 160, 260, 220]
for b in xs:
    if b >= 200:
        tess.color("blue", "red")
    elif 200 > b >= 100:
        tess.color("blue", "yellow")
    elif 100 > b >= 0:
        tess.color("blue", "green")
    draw_bar(tess, b)

# for a in xs:
#  draw_bar(tess, a)

wn.mainloop()

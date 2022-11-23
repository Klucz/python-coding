print(list(range(10, 0, -2)))  # if start < stop and step < 0 - list is empty

import turtle

tess = turtle.Turtle()
alex = tess
alex.color("hotpink")
#alex.forward(100)
turtle.Screen().mainloop()  # setting color of alex also changes color of tess, they're the same object, one turtle (same adress)

pir = [(100, 30), (100, 120), (100, 120), (100, -135), (100 * 1.41, -135), (100, -135), (100 * 1.41, -135), (100, 0)]

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")
tess.left(90)
for (dis, angle) in pir:
    tess.forward(dis)
    tess.left(angle)

wn.mainloop()

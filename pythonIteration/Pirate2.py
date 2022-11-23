pir = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

for (dis,angle) in pir:
   tess.forward(dis)       # Move tess along
   tess.left(angle)           #  ...  and turn her

wn.mainloop()
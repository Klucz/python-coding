for i in range(999):
    print("We like python turtles")

for i in ["January","February","March","April","May","August","Septemper","October","November","December"]:
    print("One of the months of the year is",i)

tess_direction = 3645 % 360
print("tess direction is", tess_direction, "left")

#import turtle
#wn = turtle.Screen()
#wn.bgcolor("lightgreen")
#tess = turtle.Turtle()
#tess.shape("turtle")
#tess.color("blue")

#for i in range(8):
#    tess.forward(80)
#    tess.left(45)

#wn.mainloop()

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total = 1
for a in xs:
    print(a)
    total=total*a

print("Total is:",total)

#import turtle
#wn = turtle.Screen()
#wn.bgcolor("lightgreen")
#tess = turtle.Turtle()
#tess.shape("turtle")
#tess.color("blue")

#angl_fin = 0
#pir = [160, -43, 270, -97, -43, 200, -940, 17, -86]
#for i in pir:
#    tess.forward(100)
#    tess.left(i)
#    angl_fin = angl_fin + i
#wn.mainloop()

#print("Final angle is:",angl_fin%360)

#import turtle
#wn = turtle.Screen()
#wn.bgcolor("lightgreen")
#alex = turtle.Turtle()
#alex.shape("turtle")
#alex.color("blue")
#alex.left(36)
#for i in range(5):
#    alex.forward(200)
#    alex.left(144)

#wn.mainloop()


import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")
print(type(alex))

alex.stamp()
for i in range(12):
    alex.penup()
    alex.forward(200)
    alex.pendown()
    alex.forward(20)
    alex.stamp()
    alex.penup()
    alex.forward(-220)
    alex.right(30)

wn.mainloop()
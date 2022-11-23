import turtle

wn = turtle.Screen()
response = input("Set background color")
bg = response
wn.bgcolor(bg)  # Set the window background color
wn.title("Hello, Tess!")  # Set the window title

tess = turtle.Turtle()
response = input("Set Tess color")
ts=response
tess.color(ts)  # Tell tess to change her color
response = input("Set Tess pen size")
ps= int(response)
tess.pensize(ps)  # Tell tess to set her pen width

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()
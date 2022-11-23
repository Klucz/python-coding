import turtle  # Tess becomes a traffic light.

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
alex = turtle.Turtle()
alex2 = turtle.Turtle()
alex3 = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:  # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
        wn.ontimer(advance_state_machine, 2000)
    elif state_num == 1:  # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
        wn.ontimer(advance_state_machine, 2000)
    else:  # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
        wn.ontimer(advance_state_machine, 2000)


# Bind the event handler to the space key.


wn.ontimer(advance_state_machine, 2000)


def draw_housing2():
    """ Draw a nice housing to hold the traffic lights """
    alex.penup()
    alex.forward(160)
    alex.pendown()
    alex.pensize(3)
    alex.color("black", "darkgrey")
    alex.begin_fill()
    alex.forward(80)
    alex.left(90)
    alex.forward(200)
    alex.circle(40, 180)
    alex.forward(200)
    alex.left(90)
    alex.end_fill()


draw_housing2()

alex.penup()
# Position alex onto the place where the green light should be
alex.forward(40)
alex.left(90)
alex.forward(50)
# Turn alex into a big green circle
alex.shape("circle")
alex.shapesize(3)
alex.fillcolor("green")

alex2.penup()
# Position alex onto the place where the green light should be
alex2.forward(200)
alex2.left(90)
alex2.forward(120)
# Turn alex into a big green circle
alex2.shape("circle")
alex2.shapesize(3)
alex2.fillcolor("orange")

alex3.penup()
# Position alex onto the place where the green light should be
alex3.forward(200)
alex3.left(90)
alex3.forward(190)
# Turn alex into a big green circle
alex3.shape("circle")
alex3.shapesize(3)
alex3.fillcolor("red")

# This variable holds the current state of the machine
state2_num = 0


def advance_state_machine2():
    global state2_num
    if state2_num == 0:  # Transition from state 0 to state 1, orange
        alex.fillcolor("darkgreen")
        alex2.fillcolor("orange")
        alex3.fillcolor("darkred")
        state2_num = 1
        wn.ontimer(advance_state_machine2, 1000)
    elif state2_num == 1:  # Transition from state 1 to state 2, red
        alex.fillcolor("darkgreen")
        alex2.fillcolor("darkorange")
        alex3.fillcolor("red")
        state2_num = 2
        wn.ontimer(advance_state_machine2, 2000)
    elif state2_num == 2:  # Transition from state 2 to state 3, green
        alex.fillcolor("green")
        alex2.fillcolor("darkorange")
        alex3.fillcolor("darkred")
        state2_num = 3
        wn.ontimer(advance_state_machine2, 3000)
    else:
        # Transition from state 3 to state 4, green+orange
        alex.fillcolor("green")
        alex2.fillcolor("orange")
        alex3.fillcolor("darkred")
        state2_num = 0
        wn.ontimer(advance_state_machine2, 1000)


wn.ontimer(advance_state_machine2, 2000)

wn.listen()  # Listen for events
wn.mainloop()

import turtle

bob = turtle.Turtle()

turtle.forward(100) #moves it forward

turtle.backward(200) #backward

turtle.right(180) #turns the angle, direction, doesn't move.

turtle.left(50) #turns the angle, direction, doesn't move.

for i in range(4):
    bob.fd(100)
    bob.lt(90)




#encapsulation

def square(t):
    for i in range(4):
        t.forward(100)
        t.left(90)

square(bob)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(bob, 100)

turtle.mainloop()

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them. t is a turtle.
    """
    for i in range(n):
    t.fd(length)
    t.lt(angle)


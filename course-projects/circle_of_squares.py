import turtle
window = turtle.Screen()
brad = turtle.Turtle()
brad.shape("turtle")
brad.color("orange")
brad.speed(0)
degree = 0
while degree < 360:
    for i in range( 0, 4, 1):
        brad.forward(100)
        brad.right(90)
    brad.right(10)
    degree += 10
else :
    brad.right(90)
    brad.forward(150)
window.exitonclick()

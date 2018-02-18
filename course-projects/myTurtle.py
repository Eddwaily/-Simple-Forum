import turtle
def draw_Square( side_length ):
    window.bgcolor("dark blue")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("orange")
    brad.pensize(5)
    brad.speed(3)
    for i in range( 0, 4, 1):
        brad.forward(side_length)
        brad.right(90)

def draw_circle( radius ):#takes radius of circle as argument
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("green")
    angie.speed(4)
    angie.pensize(4)
    angie.circle(radius)

def draw_equi_triangle( side ):# a function that drows Equilateral triangle, same sides, same angles
    dan = turtle.Turtle()
    dan.shape("square")
    dan.color("dark red")
    dan.speed(5)
    dan.pensize(4)# this function determines the thickness of the pen for drawings
    for i in range ( 0, 3, 1):
        dan.right(120)
        dan.forward(side)

my_window = turtle.Screen()
draw_Square(100)
draw_circle(100)
draw_equi_triangle(111)
my_window.exitonclick()

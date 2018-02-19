from math import sin, cos, exp
import turtle
from random import randint

def draw_Square():
    color_list = [ "red", "green", "pink", "red", "yellow", "black", "orange", "white"]
    window = turtle.Screen()  #the list above we gonna go through it using randint to change color randomly
    window.bgcolor("dark blue")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(0) #speed is zero which mean the maximum speed
    brad.color("dark blue")

    t = 0
    while t <= 500 :
        x = 16 * pow( sin(t), 3 ) #equation to get x-coordinate to shape heart
        y = 13 * cos(t) - 5 * cos(2*t) - 2 * cos (3*t) - cos(4*t) #equation to get y-coordinate to shape heart
        '''x = 2.5 * pow(sin(-5*t), 2) * pow( 2, cos( cos(2.48 * 2.3 * t))) that's another equation , don't care about this comment
        y = 2.5 * sin(sin(-5*t) * pow (cos(4.28*2.3*t), 2))'''
        brad.goto(x*10, y*10) #using goto to go to x,y coordinates,mutiplying x,y by 10 to get a bigger shape
        brad.color( color_list[ randint( 0, 7) ] ) #changing the color in every time inside the loop
        t += 1
    window.exitonclick()

draw_Square()

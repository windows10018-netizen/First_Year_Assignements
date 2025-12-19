

from p5 import *

x = 75
y = 75
circle_x = 200
circle_y = 200
diameter = 150

def setup():
    size(500, 500)
    textFont(create_font("arial.ttf", 20))
    fill(0)
    stroke(255)
    textSize(48)

def draw():
    background(0)
    global circle_x, circle_y, diameter, x, y
    fill(0)
    ellipse(circle_x, circle_y, diameter, diameter)
    fill(255)
    ellipse(x, y, 5, 5)
    
    if (inside_circle(x, y, circle_x, circle_y, diameter/2)):
        text("Inside!", 10, 60)
    else:
        text("Outside!", 10, 60)

def inside_circle(x, y, circle_x, circle_y, radius):
    # this is the function you need to implement.  No need to touch anything else
    d = dist((x, y),(circle_x, circle_y))
    if d <= radius:
        return True
    else:
        return False

def mouse_clicked():
    global x, y
    x = mouse_x
    y = mouse_y
    
run()

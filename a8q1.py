

from p5 import*
# Initialize toy variables
toy_size = 20
stack = ['cube',]

def setup():
    size(400,400)
    rect_mode(CENTER)
    
def draw_cube(x, y):
    fill(255,0,0)
    square(x, y,toy_size)
    
def draw_ball(x, y):
    fill(0,255,0)
    circle(x, y, toy_size)

def draw():
    background(100)
    bottom_y = 390
    center_x = 200
    
    for index, toy in enumerate(stack):
        # Stack items vertically with spacing
        y = bottom_y - index * toy_size
        if toy == 'cube':
            draw_cube(center_x, y)
        else:
            draw_ball(center_x, y)

def key_pressed():
    global stack
    if key == 'c':
        stack.append('cube')
    if key == 'b':
        stack.append('balls')
    if key == 'r':
        stack.pop()
    if key == ' ':
        stack.clear()
        
run()
        
        


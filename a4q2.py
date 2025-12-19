

from p5 import*

r=255
g=255
b=255
x1=50
x2=50
left_eye_x = 285   # pupil x-coordinate for left eye
right_eye_x = 315  # pupil x-coordinate for right eye
antenna_color = Color(255, 255, 0)  # start as yellow
min_x_position = 45
max_x_position = 55

def setup():
    size(500,500)
    textFont(create_font("arial.ttf"))
    textSize(20)
def bot_head(x1, x2):
    """Draw's the robot's head"""
    # head
    fill(200,0,200)
    stroke(0)
    rect(250, 180, 150, 100)
    
    # Eyes
    stroke_weight(4)
    fill(0,255,255)
    circle(220, 175, 33)  # left eyeball
    circle(280, 175, 33)  # right eyeball
    
    # Pupils
    noStroke()
    fill(255,0,0)
    circle((x1+170, 230-55), 9)  # left pupil
    circle((x2+230, 230-55), 9)  # right pupil
    
def bot_antenna(r, g, b):
    """Draw's the robot_antenna """
    fill(200)
    rect(253, 121,8,30)  # antenna stick
    fill(antenna_color)
    circle(253, 100, 25)  # antenna light
    
def bot_body():
    """Draw's the robot's body."""
    fill(80,0,80)
    rect(253, 251,15,45)  
    fill(200,0,200)
    ellipse(253, 290,150, 70)
    fill(0)
    text("I Can See U!!!",195,277)
    
def bot_arms():
    """Draw the robot's arms."""
    fill(80,0,80)
    rect(134, 290, 90, 15)  # left arm
    rect(372, 290, 90, 15)  # right arm
    fill(250,100,100)
    circle(90,290,40)
    circle(410,290,40)
    
def full_bot(x1, x2, r, g, b):
    """Draw's the whole robot """
    bot_antenna(r, g, b)
    bot_head(x1, x2)
    bot_body()
    bot_arms()
    
def key_pressed():
    global left_eye_x, right_eye_x,antenna_color,x1,x2
    # Look left
    if key == "l":
        x1 = max(min_x_position, x2 - 10)  
        x2 = min(max_x_position, x1 - 10)
    # Look right 
    if key == "r":
        x2 = min(max_x_position, x1 + 10)  
        x1 = max(min_x_position, x2 + 10)
        
    if key == "p":
        antenna_color= Color(160, 32, 240)
    if key == "g":
        antenna_color= Color(0, 255, 0)
    if key == "y":
        antenna_color= Color(255, 255, 0)
    
    
    
def draw():
    background(0)
    rectMode(CENTER)
    full_bot(x1, x2, r, g, b)
    
run()
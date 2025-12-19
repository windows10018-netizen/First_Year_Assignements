

from p5 import*
num_burgers = 0

def setup():
    size(500,500)
    textFont(create_font("arial.ttf", 20))
    textAlign(CENTER, CENTER)
    rectMode(CENTER)
    
def ham_burger(x,y):  # draw the burger at position x, y
    fill(255,165,0)
    circle(x,y,30)
    fill(0,255,0)
    rect(x,y,36,2)
    fill(255,0,0)
    rect(x,y +2,30,3)
    fill(180,0,0)
    rect(x,y +6,35,6)
    fill(255,165,0)
    rect(x +1,y +12,34,6)
    
    
def draw():
    background(100)
    # burger grid
    burger_per_row = 10
    burger_weigth = 10
    burger_heigth = 10
    x_position = 50
    y_position = 50
    
     # Draw all burger
    for i in range(num_burgers):
       rows = i // burger_per_row
       col = i % burger_per_row
       x = x_position + col * burger_weigth
       y = y_position + rows * burger_heigth
       ham_burger(x, y)
       
    # Display count at bottom
    textSize(24)
    text(f" {num_burgers} Ham Burger", 250, 400)
    
    
def key_pressed():
    global num_burgers
    if key == "b":
        num_burgers = num_burgers +1
    if key == "v":
        num_burgers = max(0, num_burgers - 1)
    
    
run()
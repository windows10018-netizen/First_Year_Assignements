

from p5 import*
import random as Rand

monsters = []   # List to store all monster positions
radius = 20   # Radius of each monster circle
canvas_full = False
def setup():
    size(400,400)
    textFont(create_font("arial.ttf")) 
    textSize(30)
    
def can_place_monster(x, y):
    """
    Check if a monster can be placed at position (x, y) without overlapping existing monsters
    """
    for m in monsters:     # Checks the distance between new position and all existing monsters
        mx = m[0]
        my = m[1]
        
        distance =  ((x - mx)**2 + (y - my)**2)**0.5
        if distance < 2 * radius:
            return False
        
    return True
        
   
def draw():
    background(100)
    fill(255,0,0)
    for m in monsters:
        circle((m[0], m[1]), radius*2)
        
        
    if canvas_full:
        fill(255,255,0)
        text("CANVAS FULL", 180,200)
    
    
def mouse_pressed():
    global monsters, canvas_full
    x_position = Rand.randint(0, width)
    y_position = Rand.randint(0, height)
    
    attempt = 0     # Keep trying random positions until we find a valid one or exceed max attempt
    while not can_place_monster(x_position, y_position) and attempt < 1000:
        x_position = Rand.randint(0, width)
        y_position = Rand.randint(0, height)
        attempt += 1
        
    if attempt < 1000:
        monsters.append([x_position, y_position])
    else:
        canvas_full = True
    
    
    

run()



from p5 import*
import math as m
import random as R


''' HOW TO PLAY THE GAME: Find the right shapes before the time runs out '''


 # Global varibles
target_objects = []
game_won = False
start_time = 0
final_time_seconds = 0.0
time_limit_seconds = 30
game_over_time_out = False
clutter_shape = []
import os

''' loading file.txt '''
    
def load_object_from_file(filename):
    #print("Trying to open:", filename)
    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path, 'r')
    #print("File opened")
    for line in f:
        #print("Reading line:", line)
        line = line.strip()
        parts = line.split(',')
        if parts[0] == 'circle' or parts[0] == 'square' or parts[0] == 'triangle' or parts[0] =='ellipse':
            obj = {'shape': parts[0], 'x': int(parts[1]), 'y': int(parts[2]), 'size': int(parts[3]), 'r': int(parts[4]), 'g': int(parts[5]), 'b': int(parts[6]), 'found': False}
    
        target_objects.append(obj)
        #print("Added object:", obj)
    
    f.close()
    #print("Finished loading")

def setup():
    global clutter_shape
    size(600,600)
    textFont(create_font("arial.ttf"))
    load_object_from_file('objects1.txt')
    start_time = millis()
    #print(target_objects) 
    
    # random shapes in the background
    for i in range(70):
        clutter_obj = {
            'shape': R.choice(['circle', 'square', 'triangle', 'ellipse']),
            'x': R.randint(0, width),
            'y': R.randint(0, height),
            'size': R.randint(5, 70),
            'r': R.randint(0,255),
            'g': R.randint(0, 255),
            'b': R.randint(0, 255),
            }
        clutter_shape.append(clutter_obj)
        
    
def draw():
    global game_won, final_time_seconds, start_time, game_over_time_out, clutter_shape
    
    background(0) # Clear the screen each frame
    no_stroke() # Reset stroke at the start of draw for general drawing
    
     #Draw background clutter
    for clutter_obj in clutter_shape:
        fill(clutter_obj['r'], clutter_obj['g'], clutter_obj['b'])
        no_stroke()
        
        # draws all the the clutter random shapes
        if clutter_obj['shape'] == 'circle':
            circle(clutter_obj['x'], clutter_obj['y'], clutter_obj['size'])
        elif clutter_obj['shape'] == 'square':
            rect(clutter_obj['x'], clutter_obj['y'], clutter_obj['size'], clutter_obj['size'])
        elif clutter_obj['shape'] == 'ellipse':
            ellipse(clutter_obj['x'], clutter_obj['y'], clutter_obj['size'], clutter_obj['size']* 0.7)
        elif clutter_obj['shape'] == 'triangle':
            size = clutter_obj['size']
            x = clutter_obj['x']
            y = clutter_obj['y']
            triangle(x, y - size/2, x - size/2, y + size/2, x + size/2, y +size/2)
    
    ''' a game active state '''
    if game_won == False: 
        #  Live Timer Display 
        current_elapsed_milliseconds = millis() - start_time
        current_elapsed_seconds = round(current_elapsed_milliseconds / 1000, 2)
        
        # Check for time_out to transition to game_over
        time_remaining = time_limit_seconds - current_elapsed_seconds
        if time_remaining <= 0:
            time_remaining = 0.0 
            game_over_time_out = True 
            game_won = True
        
        fill(255) 
        textSize(28) 
        text("TIME LEFT: " + str(round(time_remaining, 2)), 10, 30) # Display time remaining
        
        # Draws the main shapes that is to be found
        for obj in target_objects:
            fill(obj['r'], obj['g'], obj['b'])
            
            if obj['found'] == True:
                stroke(255, 255, 255) # White outline for found shapes
                stroke_weight(4)
            else:
                no_stroke()
                
            # Draw the shapes itself
            if obj['shape'] == 'circle':
                circle(obj['x'], obj['y'], obj['size'])
            elif obj['shape'] == 'square':
                rect(obj['x'], obj['y'], obj['size'], obj['size'])
            elif obj['shape'] == 'ellipse':
                ellipse(obj['x'], obj['y'] + 50, obj['size'], obj['size'] - 20)
            elif obj['shape'] == 'triangle':
                size = obj['size']
                x = obj['x']
                y = obj['y']
                triangle(x, y - size/2, x - size/2, y + size/2, x + size/2, y + size/2)
                
        # Checking wining conditions 
        if game_over_time_out == False: 
            all_shapes_found = True
            for obj in target_objects:
                if obj['found'] == False:
                    all_shapes_found = False
                    break 
                
            if all_shapes_found == True: 
                final_time_seconds = round((millis() - start_time) / 1000, 2) 
                game_won = True 
            
    
    else: 
        
        
        
        # Redraws all shapes with outlines 
        # This ensures all found shapes remain visible with their outlines in the win/loss screen
        for obj in target_objects:
            fill(obj['r'], obj['g'], obj['b'])
            stroke(255, 255, 255) 
            stroke_weight(4)
            
            # Draw the shape itself
            if obj['shape'] == 'circle':
                circle(obj['x'], obj['y'], obj['size'])
            elif obj['shape'] == 'square':
                rect(obj['x'], obj['y'], obj['size'], obj['size'])
            elif obj['shape'] == 'ellipse':
                ellipse(obj['x'], obj['y'] + 50, obj['size'], obj['size'] - 20)
            elif obj['shape'] == 'triangle':
                size = obj['size']
                x = obj['x']
                y = obj['y']
                triangle(x, y - size/2, x - size/2, y + size/2, x + size/2, y + size/2)
                
           # display game over Message
        if game_over_time_out == True:
            stroke(0)
            fill(255,0,0) # Red for "TIME'S UP!"
            textSize(36)
            text("TIME'S UP!", 150, 200)
            textSize(28)
            text("GAME OVER!", 150, 250)
            no_stroke() 
        else: 
            stroke(0)
            fill(255, 255, 255) 
            textSize(28) 
            text("FINAL TIME: " + str(final_time_seconds), 10, 30)
            
            # "YOU WON!!!" message display 
            stroke(0)
            fill(255, 255, 0) 
            textSize(48) 
            text("YOU WON!!!", 100, 250) 
            no_stroke() 

               
def mouse_pressed():
    global target_objects, game_won, game_over_time_out
    
     # Check if the game is already over
    if game_won == True or game_over_time_out == True:
        return
   # print("Mouse clicked at:", mouse_x, mouse_y)
    
    for obj in target_objects:
        if obj['found'] == False:
            
            if obj['shape'] == 'circle':
                circle_x = obj['x']
                circle_y = obj['y']
                radius = obj['size']/2
                
                # Calculate the straight-line distance from the mouse click to the circle's center
                distance = m.sqrt((mouse_x - circle_x)**2 + (mouse_y - circle_y)**2)
                if distance < radius:
                    obj['found'] = True
                    #print("found a circle")
                    break
                
            elif obj['shape'] == 'square':
                square_x = obj['x']
                square_y = obj['y']
                square_size = obj['size']
                
                #Check if the mouse click's x and y coordinates are within the square's boundaries
                if (square_x <= mouse_x <= square_x + square_size) and (square_y <= mouse_y <= square_y + square_size):
                    obj['found'] = True
                    #print('found a square')
                    break
                
            elif obj['shape'] == 'ellipse':
                ellipse_x = obj['x']
                ellipse_y = obj['y']+50
                radius = obj['size']/2
                
                # Calculate distance from mouse click to ellipse center
                distance = m.sqrt((mouse_x - ellipse_x)**2 + (mouse_y - ellipse_y)**2)
                if distance < radius:
                    obj['found'] = True
                    #print('found an ellipse')
                    break
                
            elif obj['shape'] == 'triangle':
                triangle_x = obj['x']
                triangle_y = obj['y']
                triangle_size = obj['size']
                
                # Check if the mouse click is within the rectangular "bounding box" around the triangle
                if (triangle_x - triangle_size/2 <= mouse_x <= triangle_x + triangle_size/2) and (triangle_y - triangle_size/2 <= mouse_y <= triangle_y + triangle_size/2):
                    obj['found'] = True
                    #print('found triangle')
                    break
                
                
                

    
run()




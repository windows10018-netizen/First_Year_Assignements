


from p5 import*
import math as m
import random as R

target_objects = []
game_won = False
start_time = 0
final_time_seconds = 0.0
time_limit_seconds = 10
game_over_time_out = False

def load_object_from_file(filename):
    print("Trying to open:", filename)
    f = open(filename, 'r')
    print("File opened")
    for line in f:
        print("Reading line:", line)
        line = line.strip()
        parts = line.split(',')
        if parts[0] == 'circle' or parts[0] == 'square' or parts[0] == 'triangle' or parts[0] =='ellipse':
            obj = {'shape': parts[0], 'x': int(parts[1]), 'y': int(parts[2]), 'size': int(parts[3]), 'r': int(parts[4]), 'g': int(parts[5]), 'b': int(parts[6]), 'found': False}
    
        target_objects.append(obj)
        print("Added object:", obj)
    
    f.close()
    print("Finished loading")

def setup():
    size(500,500)
    textFont(create_font("arial.ttf"))
    load_object_from_file('objects1.txt')
    start_time = millis()
print(target_objects) 

def draw():
    global game_won, final_time_seconds, start_time, game_over_time_out # Declare all globals needed in draw()
    
    background(100) # Clear the screen each frame
    no_stroke() # Reset stroke at the start of draw for general drawing
    
    # --- 1. GAME ACTIVE STATE (game_won == False) ---
    if game_won == False: 
        # --- Live Timer Display ---
        current_elapsed_milliseconds = millis() - start_time
        current_elapsed_seconds = round(current_elapsed_milliseconds / 1000, 2)
        
        # Check for time out here to transition to game over
        time_remaining = time_limit_seconds - current_elapsed_seconds
        if time_remaining <= 0:
            time_remaining = 0.0 # Don't show negative time
            game_over_time_out = True # Set game over flag
            game_won = True # Transition to the 'game won' state (which handles both win/loss display)
        
        fill(255, 0, 0) # Red text for live timer
        textSize(28) # Set text size for timer
        text("TIME LEFT: " + str(round(time_remaining, 2)), 10, 30) # Display time remaining
        
        # --- Draw all shapes (active game, some may be found) ---
        for obj in target_objects:
            fill(obj['r'], obj['g'], obj['b'])
            
            if obj['found'] == True:
                stroke(255, 255, 255) # White outline for found shapes
                stroke_weight(4)
            else:
                no_stroke() # No outline for unfound shapes
                
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
                
        # --- Check Win Condition (ONLY if game is NOT won yet, and time has not run out) ---
        if game_over_time_out == False: # Only check for win if time hasn't already run out
            all_shapes_found = True
            for obj in target_objects:
                if obj['found'] == False:
                    all_shapes_found = False
                    break # Found one unfound, so no need to check others
                
            if all_shapes_found == True: # If all shapes ARE found NOW (first frame of win)
                final_time_seconds = round((millis() - start_time) / 1000, 2) # Capture final time
                game_won = True # Set game_won to True (this is the first frame of winning)
            
    # --- 2. GAME WON STATE (game_won == True) ---
    else: # game_won == True: Game IS WON or LOST by time out (display final screen)
        # --- Display Game Over Message (TIME'S UP! / GAME OVER!) ---
        
        
        # --- Redraw all shapes with outlines (win/loss screen) ---
        # This ensures all found shapes remain visible with their outlines in the win/loss screen
        for obj in target_objects:
            fill(obj['r'], obj['g'], obj['b'])
            stroke(255, 255, 255) # White outline for all shapes (they are all found or game is over)
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
            
        if game_over_time_out == True:
            stroke(0)
            fill(255,0,0) # Red for "TIME'S UP!"
            textSize(36)
            text("TIME'S UP!", 150, 200)
            textSize(28)
            text("GAME OVER!", 150, 250)
            no_stroke() # Ensure no stroke on this text
        else: # Game was won by finding all shapes (before time ran out)
            # --- Final Time Display ---
            stroke(0)
            fill(255, 255, 255) # White text for final time
            textSize(28) # Set text size for final time
            text("FINAL TIME: " + str(final_time_seconds), 10, 30)
            
            # --- "YOU WON!!!" Message Display ---
            stroke(0)
            fill(255, 255, 0) # Yellow for "YOU WON!!!"
            textSize(48) # Larger text size for "YOU WON!!!"
            text("YOU WON!!!", 100, 250) # Position for "YOU WON!!!"
            no_stroke() # Ensure no stroke on the text

               
def mouse_pressed():
    global target_objects, game_won, game_over_time_out
    if game_won == True or game_over_time_out == True:
        return
    print("Mouse clicked at:", mouse_x, mouse_y)
    
    for obj in target_objects:
        if obj['found'] == False:
            
            if obj['shape'] == 'circle':
                circle_x = obj['x']
                circle_y = obj['y']
                radius = obj['size']/2
                distance = m.sqrt((mouse_x - circle_x)**2 + (mouse_y - circle_y)**2)
                if distance < radius:
                    obj['found'] = True
                    print("found a circle")
                    break
                
            elif obj['shape'] == 'square':
                square_x = obj['x']
                square_y = obj['y']
                square_size = obj['size']
                if (square_x <= mouse_x <= square_x + square_size) and (square_y <= mouse_y <= square_y + square_size):
                    obj['found'] = True
                    print('found a square')
                    break
                
            elif obj['shape'] == 'ellipse':
                ellipse_x = obj['x']
                ellipse_y = obj['y']+50
                radius = obj['size']/2
                distance = m.sqrt((mouse_x - ellipse_x)**2 + (mouse_y - ellipse_y)**2)
                if distance < radius:
                    obj['found'] = True
                    print('found an ellipse')
                    break
                
            elif obj['shape'] == 'triangle':
                triangle_x = obj['x']
                triangle_y = obj['y']
                triangle_size = obj['size']
                if (triangle_x - triangle_size/2 <= mouse_x <= triangle_x + triangle_size/2) and (triangle_y - triangle_size/2 <= mouse_y <= triangle_y + triangle_size/2):
                    obj['found'] = True
                    print('found triangle')
                    break
                
                
                

    
run()




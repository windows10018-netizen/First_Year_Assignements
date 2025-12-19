

from p5 import*
import random as rand
name = "M  A  R  K"

def setup():
    size(500,500)
    textFont(create_font("arial.ttf", 20))
    textAlign(CENTER, CENTER)

def random_color(prev_color):
    colors = ("R", "G", "B", "Y", "M", "C")
    new_color = rand.choice(colors)
    while new_color == prev_color:
        new_color = rand.choice(colors)
    return new_color
   
def draw():
    global name
     # colorful background
    background(0)
    # colorful border frame
    noFill()
    strokeWeight(30)
    stroke(rand.randint(0,200), rand.randint(0,200), rand.randint(0,200))
    rect(0, 0, width, height)
    # Display's happy birthday text
    strokeWeight(1)
    fill(255)
    textSize(30)
    textAlign(CENTER, CENTER)
    text("HAPPY BIRTHDAY", 250, 200)
    textSize(50)
    old_color = ""
    total_name_width = 0
    
    for letter in name:
        total_name_width += textWidth(letter)
    x_position = (width/2) - (total_name_width/2)
    # draw each letter with random color
    for letter in name:
        color_letter = random_color(old_color)
        if color_letter == "R":
            fill(255,0,0) #Red
        elif color_letter == "G":
            fill(0,255,0 ) #Green
        elif color_letter == "B":
            fill(0,0,255) #Blue
        elif color_letter == "Y":
             fill(255,255,0)
        elif color_letter == "M":
            fill(255,0,255)
        elif color_letter == "C":
            fill(0,255,255)
        text(letter, x_position, 250)
        x_position += textWidth(letter)
            
        old_color = color_letter


run(frame_rate =5)
    
    

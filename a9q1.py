

from p5 import*
import random as R

my_size = 50
balloons = []

def setup():
    size(400,400)
    textFont(create_font("arial.ttf"))
    textSize(20)
    
def draw():
    background(180)
    
    for index, balloon in enumerate(balloons):
        pos = balloon['position']
        sz = balloon['size']
        col = balloon['color']
        x = pos[0]
        y = pos[1]
        fill(col[0], col[1], col[2])
        circle(x,y, sz)
        
        letter = chr(ord('a') + index)
        fill(0)
        text(letter,x,y)
        
def mouse_pressed():
    if len(balloons) >= 26:
        return 
    
    random_color = (R.randint(0,255),R.randint(0,255),R.randint(0,255))
    new_balloon = {'position':(mouse_x,mouse_y),'color':random_color, 'size':my_size}
    balloons.append(new_balloon)
    
def key_pressed(event):
    k = str(event.key).lower()
    if k == ' ':
        if len(balloons) > 0:
            balloons.pop()
        return
    
    if k.isalpha():
        index = ord(k) - ord('a')

        if 0 <= index < len(balloons):
            balloons[index]['size'] += 10
run()





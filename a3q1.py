

from p5 import*

background_colour=255
cookie_monster_fur_red=0
cookie_monster_fur_green=0
cookie_monster_fur_blue=255
def setup():
    size(500,500)
def draw():
    # Face
    background(background_colour)
    fill(cookie_monster_fur_green,cookie_monster_fur_red,cookie_monster_fur_blue)
    circle(width/2, height/2, 250)
    
    # Mouth
    fill(0)
    ellipse(250,300,200,110)
    
    # Eyes
    fill(255)
    circle(100+90,100+60,80)
    fill(255)
    circle(300,100+60,80)
    
    # Pupil
    fill(0)
    circle(100+85,100+45,40)
    fill(0)
    circle(300-15,100+70,40)
    
def key_pressed():
    global cookie_monster_fur_red
    global cookie_monster_fur_blue
    global cookie_monster_fur_green
    if key =="g":
        cookie_monster_fur_red=cookie_monster_fur_red+50
        cookie_monster_fur_green=0
        cookie_monster_fur_blue=0
    if key =="r":
        cookie_monster_fur_red=0
        cookie_monster_fur_green=cookie_monster_fur_green+50 
        cookie_monster_fur_blue=0
def mouse_clicked():
    global cookie_monster_fur_red
    global cookie_monster_fur_blue
    global cookie_monster_fur_green
    cookie_monster_fur_blue=255
    cookie_monster_fur_red=0
    cookie_monster_fur_green=0
run()
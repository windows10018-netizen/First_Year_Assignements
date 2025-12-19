

from p5 import*

def setup():
    size(500,500)
    textFont(create_font("arial.ttf"))
    textSize(20)
def land_scape(x,y):
    #green_grass
    fill(0,mouse_x+30,0)
    rect(0,450-90,510,90)
    #montain
    fill(mouse_x+30,0,0)
    triangle(100-30, 360, 200-30, 160, 300-30, 360)
    #the sun
    fill(mouse_x+30,mouse_x+30,0)
    circle(400,100,60)
    
def brightness_box(x,y):
    fill(255)
    rect(0,250+200,510,50)
    fill(0)
    text("< --Brightness-- >",170,470)
    #blacke circle 
    fill(0)
    circle(70,480,20)
    #yellow circle
    fill(255,255,0)
    circle(380,480,20)
   
def draw():
    background(0,0,mouse_x+30)
    land_scape(300,300)
    brightness_box(100,100)
run()
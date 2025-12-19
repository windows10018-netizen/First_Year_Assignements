
from p5 import*

robot_size = 50  
robot_x = 200    
robot_y = 200
background_colour=200
def setup():
    size(500,500)
    
def super_robot(x, y, size, cap, rap):
    #head
    fill(15,250,100)
    rect(x+200,y+100,60,60)
    #eyes():
    fill(255,0,0)
    circle(x+215,y+120,15)
    circle(x+245,y+120,15)
    #mouth
    fill(125,125,0)
    rect(x+150+60,y+100+40,10,10)
    rect(x+150+70,y+100+40,10,10)
    rect(x+150+80,y+100+40,10,10)
    rect(x+150+90,y+100+40,10,10)
    #Hands
    fill(15,250,100)
    rect(x+63,y+175,100,30)
    rect(x+310,y+175,100,30)
    #legs
    fill(15,250,100)
    rect(x+183,y+300,40,100)
    rect(x+250,y+300,40,100)
    #Body
    fill(15,250,100)
    rect(x+160,y+160,150,140)
    
    
def draw():
    background(background_colour)
    super_robot(robot_x-200, robot_y-203, robot_size)
    
def mouse_clicked():
    global robot_x, robot_y
    robot_x = mouse_x
    robot_y = mouse_y
    
def key_pressed():
    global robot_size
    global robot_x
    global robot_y
    if key =="1":
        robot_size=robot_size+10
    if key =="2":
        robot_size=robot_size-10
        
run()
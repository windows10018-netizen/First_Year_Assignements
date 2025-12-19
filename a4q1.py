

from p5 import*
x=0
y=0
scale=0.4
def setup():
    size(500,500)
    
def draw_tree(x,y):
    """ draws a tree centered at coodinate x and y"""
    #A_tree
    fill(200,155,120)
    rect(x+250,y+250,15,80)
    fill(0,240,0)
    circle(x+257,y+250,95)

def draw_house(x,y):
    """ draws a house centered at coodinate x and y"""
    #roof
    fill(0,0,200)
    triangle(x+40, y+180, x+100, y+180, x+70, y+80)
    #struture_of_the_house
    fill(200,100,150)
    rect(x+42,y+180,58,58)
    #door
    fill(125,125,0)
    rect(x+65,y+188,15,45)
    #door_handle
    fill(0)
    circle(x+72,y+200,8)
    #left_window
    fill(255)
    rect(x+46,y+185,9,9)
    rect(x+55,y+185,9,9)
    rect(x+46,y+193,9,9)
    rect(x+55,y+193,9,9)
    #right_window
    fill(255)
    rect(x+88,y+185,9,9)
    rect(x+80,y+185,9,9)
    rect(x+88,y+193,9,9)
    rect(x+80,y+193,9,9)


def forest_trees(x,y):
    """ draws multiple tree centered at random places on the canvas"""
   # draw_tree(x,y)
    draw_tree(x-325.8, y+184.4)
    draw_tree(x+142.7,y-58.9)
    draw_tree(x+273.6, y+128.4)
    draw_tree(x-188.5, y-234.1)
    draw_tree(x+217.4, y-163.2)
    draw_tree(x-255.1, y+47.2)
    draw_tree(x+89.5, y+272.1) 
    draw_tree(x-104.6, y-126.7)
    draw_tree(x+301.2,y-87.6)
    draw_tree(x+109.5, y+51.3)
    
def draw():
    background(0,100,0)
    #trees
    forest_trees(x,y)
    #the_house
    draw_house(mouse_x,mouse_y)
    # lake
    fill(0,255,255)
    ellipse(x+300,y+400,120,70)
    
#run()
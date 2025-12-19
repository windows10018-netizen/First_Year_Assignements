
from p5 import*
button_x = 100
button_y = 100
#button_size = 50
button_color_white = 255
button_color_black = 0
canvas_width = 281
canvas_height = 284
tileSize = 80
#tile=50
def setup():
    size(canvas_width, canvas_height)
    
def draw():
    x=button_x
    y=button_y
#Tiles
    fill(button_color_white)
    noStroke()
    rect(x -99, y -99, tileSize +20, tileSize +20)
    fill(button_color_black)
    noStroke()
    rect(x -29, y -99 , tileSize +20, tileSize +20)
    fill(button_color_white)
    noStroke()
    rect(x +40,y -99, tileSize +20, tileSize +20)
    fill(button_color_black)
    noStroke()
    rect(x+111, y -99, tileSize +20, tileSize +20)
#y-axis:
    fill(button_color_black)
    noStroke()
    rect(x -100,y -28, tileSize +20, tileSize +20)
    fill(button_color_white)
    noStroke()
    rect(x -99,y +42, tileSize +20, tileSize +20)
    fill(button_color_black)
    noStroke()
    rect(x -100,y +113, tileSize +20, tileSize +20)
#x-axis:2
    fill(button_color_white)
    noStroke()
    rect(x -29, y -28, tileSize +20, tileSize +20)
    fill(button_color_black)
    noStroke()
    rect(x +42, y -28, tileSize +20, tileSize +20)
    fill(button_color_white)
    noStroke()
    rect(x +110, y -28, tileSize +20, tileSize +20)
#x-axis:3
    fill(button_color_black)
    noStroke()
    rect(x -29, y +43, tileSize +20, tileSize +20)
    fill(button_color_white)
    noStroke()
    rect(x +40, y +43, tileSize +20, tileSize +20)
    fill(button_color_black)
    noStroke()
    rect(x +111, y +42, tileSize +20, tileSize +20)
#x-axis:4
    fill(button_color_white)
    noStroke()
    rect(x -29, y +112, tileSize +20, tileSize +20)
    fill(button_color_black)
    noStroke()
    rect(x +42, y +113, tileSize +20, tileSize +20)
    fill(button_color_white)
    noStroke()
    rect(x +111, y +113, tileSize +20, tileSize +20)
    
run()
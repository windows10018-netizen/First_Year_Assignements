

from p5 import*
x = 200
y = 200
#colour
white = 255
black = 0
gray=125

def setup():
    size(500,500)
    
def draw():
    fill(255, 0, 0)
    rect(100 +65, 100+10, x -20, y-120)
    
    fill(0, 0, 255)
    rect(x -25 , y -85, 60, 60)
    rect(x +75 , y -85, 60, 60)
    
    fill(gray)
    rect(100-1, x+50, x-150, y-210)
    
    fill(255, 0, 0)
    rect(100 +10, 100+80, x +100, y -120)
    
    fill(0, 0, 255)
    rect(x +14 , y -15, 60 +10, 60 +9)
    
    fill(0, 100, 255)
    ellipse(x-76, y, 30, 20)
    
    #fill(255)
    #ellipse(x-76, y, 30, 12)
    
    fill(400, 400, 50)
    ellipse(x+195, y, 30, 20)
    
    #fill(255)
    #ellipse(x+195, y, 30, 12)
    
    fill(black)
    circle(270, x, 10)
    
    fill(black)
    circle(190, x+50, 70)
    
    fill(white)
    circle(190, x+50, 30)
    
    fill(black)
    circle(310, x+50, 70)
    
    fill(white)
    circle(310, x+50, 30)
    

run()
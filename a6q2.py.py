

from p5 import*

# The weight of the balls 
ball1_weight =40
ball2_weight =60
ball3_weight =100

# The colour of the balls
ball1_colour = 100
ball2_colour = 200
ball3_colour = 150

# The position of the balls
ball1_x = 350
ball1_y = 250
ball2_x = 300
ball2_y = 200
ball3_x = 150
ball3_y = 250

#The size of the balls 
ball1_size = 40 #40kg
ball2_size = 60 #60kg
ball3_size = 100 #100kg

scale_center_x = 200
scale_center_y = 150
#scale_weight = 300

# weight on each side
left_weight = 0
right_weight = 0

midline_x = 300
midline_y = 300


def setup():
    size(700,500)
    textFont(create_font("arial.ttf"))
    textSize(20)
    
def draw():
    background(100)
    stroke_weight(10)
# Draw's the scale
    line(scale_center_x +100, scale_center_y, scale_center_x +100, scale_center_y +200)  # vertical line
    line(scale_center_x - 160, scale_center_y +150, scale_center_x +400, scale_center_y +150)  # horizontal line
# Draw balls
    stroke_weight(1)
    fill(ball1_colour,0,150)
    circle(ball1_x, ball1_y, ball1_size)
    fill(ball2_colour,40,90)
    circle(ball2_x, ball2_y, ball2_size)
    fill(ball3_colour,150,190)
    circle(ball3_x, ball3_y, ball3_size)
#left and right weight
    global left_weight, right_weight, midline_x, midline_y 
    left_weight = 0
    right_weight = 0
#scale’s vertical pole
    midline_x = scale_center_x + 100  
    #midline_y = scale_center_y + 100

    # ball 1
    if ball1_y > 250 and ball1_y < 350:
        """ Checks wether the balls are on the scale"""
        if ball1_x < 300:  # Left side
            left_weight += ball1_size
        elif ball1_x > 300:  # Right side
            right_weight += ball1_size
    
    # ball 2
    if ball2_y > 250 and ball2_y < 350:
        if ball2_x < 300:
            left_weight += ball2_size
        elif ball2_x > 300:
            right_weight += ball2_size
    
    # ball 3
    if ball3_y > 250 and ball3_y < 350:
        if ball3_x < 300:
            left_weight += ball3_size
        elif ball3_x > 300:
            right_weight += ball3_size

# Display's the weights
    fill(0)
    text(f"Left: {left_weight} kg", 50, 50)
    text(f"Right: {right_weight} kg", 400, 50)
#show's balance message
    if left_weight == right_weight:  
        text("Balanced", 250, 100)
    
def key_pressed():
    global ball1_x, ball1_y, ball2_x, ball2_y, ball3_x, ball3_y
    if key == '1':
        ball1_x = mouse_x
        ball1_y = mouse_y
    if key == '2':
        ball2_x = mouse_x
        ball2_y = mouse_y
    if key == '3':
        ball3_x = mouse_x
        ball3_y = mouse_y
        

    
    
run()
    
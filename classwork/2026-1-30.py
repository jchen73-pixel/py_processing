def setup(): #runs once
    size(400, 400)
    print("width =", width, "\nheight =", height) #system variables
 
def draw(): #runs like in a Netlogo forever loop
    background(220) #make the background grey
    #fill(0) #make the letters black so I can see them
    text(str(mouse_x) + ", " + str(mouse_y), 20, 20)
    stroke_weight(1)
    square(0,0,50)
    square(350,0,50)
    square(0,350,50)
    square(350,350,50)
    square(200,200,50)
    square(200,200,-50)
    square(150,200,50)
    square(200,150,50)
    circle(25,25,50)
    circle(375,25,50)
    circle(25,375,50)
    circle(375,375,50)
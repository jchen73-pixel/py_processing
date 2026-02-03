def setup(): #runs once
    size(400, 400)
 
def draw(): #runs like in forever loop in Netlogo
    #background(220) #make the background grey
    #fill(255)
    #circle(120,120,200)
    #fill(220)
    #no_stroke()
    #rect(10,100,220,150)
    #stroke(0)
    #line(20,100,220,100)
    background(220)
    grid()
    displayCoordinates()
    fill(255)
    rect(145, 185, 110, 70)
    rect(120, 80, 160, 80)
    rect()

def grid():
    stroke(255)
    for x in range(width):
        if x % 20 == 0:
            for y in range(height):
                if y % 20 == 0:
                    line(x, 0, x, height)
                    line(0, y, width, y)
    stroke(0)
    
def displayCoordinates():
    fill(0)
    text(str(mouse_x) + ", " + str(mouse_y), 20, 20)
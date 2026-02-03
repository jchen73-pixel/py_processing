def setup(): #runs once
    size(400, 400)
 
def draw():
    background(255)
    grid()
    displayCoordinates()
    
    # Robot drawing
    stroke(0)
    stroke_weight(3)
    no_fill()
    
    # Antenna
    circle(200, 60, 15)
    line(200, 67, 200, 90)

    stroke(0)
    ellipse(200, 110, 60, 40)
    no_stroke()
    fill(255)
    rect(160, 110, 80, 25)
    stroke(0)
    line(170, 110, 230, 110)
    no_fill()
    
    # Head
    rect(120, 110, 160, 100)
    
    # Eyes
    stroke_weight(4)
    circle(160, 150, 40)
    circle(240, 150, 40)
    circle(160, 150, 15)
    circle(240, 150, 15)
    stroke_weight(3)
    
    # Neck
    line(180, 210, 180, 230)
    line(220, 210, 220, 230)
    
    # Body
    rect(140, 230, 120, 100)
    
    # Arms
    line(140, 240, 100, 290)
    line(260, 240, 300, 290)
    
    # Chest Plate
    rect(160, 245, 80, 30)
    circle(200, 290, 15)
    
    # Legs
    line(170, 330, 160, 350)
    line(230, 330, 240, 350)
    
    # Feet
    stroke(0)
    no_fill()
    circle(160, 370, 40)
    circle(240, 370, 40)
    no_stroke()
    fill(255)
    rect(130, 370, 60, 30)
    rect(210, 370, 60, 30)
    stroke(0)
    line(140, 370, 180, 370)
    line(220, 370, 260, 370)

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
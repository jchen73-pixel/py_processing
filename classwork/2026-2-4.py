def setup(): #runs once
    size(400, 400)

def draw():
    background(225)
    grid()
    displayCoordinates()
    #taijitu()
    moai()
    
def taijitu():
    stroke_weight(2)
    fill(0)
    arc(200, 200, 200, 200, HALF_PI, PI+HALF_PI, CHORD)
    fill(255)
    arc(200, 200, 200, 200, HALF_PI+PI, PI+PI+HALF_PI, CHORD)
    no_stroke()
    fill(0)
    circle(200, 150, 100)
    fill(255)
    circle(200, 150, 20)
    circle(200, 250, 100)
    fill(0)
    circle(200, 250, 20)
    stroke_weight(1)
    stroke(255)
    
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

def moai():
    no_stroke()
    fill(100)
    rect(140, 160, 120, 140)
    arc(200, 160, 120, 120, PI, TWO_PI)

    # Head
    stroke(0)
    stroke_weight(4)
    no_fill()
    arc(200, 160, 120, 120, PI, TWO_PI) # Top
    line(140, 160, 140, 300) # Left
    line(260, 160, 260, 300) # Right
    line(140, 300, 260, 300) # Bottom
    
    # Eyes
    no_stroke()
    fill(80) 
    rect(140, 150, 120, 30)
    
    # Nose
    fill(100)
    stroke(0)
    begin_shape()
    vertex(180, 150)
    vertex(220, 150)
    vertex(230, 240)
    vertex(170, 240)
    end_shape()
    line(170, 240, 180, 150)
    
    # Mouth
    stroke_weight(3)
    line(180, 270, 220, 270)
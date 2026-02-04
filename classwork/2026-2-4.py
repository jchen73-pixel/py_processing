def setup(): #runs once
    size(400, 400)

def draw():
    background(225)
    grid()
    displayCoordinates()
    taijitu()
    
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
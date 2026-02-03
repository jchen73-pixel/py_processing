def setup(): #runs once
    size(400, 400)

def draw():
    background(225)
    grid()
    displayCoordinates()
    mystery = color(105, 215, 78)
    fill(mystery)
    stroke(0)
    #arc(200, 200, 100, 100, radians(45), radians(45 + 90), PIE)
    arc(200, 200, 100, 100, radians(90 + 45), radians(45 + 360), PIE)
    triangle(50,25,125,50,75,75)
    quad(275,50,350,75,300,125,250,75)
    begin_shape()
    vertex(175,100)
    vertex(225,125)
    vertex(225,175)
    vertex(175,200)
    vertex(125,175)
    vertex(175,150)
    vertex(150,125)
    end_shape(CLOSE) # connects the last vertex to the first

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
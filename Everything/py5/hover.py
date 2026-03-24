def setup():
    size(400,600)
def draw():
    background(220)
    #text(str(mouseX) + ", " + str(mouseY), 20, 20)
    #When you hover over the top left circle, it should turn light blue.
    draw_circles()
    mouse_hover()

def mouse_hover():
    if collidePointCircle(mouse_x, mouse_y,100,200,75):
        fill(175,215,255)
        circle(100, 200, 75)
    elif collidePointCircle(mouse_x, mouse_y,200,200,75):
        fill(130,0,130)
        circle(100, 300, 75)
        circle(300, 300, 75)
    elif collidePointCircle(mouse_x, mouse_y,300,200,75):
        fill(0)
        circle(300,200,75)
        circle(200,300,75)
    elif collidePointCircle(mouse_x, mouse_y,100,300,75):
        fill(255,0,0)
        for x in [100,200,300]:
            circle(x,200,75)
    elif collidePointCircle(mouse_x, mouse_y,200,300,75):
        fill(0,255,0)
        circle(100, 200, 75)
    elif collidePointCircle(mouse_x, mouse_y,300,300,75):
        fill(255, 120, 0)
        circle(100,300,75)
    fill(255)
    
def draw_circles():
    for x in [100,200,300]:
        for y in [200,300]:
            circle(x,y,75)                
    
def collidePointCircle(pointX, pointY, circX, circY, diameter):
  """Input coordinates for the point and x, y, and diameter (the width/height) of the circle.
  Returns true if the point and circle are touching.
  Does not work for ellipse/oval shapes."""
  
  distance = dist(pointX, pointY, circX, circY)
  radius = diameter/2
  
  if(distance <= radius):
    return True
  else:
    return False


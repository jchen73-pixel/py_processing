

def setup():
    size(400, 400)
    fill(200)
    
def draw():
    background(220)
    rect(150, 100, 100, 200)
    fill(255, 0, 0)
    circle(200, 140, 50)
    fill(255, 255, 0)
    circle(200, 200, 50)
    fill(0, 255, 0)
    circle(200, 260, 50)
    fill(200)
    
def mouse_pressed():
    if collidePointRect(mouse_x, mouse_y, 100, 100, 200, 100):
        fill(random(255), random(255), random(255))
        
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

def collidePointRect(pX, pY, rX, rY, rW, rH):
  """Input x,y coordinates of point and x, y, width, and height of rectangle.
  Returns true if the point and rectangle are touching."""

  if pX >= rX and pX <= rX + rW and pY >= rY and pY <= rY + rH:
    return True
  else:
    return False
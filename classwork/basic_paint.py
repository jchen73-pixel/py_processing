settings = {
    "stroke" = 0,
    "stroke_weight" = 0,
    "fill" = 0
    }

def setup():
    size(400, 400)
    background(220)
    
def draw():
    fill(0)
    square(20, 20, 20)
    fill(255, 0, 0)
    square(50, 20, 20)
    fill(0, 255, 0)
    square(80, 20, 20)
    fill(0, 0, 255)
    square(110, 20, 20)
    

def mouse_pressed():
    if (collidePointRect(mouse_x, mouse_y, 20, 20, 40, 20)):
        
    
def collidePointRect(pX, pY, rX, rY, rW, rH):
  """Input x,y coordinates of point and x, y, width, and height of rectangle.
  Returns true if the point and rectangle are touching."""

  if pX >= rX and pX <= rX + rW and pY >= rY and pY <= rY + rH:
    return True
  else:
    return False
hovers = {
    "tl": 0,
    "tlh": False,
    "tm": 0,
    "tr": 0,
    "bl": 0,
    "bm": 0,
    "br": 0
    }

def setup():
    size(400,600)
def draw():
    fill(255)
    background(220)
    #text(str(mouseX) + ", " + str(mouseY), 20, 20)
    circle(100, 200, 75) #top left
    circle(200, 200, 75) #top middle
    circle(300, 200, 75) #top right
    circle(100, 300, 75) #bottom left
    circle(200, 300, 75) #bottom middle
    circle(300, 300, 75) #bottom right
    if (collidePointCircle(mouse_x, mouse_y, 100, 200, 75)): #top left
        fill(173, 216, 230)
        circle(100, 200, 75)
        if (hovers["tlh"] == False):
            hovers["tl"] += 1
            hovers["tlh"] = True
    if (collidePointCircle(mouse_x, mouse_y, 200, 200, 75)): #top middle
        fill(128, 0, 128)
        circle(100, 300, 75)
        circle(300, 300, 75)
        hovers["tm"] += 1
    if (collidePointCircle(mouse_x, mouse_y, 300, 200, 75)): #top right
        fill(0)
        circle(200, 300, 75)
        hovers["tr"] += 1
    if (collidePointCircle(mouse_x, mouse_y, 100, 300, 75)): #bottom left
        fill(255, 0, 0)
        circle(100, 200, 75)
        circle(200, 200, 75)
        circle(300, 200, 75)
        hovers["bl"] += 1
    if (collidePointCircle(mouse_x, mouse_y, 200, 300, 75)): #bottom middle
        fill(0, 255, 0)
        circle(100, 200, 75)
        hovers["bm"] += 1
    if (collidePointCircle(mouse_x, mouse_y, 300, 300, 75)): #bottom right
        fill(255, 165, 0)
                 circle(100, 300, 75)
        hovers["br"] += 1
        
    if (not collidePointCircle(mouse_x, mouse_y, 100, 200, 75) and hovers["tlh"] == True):
        hovers["tlh"] = False
    fill(0)
    text("Top Left: " + str(hovers["tl"]), 20, 20)
    text("Top Middle: " + str(hovers["tm"]), 20, 30)
    text("Top Right: " + str(hovers["tr"]), 20, 40)
    text("Bottom Left: " + str(hovers["bl"]), 20, 50)
    text("Bottom Middle: " + str(hovers["bm"]), 20, 60)
    text("Bottom Right: " + str(hovers["br"]), 20, 70)
        
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
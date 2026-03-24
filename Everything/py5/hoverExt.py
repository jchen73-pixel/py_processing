count = {
        "tl": 0,
        "tm": 0,
        "tr": 0,
        "bl": 0,
        "bm": 0,
        "br": 0
        }
fill_color = color(220,255,220)
def setup():
    size(400,600)
def draw():
    background(255,220,220)
    #text(str(mouseX) + ", " + str(mouseY), 20, 20)
    #When you hover over the top left circle, it should turn light blue.
    draw_circles()
    mouse_hover()

def mouse_hover():
    global count
    if collidePointCircle(mouse_x, mouse_y,100,200,75):
        fill(175,215,255)
        circle(100, 200, 75)
        count["tl"] += 1
        if count["tl"] > 100:
            circle(100,200,25)
    elif collidePointCircle(mouse_x, mouse_y,200,200,75):
        fill(130,0,130)
        circle(100, 300, 75)
        circle(300, 300, 75)
        count["tm"] += 1
        if count["tm"] > 100:
            circle(100,300,100)
            circle(300,300,100)
    elif collidePointCircle(mouse_x, mouse_y,300,200,75):
        fill(count["tr"])
        circle(300,200,75)
        circle(200,300,75)
        count["tr"] += 1
        if count["tr"] > 255:
            count["tr"] = 0
    elif collidePointCircle(mouse_x, mouse_y,100,300,75):
        fill(255,count["bl"],count["bl"])
        for x in [100,200,300]:
            circle(x,200,75)
        count["bl"] += 1
        if count["bl"] > 255:
            count["bl"] = 0
    elif collidePointCircle(mouse_x, mouse_y,200,300,75):
        fill(0,255,0)
        count["bm"] += 1
        circle(100, 200, count["bm"])
        if count["bm"] > 100:
            count["bm"] = 1
    elif collidePointCircle(mouse_x, mouse_y,300,300,75):
        fill(255, count["br"] , 0)
        circle(100,300,75)
        count["br"] += 1
        if count["br"] > 255:
            count["br"] = 0
    fill(fill_color)
    
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


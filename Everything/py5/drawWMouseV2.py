x = 20
colors = {
    "red":[x,color(255,0,0)],
    "green":[x,color(0,255,0)],
    "blue":[x,color(0,0,255)],
    "yellow":[x,color(255,255,0)],
    "orange":[x,color(250,120,0)],
    "pink":[x,color(255,200,200)],
    "fushia":[x,color(250,0,180)],
    "black":[x,color(0)],
    "white":[x,color(255)],
    "grey":[x,color(210)],
    "lightGreen":[x,color(220,255,220)],
    "random":[x,color(255)]
    }
stroke_color = color(0)
back_color=color(230)

def setup():
    size(400,400)
    start_setup()
    
def start_setup():
    global stroke_color
    stroke_color = 0
    background(back_color)
    stroke_weight(1)
    stroke(stroke_color)
    fill(0)
    #draw squares at the bottom
    text_size(15)
    text("Press your mouse to draw\nPress a number to change your stroke's width",10,28)
    text("Click any rectangle to choose your stroke's color",50,360)
    global colors
    i = 0
    for x in range(20,361,30):
        fill(list(colors.values())[i][1])
        if x >= 350:
            rect(x, 370, 43, 20)
            #print(x)
            fill(0)
            text_size(12)
            text("random",x+2,384)
        else:
            square(x, 370, 20)
        list(colors.values())[i][0] = x
        i += 1
    #eraser
    text_size(15)
    fill(255)
    rect(320,5,50,20)
    fill(0)
    text("eraser",325,20)
    #clear
    fill(255)
    circle(275,17,33)
    fill(0)
    text("clear",260,20)

def draw():
    #text(str(mouse_x) + ", " + str(mouse_y), 20, 20)
    stroke(stroke_color)
    #draw with lines
    if is_mouse_pressed and collidePointRect(mouse_x,mouse_y,0,69,width,255):
        line(mouse_x, mouse_y, pmouse_x, pmouse_y)
    if is_key_pressed:
        if key.isdigit():
            stroke_weight(int(key))
                    
def mouse_pressed():
    global stroke_color
    for x in range(20,350,30):
      if collidePointSquare(mouse_x,mouse_y,x,370,20):
          for i in range(len(colors)):
              if x == list(colors.values())[i][0]:
                  stroke_color = list(colors.values())[i][1]
                  break
    if collidePointRect(mouse_x,mouse_y,350,370,43,20):
        # Random fill
        stroke_color = color(random(255),random(255),random(255))
    if collidePointRect(mouse_x,mouse_y,320,5,50,20):
      # Use the background color to erase
      stroke_color = back_color
    if collidePointCircle(mouse_x,mouse_y,275,17,33):
      #clear the screen
      start_setup()
      
    
def collidePointSquare(px,py,sx,sy,sw):
    return collidePointRect(px,py,sx,sy,sw,sw)
    
def collidePointRect(pX, pY, rX, rY, rW, rH):
  """Input x,y coordinates of point and x, y, width, and height of rectangle.
  Returns true if the point and rectangle are touching."""

  if pX >= rX and pX <= rX + rW and pY >= rY and pY <= rY + rH:
    return True
  else:
    return False

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
        
        


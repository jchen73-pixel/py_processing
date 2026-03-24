#screen dimensions
sw = 600
sh = 600

#flag width
w = 480

#position
u = "up"
d = "down"

def setup():
    size(sw,sh)
    frame_rate(5)
    #rectmode(CENTER)
    
def star(x,y):
    fill("#FFFFFF")
    # two triangles for the star (white)
    triangle(x,y,x+10,y-25,x+20,y)
    triangle(x-2.5,y-15,x+22.5,y-15,x+10,y-2.5)
    #third triangle for the star = at the bottom (blue)
    fill("#000080")
    triangle(x+10,y-5,x,y,x+20,y)
    
def wavyRect(x,y,h,upDn):
    d = w/2 # waves distance
    begin_shape()
    vertex(x,y)
    if upDn == "up":
      bezier_vertex(x+d,y-50,x+d,y+50,x+w,y)
    else:
      bezier_vertex(x+d,y+50,x+d,y-50,x+w,y)
    vertex(x+w,y+h)
    if upDn == "up":
      bezier_vertex(x+w-d,y+h+50,x+w-d,y+h-50,x,y+h)
    else:
      bezier_vertex(x+w-d,y+h-50,x+w-d,y+h+50,x,y+h)
    vertex(x,y)
    end_shape(CLOSE)
    
def wavySq(x,y,w,h,upDn):
    d = w/2 # delat for wave location
    wH = 31 # wave height
    begin_shape()
    vertex(x,y)
    if upDn == "up":
      bezier_vertex(x,y,x+d,y-wH,x+w,y)
    else:
      bezier_vertex(x,y,x+d,y+wH,x+w,y)
    vertex(x+w,y+h)
    if upDn == "up":
      bezier_vertex(x+w,y+h,x+w-d,y+h-wH,x,y+h)
    else:
      bezier_vertex(x+w,y+h,x+w-d,y+h+wH,x,y+h)
    vertex(x,y)
    end_shape(CLOSE)
    
   
def waveStars(x,y,yE,yI,xE,xI,middle): 
    for j in range(0,yE,yI):
      d = 0
      for i in range(0,xE,xI):
        if (i < middle and u == "up") or (i > middle and u != "up"):
          d += 4
        elif i < middle and u != "up" or (i > middle and u == "up"):
          d -= 4
        star(x+i,y+j-d)
    
def flag():
    no_stroke()
    x = 20
    y = 50
    h = 300
    
    # Main rectangle (white)
    fill("#FFFFFF")
    wavyRect(x,y,h,u)
    
    # red sripes
    h = 20
    fill(255,0,0)
    wavyRect(x,y,h,u)
    wavyRect(x,y+h*2,h,u)
    wavyRect(x,y+h*4,h,u)
    wavyRect(x,y+h*6,h,u)
    wavyRect(x,y+h*8,h,u)
    wavyRect(x,y+h*10,h,u)
    wavyRect(x,y+h*12,h,u)
    wavyRect(x,y+h*14,h,u)
    
    # corner rectangle (blue)
    fill("#000080")
    wavySq(x,y,240,180,u)
    
    # starts (rows of 5)
    x = x + 8
    y = y + 30
    yE = 175
    yI = 35
    xE = 240
    xI = 40
    middle = xI * 3
    waveStars(x,y,yE,yI,xE,xI,middle)
        
    # stars (rows of 4)
    x = x + 20
    y = y + 17.5
    yE = 140
    yI = 35
    xE = 200
    waveStars(x,y,yE,yI,xE,xI,middle)
    
    # # grey elipses
    # x = 20
    # y = 50
    # h = 300
    # fill(150,150,150,50)
    # if u == "up":
    #   ellipse(x+25,y+h/2,50,h)
    #   ellipse(x+25*3+w/2,y+10+h/2,50,h)
    # else:
    #   ellipse(x+25+110,y+h/2+20,50,h)
    #   ellipse(x+25*3+140+w/2,y+10+h/2-15,50,h)
 
# not currently used   
def draw_gradient(x,y,w,h):
    #Color stops 
    top_color = color(200,200,200,50) # lighter grey#
    middle_color = color(150,150,150,50) # grey
    bottom_color = color(200,200,200,50) # lighter grey
    
    for x in range(w):
      #Blend colors vertically
      if x < w/2:
        #Blue to purple (top half)
        interp = map(x, 0, w/2, 0, 1)
        c = lerpColor(top_color, middle_color, interp)
      else:
        #Purple to black (bottom half)
        interp = map(x, w/2, w, 0, 1)
        c = lerpColor(middle_color, bottom_color, interp)
        
      #Draw horizontal line
      stroke(c)
      #line(x+20, y, x+20, h+45)
      # grey elipses
      x = 20
      y = 50
      h = 300
      #fill(150,150,150,50)
      if u == "up":
        ellipse(x+25,y+h/2,50,h)
        ellipse(x+25*3+w/2,y+10+h/2,50,h)
      else:
        ellipse(x+25+110,y+h/2+20,50,h)
        ellipse(x+25*3+140+w/2,y+10+h/2-15,50,h)
    
def draw():
    global u,d
    
    background(220)
    text_size(25)
    #text(str(mouseX) + ", " + str(mouseY), 20, 20)
    
    u,d = d,u
    #u = "Dn"
    flag()
    
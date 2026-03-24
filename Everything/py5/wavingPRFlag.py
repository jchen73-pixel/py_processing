#screen dimensions
sw = 600
sh = 400

#flag width
w = 300

#position
u = "up"
d = "down"

def setup():
    size(sw,sh)
    frame_rate(4)
    #rectmode(CENTER)
    
def wavyRect(x,y,h,upDn):
    begin_shape()
    vertex(x,y)
    if upDn == "up":
      bezier_vertex(x+100,y-50,x+200,y+50,x+w,y)
    else:
      bezier_vertex(x+100,y+50,x+200,y-50,x+w,y)
    vertex(x+w,y+h)
    if upDn == "up":
      bezier_vertex(x+w-100,y+h+50,x+w-200,y+h-50,x,y+h)
    else:
      bezier_vertex(x+w-100,y+h-50,x+w-200,y+h+50,x,y+h)
    vertex(x,y)
    end_shape(CLOSE)

# def wavyRect(x,y,h,upDn):
#     d = w/2
#     begin_shape()
#     vertex(x,y)
#     if upDn == "up":
#       bezier_vertex(x+d,y-50,x+d,y+50,x+w,y)
#     else:
#       bezier_vertex(x+d,y+50,x+d,y-d,x+w,y)
#     vertex(x+w,y+h)
#     if upDn == "up":
#       bezier_vertex(x+w-d,y+h+50,x+w-d,y+h-50,x,y+h)
#     else:
#       bezier_vertex(x+w-d,y+h-50,x+w-d,y+h+50,x,y+h)
#     vertex(x,y)
#     end_shape(CLOSE)
    
def banderaW():
    ######################## Flag #############################
    skyblue = color(153,204,255)
    #fill(0,0,0)
    #text("Bandera de Puerto Rico",65,30) # Puerto Rico's Flag (in Spanish)
    
    no_stroke()
    # Main rectangle (white)
    fill("#FFFFFF")
    x = y = 50
    
    wavyRect(x,y,200,u)
    
    # red sripes
    fill("#FF0000")
    h = 40
    wavyRect(x,y,h,u)
    wavyRect(x,y+80,h,u)
    wavyRect(x,y+160,h, u)
    
    # translate triangle and star 5 up
    if u == "up":
      translate(0,-5)
    
    # large triangle (blue)
    fill(skyblue)
    h = sh/2
    triangle(x,y,x+h/2,y+h/2,x,y+h)
    
    # two triangles for the star (white)
    fill("#FFFFFF")
    y = 170
    triangle(x+15,y,x+35,y-50,x+55,y)
    triangle(x+10,y-30,x+60,y-30,x+35,y-5)
    #third triangle for the star = at the bottom (blue)
    fill(skyblue)
    triangle(x+35,y-10,x+15,y,x+55,y)

def draw():
    global u,d
    
    background(220)
    text_size(25)
    #text(str(mouseX) + ", " + str(mouseY), 20, 20)
    
    u,d = d,u
    banderaW()
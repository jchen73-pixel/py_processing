import sys
sys.path.append("/home/support/ialonso/Documents")
from collide2D import *

w = h =150
x = 200

def setup():
    size(400,600)
    
def mouseOnLight(y,cOn,cOff):
    if collidePointCircle(mouse_x,mouse_y,x,y,w):
      fill(cOn)
    else:
      fill(cOff)
    ellipse(x, y, w, h)

def draw():
    background(220)
    textSize(25)
    
    #traffic light body
    fill("#999999")
    
    rect(100, 25, 200, 540)
   
    #red light
    mouseOnLight(140,"#FF0000","#AA0000")

    #yellow light
    mouseOnLight(300,"#FFFF00","#AAAA00")
    
    #green light
    mouseOnLight(460,"#00FF00","#00AA00")
    
    #text(str(mouseX) + ", " + str(mouseY), 20, 20)
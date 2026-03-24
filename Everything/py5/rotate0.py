from gridNdot import *

def setup():
  size(510,350)

def draw():
  background(220)
  
  #remap maps a number into another range
#   angle = remap(mouse_x, 0, width, 0, 360)
#   
#   push_matrix()
#   translate(width/2, height/2)
#   rotate(radians(angle))
#   rect(-40, -20, 80, 40)
#   pop_matrix()

  rect(200,100,100,159)
  rotate(radians(10))
  #draw_grid()
  rect(200,200,100,159)

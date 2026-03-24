def setup():
  size(510,350)

def draw():
  background(220)
  
  angle = remap(mouse_x, 0, width, 0, 360)
  
  push_matrix()
  translate(width/2, height/2)
  rotate(radians(angle))
  rect(-40, -20, 80, 40)
  pop_matrix()
angle = 15

def setup():
  size(510,350)

def draw():
  background(220)
  global angle
  sine_value = sin(radians(angle))
  y = remap(sine_value, -1, 1, 70, 230)	
  
  angle += 1
  
  circle(width/2, y, 50)
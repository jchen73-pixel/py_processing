angle = 15

def setup():
  size(510,350)
   
def draw():
  background(220)
  global angle
  sine_value = sin(radians(angle))
  
  print(sine_value)
  
  angle += 1
  
angle = 15
speed = 0.05
x = 0

def setup():
  size(510,350)
   
def draw():
  background(220)
  global angle, speed, x
  y1 = 60 + sin(angle) * 40
  y2 = 60 + sin(angle + 0.4) * 40
  y3 = 60 + sin(angle + 0.8) * 40
  circle(x + 80, y1, 40)
  circle(x + 120, y2, 40)
  circle(x + 160, y3, 40)
  angle += speed
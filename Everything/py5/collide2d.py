#Based on the WONDERFUL Collision Detection document made by Jeffrey Thompson:
#http://www.jeffreythompson.org/collision-detection/table_of_contents.php

#Kept as close to the p5.js version of Collide2D made by Ben Moren as possible:
#https://github.com/bmoren/p5.collide2D

def collidePointPoint(x1, y1, x2, y2):
  """Input coordinates for two points, returns true if points are touching"""
  
  if x1 == x2 and y1 == y2:
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
    
def collideCircleCircle(circ1x, circ1y, circ1d, circ2x, circ2y, circ2d):
  """Input x,y coordinates and diameter for both circles.
  Returns true if the two circles are touching.
  
  Does not work for ellipse/oval shapes."""
  
  distance = dist(circ1x, circ1y, circ2x, circ2y)
  circ1rad = circ1d/2
  circ2rad = circ2d/2
  
  if distance <= circ1rad + circ2rad:
    return True
  else:
    return False

def collidePointRect(pX, pY, rX, rY, rW, rH):
  """Input x,y coordinates of point and x, y, width, and height of rectangle.
  Returns true if the point and rectangle are touching."""

  if pX >= rX and pX <= rX + rW and pY >= rY and pY <= rY + rH:
    return True
  else:
    return False

def collideRectRect(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h):
  """Input x,y,w,h for rect1 and x,y,w,h for rect2.
  Returns true if the rectangle and rectangle are touching."""
  
  if r1x + r1w >= r2x and r1x <= r2x + r2w and r1y + r1h >= r2y and r1y <= r2y + r2h:
    return True
  else:
    return False

def collideCircRect(cX, cY, cD, rX, rY, rW, rH):
  """Input x, y, diameter of the circle and x, y, width, height of the rectangle.
  Returns true if the circle and rectangle are touching.
  
  Does not work for elliptical/oval shapes."""
  
  cR = cD/2
  
  testX = cX
  testY = cY
  
  if cX < rX:
    testX = rX
  elif cX > rX + rW:
    testX = rX + rW
  
  if cY < rY:
    testY = rY
  elif cY > rY + rH:
    testY = rY+rH
  
  distX = cX - testX
  distY = cY - testY
  distance = sqrt((distX*distX) + (distY*distY))
  
  if (distance <= cR):
    return True
  else:
    return False

def collideLinePoint(x1, y1, x2, y2, px, py, buffer=0.1):
  """Input the x1,y1,x2,y2 of the line and the x,y of the point.
  Returns true if the point and line are touching.
  
  Buffer is optional and set to 0.1 by default - higher #s are less accurate."""
  
  d1 = dist(px,py,x1,y1)
  d2 = dist(px,py,x2,y2)
  
  lineLen = dist(x1,y1,x2,y2)
  
  if d1 + d2 >= lineLen - buffer and d1 +d2 <= lineLen + buffer:
    return True
  else:
    return False

def collideLineCircle(x1, y1, x2, y2, cX, cY, cD):
  """Input the x1,y1,x2,y2 of the line and then the x,y,diameter of the circle.
  Returns true if they are touching.
  
  Does not work with elliptical/oval shapes."""
  
  r = cD/2
  
  inside1 = collidePointCircle(x1, y2, cX, cY, cD)
  inside2 = collidePointCircle(x2, y2, cX, cY, cD)
  
  if inside1 or inside2:
    return True
  
  lineLen = dist(x1,y1,x2,y2)
  
  dot = ( ((cX-x1)*(x2-x1)) + ((cY-y1)*(y2-y1)) ) / pow(len,2)
  
  closestX = x1 + (dot * (x2 - x1))
  closestY = y1 + (dot * (y2 - y1))
  
  onSegment = collideLinePoint(x1, y1, x2, y2, closestx, closestY)
  
  if not onSegment:
    return False
  
  distX = closestX - cX
  distY - closestY - cY
  distance = sqrt((distX*distX) + (distY*distY))
  
  if(distance <= r):
    return True
  else:
    return False

def collideLineLine(x1,y1,x2,y2,x3,y3,x4,y4):
  """Input x1,y1,x2,y2 of first line and x3,y3,x4,y4 of second line.
  Returns true if lines are touching."""
  
  uA=((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
  uB=((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
  
  if uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1:
    return True
  else:
    return False


def collideLineRect(x1,y1,x2,y2,rX,rY,rW,rH):
  """Input x1,y1,x2,y2 for the line and x,y,width,height for the rect.
  Returns true if they are touching."""
  
  left = collideLineLine(x1,y1,x2,y2,rX,rY,rX,rY+rH)
  right = collideLineLine(x1,y1,x2,y2, rX+rW, rY, rX+rW, rY+rH)
  top = collideLineLine(x1,y1,x2,y2, rX, rY, rX+rW, rY)
  bottom = collideLineLine(x1,y1,x2,y2, rX, rY + rH, rX+rW, rY+rH)
  
  if left or right or top or bottom:
    return True
  else:
    return False
  
def collidePointTriangle(px, py, x1, y1, x2, y2, x3, y3):
  areaOrig = abs( (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1))
  
  area1 = abs( (x1-px)*(y2-py) - (x2-px)*(y1-py) )
  area2 = abs( (x2-px)*(y3-py) - (x3-px)*(y2-py) )
  area3 = abs( (x3-px)*(y1-py) - (x1-px)*(y3-py) )
  
  if area1 + area2 + area3 == areaOrig:
    return True
  else:
    return False
defaultWid = 400
defaultLen = 400
defaultBack = 220

# color squares setting
sqStartRow = 20
sqStartCol = 20
sqRadius = 20
sqSpacing = 50

# User modifiable variables
user = {
  "stroke_weight" : 1,
  "fill" : 0,
  "mode": "free"
}

def setup():
  size(defaultWid, defaultLen)
  background(defaultBack)

def draw():
  fill(user["fill"])
  stroke(user["fill"])
  stroke_weight(user["stroke_weight"])

  if (is_key_pressed()):
    if (key in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]):
      user["stroke_weight"] = int(key)
    elif (key in ["f", "r", "c"]):
      user["mode"] = key

  # reset for permanent displays
  stroke_weight(1)

  # Auto creates rectangles for colors
  #          Black      Red        Orange     Yellow     Green      Blue       Purple     White
  colors = ["#000000", "#FF0000", "#FFA500", "#FFFF00", "#008000", "#0000FF", "#4B0082", "#FFFFFF"]
  for clr in colors:
      fill(clr)
      stroke(clr)
      square(sqStartRow + colors.index(clr) * sqSpacing, sqStartCol, sqRadius)

  if (is_mouse_pressed()):
      if (mouse_y <= sqStartRow and mouse_y >= sqStartRow + sqRadius):
          fill(255)
          stroke_weight(5)
          point(mouse_x, mouse_y)
      
  
def collidePointSquare(pX, pY, x, y, r):
  if pX >= x and pX <= x + r and pY >= y and pY <= y + r:
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
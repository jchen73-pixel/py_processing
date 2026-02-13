# Setup
defaultWid = 400
defaultLen = 400
defaultBack = 220
commandAreaHeight = 60

# Color Squares Settings
sqStartRow = 20
sqStartCol = 20
sqRadius = 20
colors = ["#000000", "#FF0000", "#FFA500", "#FFFF00", "#008000", "#0000FF", "#4B0082", "#FFFFFF"]
sqSpacing = defaultWid / len(colors)

# User Modifiable Variables
user = {
  "stroke_weight" : 1,
  "fill" : 0,
  "mode": "free"
}

def setup():
  size(defaultWid, defaultLen)
  background(defaultBack)

def draw():
  # Reset for user actions
  fill(user["fill"])
  stroke(user["fill"])
  stroke_weight(user["stroke_weight"])

  if (is_key_pressed()):
    # Change stroke weight
    if (key in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]):
      user["stroke_weight"] = int(key)
    # Change mode
    elif (key in ["f", "r", "c"]): # free, rectangle, circle
      user["mode"] = key

  if (is_mouse_pressed()):
    if pmouse_y < commandAreaHeight:
      for i in range(len(colors)):
          if collidePointSquare(mouse_x, mouse_y, sqStartCol + i * sqSpacing, sqStartRow, sqRadius):
              user["fill"] = colors[i]
              break
    if user["mode"] == "free":
      line(pmouse_x, pmouse_y, mouse_x, mouse_y)

  # Overlays commands
  no_stroke()
  fill(defaultBack)
  rect(0, 0, width, commandAreaHeight)
  
  # Border line
  stroke(0)
  stroke_weight(1)
  line(0, commandAreaHeight, width, commandAreaHeight)
  
  # Draw colors
  for i in range(len(colors)):
      fill(colors[i])
      stroke(0)
      square(sqStartCol + i * sqSpacing, sqStartRow, sqRadius)
      
  
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
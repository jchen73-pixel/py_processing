# Setup
defaultWid = 400
defaultLen = 400
defaultBack = 220
commandAreaHeight = 100

# Color Squares Settings
sqStartRow = 20
sqStartCol = 20
sqRadius = 20
colors = ["#000000", "#FF0000", "#FFA500", "#FFFF00", "#008000", "#0000FF", "#4B0082", "#FFFFFF"]
sqSpacing = defaultWid / len(colors)

# User Variables
shapes = []
user = {
  "stroke_weight" : 1,
  "fill" : 0,
  "mode": "f"
}

circ = {
  "x": 0,
  "y": 0,
  "radius": 0,
  "drawing": False
}

rectangle = {
    "x1": 0,
    "y1": 0,
    "x2": 0,
    "y2": 0,
    "drawing": False
}

def setup():
  size(defaultWid, defaultLen)
  background(defaultBack)

def draw():
  # clear screen/draw background
  background(defaultBack)
  
  # Redraw all saved shapes
  for shape_data in shapes:
      fill(shape_data["color"])
      stroke(shape_data["color"])
      stroke_weight(shape_data["weight"])
      if shape_data["type"] == "line":
          line(shape_data["x1"], shape_data["y1"], shape_data["x2"], shape_data["y2"])
        
      elif shape_data["type"] == "circle":
          ellipse(shape_data["x"], shape_data["y"], shape_data["w"], shape_data["h"])
      
      elif shape_data["type"] == "rect":
          w = shape_data["x2"] - shape_data["x1"]
          h = shape_data["y2"] - shape_data["y1"]
          rect(shape_data["x1"], shape_data["y1"], w, h)

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
    if user["mode"] == "f" and mouse_y > commandAreaHeight and pmouse_y > commandAreaHeight:
      new_line = {
        "type": "line",
        "x1": pmouse_x, "y1": pmouse_y,
        "x2": mouse_x, "y2": mouse_y,
        "color": user["fill"],
        "weight": user["stroke_weight"]
      }
      shapes.append(new_line)
      line(pmouse_x, pmouse_y, mouse_x, mouse_y)

  if (circ["drawing"] and not circ["x"] == -1):
      circle(circ["x"], circ["y"], dist(circ["x"], circ["y"], mouse_x, mouse_y) * 2)
      
  if (rectangle["drawing"] and not rectangle["x1"] == -1):
      rect(rectangle["x1"], rectangle["y1"], mouse_x - rectangle["x1"], mouse_y - rectangle["y1"])

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
  
  # Draw Buttons
  fill(0)
  text_size(12)
  text_align(CENTER, CENTER)
  
  # Clear Button
  fill(255)
  rect(20, 60, 60, 30)
  fill(0)
  text("Clear", 50, 75)
  
  # Free Button (f)
  if user["mode"] == "f":
      fill(200) # Highlight
  else:
      fill(255)
  rect(100, 60, 60, 30)
  fill(0)
  text("Free", 130, 75)
  
  # Circle Button (c)
  if user["mode"] == "c":
      fill(200)
  else:
      fill(255)
  rect(180, 60, 60, 30)
  fill(0)
  text("Circle", 210, 75)

  # Rectangle Button (r)
  if user["mode"] == "r":
      fill(200)
  else:
      fill(255)
  rect(260, 60, 60, 30)
  fill(0)
  text("Rect", 290, 75)

def mouse_pressed():
  # Handle UI clicks
  if mouse_y < commandAreaHeight:
      # Handle Color Selection
      if mouse_y >= sqStartRow and mouse_y <= sqStartRow + sqRadius:
          for i in range(len(colors)):
              if collidePointSquare(mouse_x, mouse_y, sqStartCol + i * sqSpacing, sqStartRow, sqRadius):
                  user["fill"] = colors[i]
                  break
      
      # Handle Button Clicks
      elif mouse_y >= 60 and mouse_y <= 90:
          if mouse_x >= 20 and mouse_x <= 80: # Clear
              shapes[:] = []
          elif mouse_x >= 100 and mouse_x <= 160: # Free
              user["mode"] = "f"
          elif mouse_x >= 180 and mouse_x <= 240: # Circle
              user["mode"] = "c"
          elif mouse_x >= 260 and mouse_x <= 320: # Rectangle
              user["mode"] = "r"
  else:
      if user["mode"] == "c":
          if not circ["drawing"]:
              circ["x"] = mouse_x
              circ["y"] = mouse_y
              circ["drawing"] = True
          else:
              circ["drawing"] = False
              r = dist(circ["x"], circ["y"], mouse_x, mouse_y)
              new_circle = {
                  "type": "circle",
                  "x": circ["x"], "y": circ["y"],
                  "w": r*2, "h": r*2,
                  "color": user["fill"],
                  "weight": user["stroke_weight"]
              }
              shapes.append(new_circle)
              circ["x"] = -1
      elif user["mode"] == "r":
          if not rectangle["drawing"]:
              rectangle["x1"] = mouse_x
              rectangle["y1"] = mouse_y
              rectangle["drawing"] = True
          else:
              rectangle["drawing"] = False
              new_rect = {
                  "type": "rect",
                  "x1": rectangle["x1"], "y1": rectangle["y1"],
                  "x2": mouse_x, "y2": mouse_y,
                  "color": user["fill"],
                  "weight": user["stroke_weight"]
              }
              shapes.append(new_rect)
              rectangle["x1"] = -1

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
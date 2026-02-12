settings = {
  "stroke_weight" : 1,
  "fill" : 0,
  "mode": "free"
}

def setup():
  size(400, 400)
  background(220)

def draw():
  fill(settings["fill"])
  stroke(settings["fill"])
  stroke_weight(settings["stroke_weight"])

  if (settings["mode"] == "free"):
    if (is_mouse_pressed()):
      line(mouse_x, mouse_y, pmouse_x, pmouse_y)
  elif (settings["mode"] == "rect"):
    if (is_mouse_pressed()):
      rect(mouse_x, mouse_y, 10, 10)
  elif (settings["mode"] == "circle"):
    if (is_mouse_pressed()):
      circle(mouse_x, mouse_y, 10)

  if (is_key_pressed()):
    # stroke weights
    if (key in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]):
      settings["stroke_weight"] = int(key)
    elif (key == "f"):
      settings["mode"] = "free"
    elif (key == "r"):
      settings["mode"] = "rect"
    elif (key == "c"):
      settings["mode"] = "circle"

def collidePointRect(pX, pY, rX, rY, rW, rH):
  """Input x,y coordinates of point and x, y, width, and height of rectangle.
  Returns true if the point and rectangle are touching."""

  if pX >= rX and pX <= rX + rW and pY >= rY and pY <= rY + rH:
    return True
  else:
    return False
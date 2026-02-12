settings = {
  "stroke" : 0,
  "stroke_weight" : 1,
  "fill" : 0,
  "mode": "free"
}

def setup():
  size(400, 400)
  background(220)

def draw():
  stroke(settings["stroke"])
  stroke_weight(settings["stroke_weight"])
  fill(settings["fill"])

  if (is_key_pressed()):
    # stroke weights
    if (key == "0"):
      settings["stroke_weight"] = 1
    elif (key == "1"):
      settings["stroke_weight"] = 2
    elif (key == "2"):
      settings["stroke_weight"] = 3
    elif (key == "3"):
      settings["stroke_weight"] = 4
    elif (key == "4"):
      settings["stroke_weight"] = 5
    elif (key == "5"):
      settings["stroke_weight"] = 6
    elif (key == "6"):
      settings["stroke_weight"] = 7
    elif (key == "7"):
      settings["stroke_weight"] = 8
    elif (key == "8"):
      settings["stroke_weight"] = 9
    elif (key == "9"):
      settings["stroke_weight"] = 10

def collidePointRect(pX, pY, rX, rY, rW, rH):
  """Input x,y coordinates of point and x, y, width, and height of rectangle.
  Returns true if the point and rectangle are touching."""

  if pX >= rX and pX <= rX + rW and pY >= rY and pY <= rY + rH:
    return True
  else:
    return False
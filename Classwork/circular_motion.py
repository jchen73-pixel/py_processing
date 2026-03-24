circ1 = {
  "x":0,
  "y":0,
  "angle":17.0,
  "offset":20, #scales it on diagonal from origin
  "scalar":20, #size of circle
  "speed":0.5
  
}

def setup():
  size(600,420)
  background(220) 

def draw():
  global circ1
  #background(220)
  
  circ1["x"] = circ1["offset"] + cos(circ1["angle"]) * circ1["scalar"]
  circ1["y"] = circ1["offset"] + sin(circ1["angle"]) * circ1["scalar"]
  
  circle(circ1["x"], circ1["y"], 40)
  circ1["angle"] += circ1["speed"]
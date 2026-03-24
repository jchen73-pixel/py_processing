circ1 = {
  "x":0,
  "y":0,
  "angle":0.0,
  "offset":200,
  "scalar":20,
  "speed":0.05
}

def setup():
  size(600,420)
  background(220) 

def draw():
  global circ1
  #background(220)
  
  circ1["x"] = circ1["offset"] + cos(circ1["angle"]) * circ1["scalar"]
  circ1["y"] = circ1["offset"] + sin(circ1["angle"]) * circ1["scalar"]
  
  frame_rate(100)
  circle(circ1["x"], circ1["y"], 40)
  circ1["angle"] += circ1["speed"]
  circ1["scalar"] += circ1["speed"]
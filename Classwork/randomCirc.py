circ1 = {
  "x":0,
  "y":0,
  "angle":17.0,
  "offset":20, #scales it on diagonal from origin
  "scalar":20, #size of circle
  "speed":0.5
  
}

circles = []

def setup():
  size(600,600)
  background(220)
  stroke(255)
  frame_rate(10)
  gen_circle()

def draw():
    global circles
    for circ in circles:
        if circ["radius"] <= 0:
            circles.remove(circ)
            continue
        stroke_weight(circ["stroke_weight"])
        stroke(circ["color"])
        circ["x"] = circ["offset"] + cos(circ["angle"]) * circ["scalar"]
        circ["y"] = circ["offset"] + sin(circ["angle"]) * circ["scalar"]
        circle(circ1["x"], circ["y"], circ["radius"])
        circ["angle"] += circ["speed"]
        if circ["aging"]:
            circ["radius"] -= 1
        else:
            circ["radius"] += 1
            if circ["radius"] >= circ["max_size"]:
                circ["aging"] = True

def gen_circle():
    global circles
    for i in range(1, 10, 1):
        circle.append( {
            "x": int(random(width)),
            "y": int(random(height)),
            "angle": 5.0,
            "offset": 20,
            "scalar": 20,
            "speed": 0.05,
            "color": color(int(random(255)), int(random(255)), int(random(255))),
            "stroke_weight": int(random(3)),
            "max_size": int(random(width/4)),
            "radius": 1,
            "aged": False
        })
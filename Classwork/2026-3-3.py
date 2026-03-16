diam = 20
rad = diam/2
rand = 4
def setup():
    size(500,360)
    global circ1
    global circ2
    global circ3
    global circ4
    circ1 = {
        "x": width + diam,
        "xSpd":3,
        "dir": -1
        }
    circ2 = {
        "y":diam,
        "ySpd": 2,
        "dir": 1
        }
    circ3 = {
        "x": diam,
        "y": diam,
        "xSpd":4,
        "xDir":1,
        "ySpd":1,
        "yDir":1
        }
    circ4 = {
        "x": width/2,
        "y": height/2,
        "xSpd": random(-rand, rand),
        "ySpd": random(-rand, rand)
        }


def draw():
    global circ1
    global circ2
    global circ3
    global circ4
    global diam
    background(220)
    
    circle(circ1["x"], 50, diam)
    circ1["x"] += circ1["xSpd"] * circ1["dir"]
    #if circ1["x"] < 0:
    #    circ1["x"] = width + diam
    if circ1["x"] < 0:
        circ1["dir"] = 1
    if circ1["x"] > width:
        circ1["dir"] = -1
    
    circle(50, circ2["y"], diam)
    circ2["y"] += circ2["ySpd"] * circ2["dir"]
    #if circ2["y"] > height:
    #    circ2["y"] = diam
    if circ2["y"] < 0:
        circ2["dir"] = 1
    if circ2["y"] > height:
        circ2["dir"] = -1
    
    circle(circ3["x"], circ3["y"], diam)
    circ3["x"] += circ3["xSpd"] * circ3["xDir"]
    if circ3["x"] < 0:
        circ3["xDir"] = 1
    if circ3["x"] > width:
        circ3["xDir"] = -1
    circ3["y"] += circ3["ySpd"] * circ3["yDir"]
    if circ3["y"] < 0:
        circ3["yDir"] = 1
    if circ3["y"] > height:
        circ3["yDir"] = -1
        
    choice = int(random(4))
    if choice == 0: circ4["x"] -= circ4["xSpd"]
    if choice == 1: circ4["x"] += circ4["xSpd"]
    if choice == 2: circ4["y"] -= circ4["ySpd"]
    if choice == 3: circ4["y"] += circ4["ySpd"]
    circle(circ4["x"], circ4["y"], diam)
circ1 = {
    "x": 0,
    "xSpeed": 2
    }
circ2 = {
    "y": 0,
    "ySpeed": 2
    }
circ3 = {
    "x": 0,
    "y": 0,
    "xSpeed": 2,
    "ySpeed": 2
    }
circ4 = {
    "x": 270,
    "y": 180
    }

def setup():
    size(520, 360)
    
def draw():
    background(220)
    circle(circ1["x"], 50, 20)
    circ1["x"] += circ1["xSpeed"]
    if circ1["x"] > width:
        circ1["x"] = 0
    
    circle(50, circ2["y"], 20)
    circ2["y"] += circ2["ySpeed"]
    if circ2["y"] > height:
        circ2["y"] = 0
    
    circle(circ3["x"], circ3["y"], 20)
    circ3["x"] += circ3["xSpeed"]
    circ3["y"] += circ3["ySpeed"]
    if circ3["x"] > width:
        circ3["x"] = 0
    if circ3["y"] > height:
        circ3["y"] = 0
        
    rand = int(random(4))
    if rand == 0: circ4["x"] -= 3
    if rand == 1: circ4["x"] += 3
    if rand == 2: circ4["y"] -= 3
    if rand == 3: circ4["y"] += 3
    circle(circ4["x"], circ4["y"], 20)
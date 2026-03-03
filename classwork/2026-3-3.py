diam = 20
rad = diam/2
def setup():
    size(500,360)
    global circ1
    global circ2
    global circ3
    circ1 = {
        "x": width + diam,
        "xSpd":3,
        }
    circ2 = {
        "y":diam,
        "ySpd": 2,
        }
    circ3 = {
        "x": diam,
        "y": diam,
        "xSpd":4,
        "ySpd":1,
        }


def draw():
    global circ1
    global circ2
    global circ3
    global diam
    background(220)
    circle(circ1["x"], 50, diam)
    circ1["x"] -= circ1["xSpd"]
    if circ1["x"] < 0:
        circ1["x"] = width + diam
    circle(50, circ2["y"], diam)
    circ2["y"] += circ2["ySpd"]
    if circ2["y"] > height:
        circ2["y"] = diam
    circle(circ3["x"], circ3["y"], diam)
    circ3["x"] += circ3["xSpd"]
    circ3["y"] += circ3["ySpd"]
    if circ3["x"] > width:
        circ3["x"] = diam
    if circ3["y"] > height:
        circ3["y"] = diam
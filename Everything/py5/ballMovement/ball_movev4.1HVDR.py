diam = 20		# diameter
rad = diam/2	# rad
rand = rad/2	# random movement

def setup():
    size(500,360)
    global circ1, circ2, circ3, circ4
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

    circ4 = {
        "x": width/2,
        "y": height/2,
        "xSpd": random(-rand,rand),
        "ySpd": random(-rand,rand),
        } 

def draw():
    global circ1, circ2, circ3, circ4
    background(220)
    #text(str(mouseX) + ", " + str(mouseY), 20, 20)
    
    circle(circ1["x"], 200, 20) #circ1 moves right to left
    circle(200, circ2["y"], 20) #circ2 moves from top to bottom
    circle(circ3["x"], circ3["y"], 20) #circ3 moves diagonally
    circle(circ4["x"], circ4["y"], 20) #circ 4 moves randomly
    
    circ1["x"] -= circ1["xSpd"] #moves circ1
    if circ1["x"] < 0:
        circ1["x"] = width + 20
    circ2["y"] += circ2["ySpd"] #moves circ2
    if circ2["y"] > height:
        circ2["y"] = 0
    
    circ3["x"] += circ3["xSpd"] #moves circ3 x axis
    circ3["y"] += circ3["ySpd"] #moves circ3 y axis
    if circ3["x"] > width or circ3["y"] > height:
        circ3["x"] = 20
        circ3["y"] = 20
        
    circ4["x"] += circ4["xSpd"] #moves circ4 x axis
    circ4["y"] += circ4["ySpd"] #moves circ4 y axis
    circ4["xSpd"] = random(-rand,rand) #choose new speed for next frame
    circ4["ySpd"] = random(-rand,rand) #choose new speed for next frame
    if circ4["x"] > width:
        circ4["x"] = width - diam
    if circ4["y"] > height:
        circ4["y"] = height - diam
    if circ4["x"] < 0:
        circ4["x"] = diam
    if circ4["y"] < 0:
        circ4["y"] = diam
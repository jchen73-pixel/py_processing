diam = 20		# diameter
rad = diam/2	# rad

def setup():
    size(500,360)
    global circ1, circ2, circ3
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
    global circ1, circ2, circ3
    background(220)
    #text(str(mouseX) + ", " + str(mouseY), 20, 20)
    
    circle(circ1["x"], int(height/2), diam) #circ1 moves right to left
    circle(int(width/2), circ2["y"], diam) #circ2 moves from top to bottom
    circle(circ3["x"], circ3["y"], diam) #circ3 moves diagonally
    
    circ1["x"] -= circ1["xSpd"] #moves circ1
    if circ1["x"] < 0:
        circ1["x"] = width + diam
        
    circ2["y"] += circ2["ySpd"] #moves circ2
    if circ2["y"] > height:
        circ2["y"] = 0
    
    circ3["x"] += circ3["xSpd"] #moves circ3 x axis
    circ3["y"] += circ3["ySpd"] #moves circ3 y axis
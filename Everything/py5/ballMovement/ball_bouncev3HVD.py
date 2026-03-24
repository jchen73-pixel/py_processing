diam = 20		# diameter
rad = diam/2	# rad
rand = rad/2	# random movement

def setup():
    size(500,360)
    global circ1, circ2, circ3, circ4
    circ1 = {
        "x": width + diam,
        "xSpd":3,
        "deltaX": 3,
        } 


    circ2 = {
        "y":diam,
        "ySpd": 2,
        "deltaY": 2,
        }
        
    circ3 = {
        "x": diam,
        "y": diam,
        "xSpd":4,
        "ySpd":1,
        "deltaX":4,
        "deltaY":1,
        }
    
    circ4 = {
        "x": width/2,
        "y": height/2,
        "xSpd": random(-rand,rand),
        "ySpd": random(-rand,rand),
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
    
#     circle(circ1["x"], int(height/2), diam) #circ1 moves right to left
#     circle(int(width/2), circ2["y"], diam) #circ2 moves from top to bottom
    circle(circ3["x"], circ3["y"], diam) #circ3 moves diagonally
#     circle(circ4["x"], circ4["y"], diam) #circ 4 moves randomly

#     if circ1["x"] <= rad:
#         circ1["deltaX"] = circ1["xSpd"]
#     if circ1["x"] >= width-rad:
#         circ1["deltaX"] = -circ1["xSpd"]
#     circ1["x"] += circ1["deltaX"] #moves circ1
#     
#     if circ2["y"] >= height-rad:
#         circ2["deltaY"] = -circ2["ySpd"]
#     if circ2["y"] <= rad:
#          circ2["deltaY"] = circ2["ySpd"]
#     circ2["y"] +=  circ2["deltaY"] #moves circ2
    
    if circ3["x"] <= rad:
        circ3["deltaX"] = circ3["xSpd"]
    if circ3["y"] <= rad:
        circ3["deltaY"] = circ3["ySpd"]
    if circ3["x"] >= width-rad:
        circ3["deltaX"] = -circ3["xSpd"]
    if circ3["y"] >= height-rad:
        circ3["deltaY"] = -circ3["ySpd"]
    circ3["x"] += circ3["deltaX"] #moves circ3 x axis
    circ3["y"] += circ3["deltaY"] #moves circ3 y axis
           
#     circ4["x"] += circ4["xSpd"] #moves circ4 x axis
#     circ4["y"] += circ4["ySpd"] #mif circ3["x"] <= rad:
#     circ4["xSpd"] = random(-rand,rand) #choose new speed for next frame
#     circ4["ySpd"] = random(-rand,rand) #choose new speed for next frame
#     if circ4["x"] > width:
#         circ4["x"] = width - diam
#     if circ4["y"] > height:
#         circ4["y"] = height - diam
#     if circ4["x"] < 0:
#         circ4["x"] = diam
#     if circ4["y"] < 0:
#         circ4["y"] = diam

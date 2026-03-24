diam = 20		# diameter
rad = diam/2	# rad

def setup():
    size(500,360)
    global circ1
    circ1 = {
        "x": width + diam,
        "xSpd":3,
        }

def draw():
    global circ1
    background(220)
    #text(str(mouseX) + ", " + str(mouseY), 20, 20)
    
    circle(circ1["x"], int(height/2), diam) #circ1 moves right to left
    
    circ1["x"] -= circ1["xSpd"] #moves circ1
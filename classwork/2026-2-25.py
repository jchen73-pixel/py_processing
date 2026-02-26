#randomColors = []
#randomChoice = None
stars = []

def setup():
    size(600, 600)
    background(0)
    stroke(255)
    frame_rate(10)
    gen_star()
    #global randomColors, randomChoice
    #randomColors = [
    #    color(255, 0, 0),
    #    color(0, 255, 0),
    #    color(0, 0, 255)
    #    ]
    #randomChoice = int(random(len(randomColors)))

def draw():
    global stars
    for star in stars:
        stroke_weight(star["stroke_weight"])
        stroke(star["color"])
        point(star["x"], star["y"])
        star["color"] = color(int(random(255)), int(random(255)), int(random(255)))
        
        
    #background(220)
    #fill(randomColors[randomChoice])
    #circle(200, 200, 100)

#def mouse_pressed():
    #global randomChoice
    #randomChoice = int(random(len(randomColors)))

def gen_star():
    for i in range(1, 3000, 1):
        global stars
        stars.append( {
            "x": int(random(width)),
            "y": int(random(height)),
            "color": color(int(random(255)), int(random(255)), int(random(255))),
            "stroke_weight": int(random(3))
        })
angle = 15
def setup():
    size(510, 350)
def draw():
    background(220)
    global angle
    sine_value = sin(radians(angle))
    y1 = remap(sine_value, -1, 1, 70, 230)
    circle(width/2, y1, 50)
    z1 = remap(sine_value, -1, 1, 135, 215)
    circle(z1, z1, 50)
    r1 = remap(sine_value, -1, 1, 50, 100)
    circle(260, 175, r1)
    angle += 1
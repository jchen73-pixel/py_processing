t = 0

def setup():
    size(600, 600)

def draw():
    global t

    background(240)
    translate(width / 2, height / 2)
    rect_mode(CENTER)

    s = 0.5 + 0.4 * sin(t)
    scale(s)

    fill(100, 150, 255)
    no_stroke()
    square(0, 0, 300)

    t += 0.05
scal = 0

def setup():
    size(600, 600)
    no_stroke()
    fill(255)
    frame_rate(10)

def draw():
    global scal
    background(0)
    translate(width/2, height/2)
    for i in range(12):
        push_matrix()
        scale(0.5 + 0.4 *sin(scal))
        ellipse(0, 150, 50, 100)
        pop_matrix()
        rotate(radians(scal))
        scal += 0.5
from wigglerClass import *

num_wigglers = 20
wigglers = []

def setup():
    size(510,350)
    global wigglers
    for i in range(num_wigglers):
        wigglers.append(Wiggler(random(30,40),random(30,40)))
    background(220)

def draw():
    global wigglers
    background(220)
    #text(str(mouseX) + ", " + str(mouseY), 20, 20)
    #no_stroke()

    for w in wigglers:
        w.animate()


from Tamogatchi import *
def setup():
    size(500, 500)
    global a
    global im
    a = Tamogatchi("Snor", 50, 50, 100, color(0,1,2), 10, 10)
    
def draw():
    background(220)
    fill(0)
    text("Name: " + str(a.name), 10, 10)
    a.animate()
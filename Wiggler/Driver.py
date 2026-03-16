from wigglerClass import *

def setup():
    size(510,350)
    global wiggler1 	#global because we will use it in draw later!
    global wiggler2
    global wiggler3
    wiggler1 = Wiggler(35, 35)
    wiggler2 = Wiggler(35, 35)
    wiggler3 = Wiggler(35, 35)

def draw():
    #text(str(mouseX) + ", " + str(mouseY), 20, 20)
    wiggler1.display()
    wiggler2.display()
    wiggler3.display()
    wiggler1.bounceOnEdge()
    wiggler2.bounceOnEdge()
    wiggler3.bounceOnEdge()
    wiggler1.animate()
    wiggler2.animate()
    wiggler3.animate()
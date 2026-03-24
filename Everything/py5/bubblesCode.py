from bubblesClass import *

num_bubbles = 20
bubbles = []

def setup():
    size(510,350)
    global bubbles
    for i in range(num_bubbles):
        bubbles.append(Bubble(random(25,50)))
    background(220)
    
#     for i in range(0,360,5):
#         stroke(random(255),random(255),random(255))
#         arc(200,200,30,30,radians(i),radians(i+10),OPEN)

def draw():
    global bubbles
    background(220)
    #text(str(mouseX) + ", " + str(mouseY), 20, 20)
    #no_stroke()

    for b in bubbles:
        b.animate()


    


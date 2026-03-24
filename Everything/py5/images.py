def setup():
    size(400,400)
def draw():
    background(220)
    #text(str(mouse_x) + ", " + str(mouse_y), 20, 20)
    creep_face(200,200)
def creep_face(xPos, yPos, eyeSize=10):
    fill(255, 255, 0)
    stroke(0)
    stroke_weight(0)
    ellipse(xPos,yPos,100,100) #200, 200
    stroke_weight(1)
    ellipse(xPos-20, yPos, eyeSize, eyeSize)
    stroke_weight(5)
    ellipse(xPos+20, yPos, 20, 20)
    stroke_weight(1)
    rect(xPos-20, yPos+20, 40, 4)

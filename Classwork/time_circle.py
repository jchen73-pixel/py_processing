def setup():
    size(400,400)

def draw():
    background(220)
    
    theSecond = second()
    
    #uncomment the line below for a better result
    theSecond = remap(second(), 0, 59, 20, 200) 
    
    ellipse(200, 200, theSecond, theSecond)
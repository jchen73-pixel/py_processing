def setup():
    size(400,400)
    global bgColor
    bgColor = 220

def draw():
    global bgColor
    background(bgColor)
    
    theSecond = remap(second(), 0, 59, 20, 200)
    theMinute = minute()
    theHour = hour()
    
    circle(200, 200, theSecond)
    
    # Since we do not have 13 hours to wait,
    # change the "<" for ">" after you run this once
    # so you can see what the afternoon will look like
    if theHour < 12:
        bgColor = 0
    else:
        bgColor = 220
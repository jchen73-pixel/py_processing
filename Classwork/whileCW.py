def setup():
    size(400, 400)
    background(220)
    
def draw():
    #rings()
    #smile()
    #large_color()
    grid()

def rings():
    x = 40
    while x < width:
        y = 60
        while y > 0:
            circle(x, 60, y)
            y -= 10
        x += 80

def smile():
    x = 40
    while x < width:
        circle(x, 60, 60)
        stroke_weight(3)
        point(x-10, 50)
        point(x+10, 50)
        stroke_weight(1)
        arc(x, 60, 30, 30, 0, PI)
        x += 80

def large_color():
    x = 60
    b = 0
    for r in range(10, 60, 10):
        fill(0, 0, b)
        circle(x, 60, r)
        x += 60
        b += 60

def grid():
    for x in range(0, width, 30):
        for y in range(0, height, 30):
            circle(x, y, 20)
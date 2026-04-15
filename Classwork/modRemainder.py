from math import *
def setup():
    size(400, 400)
    #print("remainder of -10 / 3 =", remainder(-10, 3))
    #print("mod of -10 / 3 =", str(-10 % 3))
    #print("\nremainder of 10 / -3 =", remainder(10, -3))
    #print("mod of 10 / -3 =", str(10 % -3))
def draw():
    #no_stroke()
    #m = millis()
    #fill(m % 255)
    #rect(100, 100, 50, 50)
    push_matrix()
    translate(width / 2, height / 2)
    circle(0, 0, 200)
    stroke_weight(2)
    hourRad = remap(hour(), 0, 12, 0, TWO_PI)
    minRad = remap(minute(), 0, 60, 0, TWO_PI)
    secRad = remap(second(), 0, 60, 0, TWO_PI)
    line(0, 0, 30 * cos(hourRad - HALF_PI), 30 * sin(hourRad - HALF_PI))
    line(0, 0, 60 * cos(minRad - HALF_PI), 60 * sin(minRad - HALF_PI))
    line(0, 0, 90 * cos(secRad - HALF_PI), 90 * sin(secRad - HALF_PI))
    stroke_weight(1)
    for i in range(12):
        tickRad = remap(i, 0, 12, 0, TWO_PI)
        line(90 * cos(tickRad), 90 * sin(tickRad), 100 * cos(tickRad), 100 * sin(tickRad))
    
    pop_matrix()
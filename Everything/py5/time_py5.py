def setup():
    size(400,400)
    fill(0)
    date_str = str(month())+"/"+str(day())+"/"+str(year())
    text_size(50)
    text(date_str,50,height-50)
    
def draw():
    m = millis()
    no_stroke()
    fill(m % 255)
    rect(100, 100, 50, 50)
    
    #uncomment the background line below to better appreciate the second/minute/hour code
    #be aware that the date and the millisecond rectangle above will dissapear
#     background(204) 
    fill(0)
    stroke(0)
    stroke_weight(3)
    s = second()  # Values from 0 - 59
    m = minute()  # Values from 0 - 59
    h = hour()  # Values from 0 - 23
    line(s, 0, s, 33)
    line(m, 33, m, 66)
    line(h, 66, h, 100)
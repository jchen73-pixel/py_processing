def setup():
    global d,mo,y
    size(400,400)
    d = day()
    mo = month()
    y = year()
    
def draw():
    global d,mo,y
    background(204)
    
    # second, minutes & hour
    s = second()  # Values from 0 - 59
    m = minute()  # Values from 0 - 59
    h = hour()  # Values from 0 - 23
    
    #digital clock
    fill(0)
    text_size(50)
    zm = ""
    zs = ""
    if m < 10: zm = "0"
    if s < 10: zs = "0"
    dh = h % 12 # 12 hour clock
    txt = str(dh) + ":" + zm + str(m) + ":" + zs + str(s)
    text(txt, 50, height-125)
    
    #date - can't run over midnight, info is global
    date_str = str(mo)+"/"+str(d)+"/"+str(y)
    text(date_str,50, height-50)
    
    #line "clock"
    stroke(0)
    stroke_weight(2)
    line(s, 0, s, 33)
    line(m, 33, m, 66)
    line(h, 66, h, 100)
    
    #millisecond rectangle
    m = millis()
    no_stroke()
    fill(m % 255)
    rect(100, 100, 50, 50)

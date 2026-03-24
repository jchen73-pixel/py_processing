def setup():
    size(400,400)
    background(220)

def draw(): 
    fill(0)
    if is_mouse_pressed:
        line(mouse_x, mouse_y, pmouse_x, pmouse_y)
    for x in [20,361,30]:
        circle(x,370,20)

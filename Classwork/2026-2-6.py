def setup():
    size(400, 400)
    background(220)
    
def draw():    
    fill(0)
    text("I'm drawing", 20, 20)
    text(frame_count, 100, 20)
    
    circle(300, 80, 10)
    line(mouse_x, mouse_y, pmouse_x, pmouse_y)
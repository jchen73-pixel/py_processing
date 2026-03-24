def setup():
    size(500,500)

def draw():
    bgcolor = remap(mouse_x, 0, width, 0, 255)

    background(bgcolor)

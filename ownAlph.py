import numpy as np

landscape, cheese, mode = None, None, None
radius = 10

def setup():
    global landscape, cheese
    size(1280, 850)
    no_stroke()
    cheese = copy_image("Classwork/cheese.jpg")
    landscape = copy_image("landscape.jpg")

def copy_image(name):
    img = load_image(name)
    img.resize(width, height)
    image(img, 0, 0)
    load_np_pixels()
    return np_pixels.copy()

def mouse_circle(radius):
    positions = []
    for x in range(width):
        for y in range(height):
            if x + y - mouse_x - mouse_x < radius - 1:
                positions.append([x, y])
    return positions

def mouse_pressed():
    #if mode == "i":
    impacted = mouse_circle(radius)
    for pix in impacted:
        x = pix[0]
        y = pix[1]
        print(x, " ", y)
        np_pixels[x, y, 0] = np.clip(255 - landscape[x, y, 0], 0, 255)
        update_np_pixels()

def draw():
    global mode
    if is_key_pressed:
        mode = key
    update_np_pixels()
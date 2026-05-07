import numpy as np
def setup():
    global original, cheese
    size(1280, 850)
    img = load_image("landscape.jpg")
    img.resize(width, height)
    image(img, 0, 0)
    no_stroke()
    load_np_pixels()
    original = np_pixels.copy()
    img = load_image("Classwork/cheese.jpg")
    img.resize(width, height)
    image(img, 0, 0)
    load_np_pixels()
    cheese = np_pixels.copy()
    
def draw():
    bright = remap(mouse_y, 0, height, 0, 1)
    np_pixels[:, :, 1] = np.clip(original[:, :, 1] * bright + cheese[:, :, 1] * (1 - bright), 0, 255)
    np_pixels[:, :, 2] = np.clip(original[:, :, 2] * bright + cheese[:, :, 2] * (1 - bright), 0, 255)
    np_pixels[:, :, 3] = np.clip(original[:, :, 3] * bright + cheese[:, :, 3] * (1 - bright), 0, 255)
    update_np_pixels()

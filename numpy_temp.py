import numpy as np
def setup():
    global original
    size(1280, 850)
    img = load_image("landscape.jpg")
    img.resize(width, height)
    image(img, 0, 0)
    no_stroke()
    load_np_pixels()
    original = np_pixels.copy()
    
def draw():
    temp = remap(mouse_x, 0, width, -100, 100)
    bright = remap(mouse_y, 0, width, 70, -100)
    np_pixels[:, :, 1] = np.clip(original[:, :, 1] + temp + bright, 0, 255)
    np_pixels[:, :, 2] = np.clip(original[:, :, 2] + temp * 0.3 + bright, 0, 255)
    np_pixels[:, :, 3] = np.clip(original[:, :, 3] - temp + bright, 0, 255)
    update_np_pixels()
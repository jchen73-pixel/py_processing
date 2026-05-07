import numpy as np
def setup():
    global original
    size(1280, 850)
    img = load_image("image.jpg")
    img.resize(width, height)
    image(img, 0, 0)
    no_stroke()
    load_np_pixels()
    original = np_pixels.copy()
    
def draw():
    for y in range(1, width - 1):
        for x in range(1, height - 1):
            grayRed = 0
            grayRed += int(original[x, y, 1])
            grayRed += int(original[x - 1, y, 1])
            grayRed += int(original[x + 1, y, 1])
            grayRed += int(original[x, y - 1, 1])
            grayRed += int(original[x + 1, y + 1, 1])
            grayRed += int(original[x + 1, y - 1, 1])
            grayRed += int(original[x - 1, y + 1, 1])
            grayRed += int(original[x - 1, y - 1, 1])
                
            grayGreen = 0
            grayGreen += int(original[x, y, 2])
            grayGreen += int(original[x - 1, y, 2])
            grayGreen += int(original[x + 1, y, 2])
            grayGreen += int(original[x, y - 1, 2])
            grayGreen += int(original[x, y + 1, 2])
            grayGreen += int(original[x + 1, y + 1, 2])
            grayGreen += int(original[x + 1, y - 1, 2])
            grayGreen += int(original[x - 1, y + 1, 2])
            grayGreen += int(original[x - 1, y - 1, 2])
                
            grayBlue = 0
            grayBlue += int(original[x, y, 3])
            grayBlue += int(original[x - 1, y, 3])
            grayBlue += int(original[x + 1, y, 3])
            grayBlue += int(original[x, y - 1, 3])
            grayBlue += int(original[x, y + 1, 3])
            grayBlue += int(original[x + 1, y + 1, 3])
            grayBlue += int(original[x + 1, y - 1, 3])
            grayBlue += int(original[x - 1, y + 1, 3])
            grayBlue += int(original[x - 1, y - 1, 3])
                
            np_pixels[x, y, 1] = np.clip(int(grayRed)/9, 0, 255)
            np_pixels[x, y, 2] = np.clip(int(grayGreen)/9, 0, 255)
            np_pixels[x, y, 3] = np.clip(int(grayBlue)/9, 0, 255)
    update_np_pixels()
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
    for y in range(1, width - 1):
        for x in range(1, height - 1):
            if (x < height/2 and y < width/2):
                np_pixels[x, y, 1] = np.clip(255 - original[x, y, 1], 0, 255)
                np_pixels[x, y, 2] = np.clip(255 - original[x, y, 2], 0, 255)
                np_pixels[x, y, 3] = np.clip(255 - original[x, y, 3], 0, 255)
            if (x > height/2 and y < width/2):
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
                
            elif (x < height/2 and y > width/2):
                gap = 100
                np_pixels[x, y, 1] = np.clip(int(int(original[x, y, 1])/gap)*gap, 0, 255)
                np_pixels[x, y, 2] = np.clip(int(int(original[x, y, 2])/gap)*gap, 0, 255)
                np_pixels[x, y, 3] = np.clip(int(int(original[x, y, 3])/gap)*gap, 0, 255)
                
            #else if (x > height/2 and y > width/2):
    update_np_pixels()

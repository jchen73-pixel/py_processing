import numpy as np
def setup():
    size(640, 425)
    img = load_image("landscape.jpg")
    img.resize(width, height)
    image(img, 0, 0)
    load_np_pixels()
    original = np_pixels.copy()
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            for colr in range(1, 4):
                colrSum = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        colrSum += int(original[y + i, x + j, colr])
                np_pixels[y, x, colr] = np.clip(colrSum//9, 0, 255)
    update_np_pixels()
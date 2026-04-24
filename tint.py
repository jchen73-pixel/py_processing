pixelList = {}
def setup():
    global img
    size(400, 400)
    img = load_image("Classwork/cheese.jpg")
    img.resize(width, height)
    image(img, 0, 0)
    for i in range(width):
        for j in range(height):
            pixelList[(str(i) + "," + str(j))] = get_pixels(i, j)
    no_stroke()
    no_loop()

def draw():
    background(255)
    for i in range(width):
        for j in range(height):
            c = pixelList[str(i) + "," + str(j)]
            origRed = red(c)
            origGreen = green(c)
            origBlue = blue(c)
            if i < width // 2 and j < height // 2:
                fill(origRed, origGreen, origBlue, 255)
            elif i >= width // 2 and j < height // 2:
                fill(origRed, origGreen * 0.5, origBlue * 0.5, 191)
            elif i < width // 2 and j >= height // 2:
                fill(origRed * 0.5, origGreen, origBlue * 0.5, 127)
            else:
                fill(origRed * 0.5, origGreen * 0.5, origBlue, 64)
            square(i, j, 1)

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
    for i in range(width // 2):
        for j in range(height // 2):
            origRed = red(get_pixels(i, j))
            origGreen = green(get_pixels(i, j))
            origBlue = blue(get_pixels(i, j))
            fill(origRed * 0.25, origGreen * 0.25, origBlue * 0.25)
            square(i,j,1)
    for i in range(width // 2):
        for j in range(height // 2):
            origRed = red(get_pixels(i, j + height // 2))
            origGreen = green(get_pixels(i, j + height // 2))
            origBlue = blue(get_pixels(i, j + height // 2))
            fill(origRed * 0.5, origGreen * 0.5, origBlue * 0.5)
            square(i,j + height // 2,1)
    for i in range(width // 2):
        for j in range(height // 2):
            origRed = red(get_pixels(i + width // 2, j + width // 2))
            origGreen = green(get_pixels(i + width // 2, j + width // 2))
            origBlue = blue(get_pixels(i + width // 2, j + width // 2))
            fill(origRed * 0.75, origGreen * 0.75, origBlue * 0.75)
            square(i + width // 2,j + height // 2,1)
    update_pixels()

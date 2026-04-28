pixelList = {}
temp = 0
def setup():
    global img
    size(200, 200)
    img = load_image("Classwork/cheese.jpg")
    img.resize(width, height)
    image(img, 0, 0)
    no_stroke()
    load_pixels()
    for i in range(width):
        for j in range(height):
            pixelList[(str(i) + "," + str(j))] = get_pixels(i, j)

def mouse_pressed():
    global temp
    temp = remap(mouse_x, 0, width, -100, 100)

def draw():
    global temp
    load_pixels()
    for i in range(width):
        for j in range(height):
            c = pixelList[str(i) + "," + str(j)]
            pixels[j * height + i] = color(red(c) - temp, green(c) + temp * 0.3, blue(c) + temp)
    update_pixels()
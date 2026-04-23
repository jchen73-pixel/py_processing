pixelList = {}
def setup():
    size(400, 400)
    img = load_image("PRFlag.jpg")
    img.resize(width // 2, 0)
    image(img, 20, 20)
    #load_pixels
    for i in range(width):
        for j in range(height):
            pixelList[(str(i) + "," + str(j))] = get_pixels(i, j)
    background(220)

def draw():
    no_stroke()
    fill(pixelList[str(mouse_x) + "," + str(mouse_y)])
    circle(mouse_x, mouse_y, 10)
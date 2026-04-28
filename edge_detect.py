def setup():
    size(400, 400)
    img = load_image("moran.jpg")
    img.resize(width, height)
    image(img, 0, 0)
    no_stroke()
    no_loop()
    load_pixels()
    
def draw():
    load_pixels()
    thresh = 7
    for i in range(width):
        for j in range(height):
            c = get_pixels(i, j)
            bright = (red(c) + green(c) + blue(c)) / 3
            bot = get_pixels(i, j + 1)
            bBright = (red(bot) + green(bot) + blue(bot)) / 3
            right = get_pixels(i + 1, j)
            rBright = (red(right) + green(right) + blue(right)) / 3
            left = get_pixels(i - 1, j)
            lBright = (red(left) + green(left) + blue(left)) / 3
            top = get_pixels(i, j - 1)
            tBright = (red(top) + green(top) + blue(top)) / 3
            if ((bright - bBright > thresh) or (bright - rBright > thresh) or (bright - tBright > thresh) or (bright - lBright > thresh)):
                pixels[i + j * height] = color(255)
            else:
                pixels[i + j * height] = color(0)
    update_pixels()
from PIL import image
im = Image.open('Pictures/Cute Dog.jpg')
def setup():
    size(300, 300)
def draw():
    #Image(name, x, y, width, height)
    image(im, 10, 10, 250, 250)
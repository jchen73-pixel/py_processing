from PIL import Image
# Open the image’s file 
im = Image.open('images/cuteDog.jpg')
def setup():
    size(300,300)
def draw():
    # image(name,x,y,width,height)
    image(im, 10, 10, 250, 250)

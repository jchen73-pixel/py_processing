def setup():
    size(500, 500)
    global img, pDictionary
    img = load_image("PRFlag.jpg")
    
    
    #background(220) # cover image

def draw():
    background(220)
    img.resize(400,0)
    image(img,50,50)
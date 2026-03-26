from Tile import *
tiles = []
def setup():
    global a
    size(600, 600)
    genTiles()
    a = Tile(200, 200, 1, 0, 0, "A")
    a.display()
def draw():
    background(225)
    a.animate()
def genTiles():
    for i in range(200):
        direction = ["left", "right"]
        tiles.append(Tile(random(0, width), 0, 1, random.choice(direction), 0, "A"))
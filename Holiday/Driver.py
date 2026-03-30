from Tile import *
import time
tiles = []
delay = 0
sinceLast = 0
def setup():
    global a
    size(600, 600)

def draw():
    global sinceLast
    global delay
    background(225)
    if len(tiles) < 200:
        if sinceLast < delay:
            sinceLast+=1
        else:
            sinceLast = 0
            delay = random(25,50)
            genTile()
    for tile in tiles:
        if tile.checkDead():
            tiles.remove(tile)
        else:
            tile.display()
    
def genTile():
    direction = ["left", "right"]
    tiles.append(Tile(random(0, width), -50, 1, direction[int(random(0, 2))], 0, "A"))
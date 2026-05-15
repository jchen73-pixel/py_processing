import numpy as np
state = [[255, 255, 255], [255, 0, 0], [0, 255, 0], [0, 0, 255]]
def setup_pixels():
    for x in range(width):
        for y in range(height):
            chosen = int(random(0, 4))
            np_pixels[y,x,1] = state[chosen][0]
            np_pixels[y,x,2] = state[chosen][1]
            np_pixels[y,x,3] = state[chosen][2]
    update_np_pixels()
    
def setup():
    global p
    size(200, 200)
    p = []
    load_np_pixels()
    setup_pixels()
    
    
def evaluate_neighbors():
    load_np_pixels()
    global p
    for x in range(width):
        temp = []
        for y in range(height):
            pix = []
            pix.append(np_pixels[x, y, 1])
            pix.append(np_pixels[x, y, 2])
            pix.append(np_pixels[x, y, 3])
            temp.append(pix)
        p.append(temp)
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            colors = []
            for i in range(3):
                for j in range(3):
                    colors.append(p[x - 1 + i][y - 1 + j])
            colors.pop(4)
            mostCol = max(colors.count(state[0]), colors.count(state[1]), colors.count(state[2]), colors.count(state[3]))
            if colors.count(state[0]) == mostCol:
                p[x][y] = state[0]
            elif colors.count(state[1]) == mostCol:
                p[x][y] = state[1]
            elif colors.count(state[2]) == mostCol:
                p[x][y] = state[2]
            elif colors.count(state[3]) == mostCol:
                p[x][y] = state[3]
            

def transition():
    global p
    for x in range(width):
        for y in range(height):
            np_pixels[x,y,1] = p[x][y][0]
            np_pixels[x,y,2] = p[x][y][1]
            np_pixels[x,y,3] = p[x][y][2]
    update_np_pixels()
    
def draw():
    evaluate_neighbors()
    transition()
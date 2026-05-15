import numpy as np
state = [[255, 0, 0, 0], [255, 255, 0, 0]]
def setup_pixels():
    for x in range(width):
        row = []
        for y in range(height):
            row.append(state[0])
        p.append(row)
    np_pixels[int(width/2), int(height/2)] = state[1]
    np_pixels[int(width/2+1), int(height/2)] = state[1]
    np_pixels[int(width/2-1), int(height/2)] = state[1]
    np_pixels[int(width/2+2), int(height/2)] = state[1]
    np_pixels[int(width/2-2), int(height/2)] = state[1]
    np_pixels[int(width/2+2), int(height/2+1)] = state[1]
    np_pixels[int(width/2+2), int(height/2+2)] = state[1]
    np_pixels[int(width/2-2), int(height/2+1)] = state[1]
    np_pixels[int(width/2-2), int(height/2+2)] = state[1]
    np_pixels[int(width/2+2), int(height/2-1)] = state[1]
    np_pixels[int(width/2+2), int(height/2-2)] = state[1]
    np_pixels[int(width/2-2), int(height/2-1)] = state[1]
    np_pixels[int(width/2-2), int(height/2-2)] = state[1]
    update_np_pixels()
    
def setup():
    global p
    size(200, 200)
    p = []
    background(0)
    load_np_pixels()
    setup_pixels()
    
def evaluate_neighbors():
    load_np_pixels()
    global p, state
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            count = 0
            if np.array_equal(np_pixels[y - 1, x,:], state[1]):
                count+=1
            if np.array_equal(np_pixels[y + 1, x,:], state[1]):
                count+=1
            if np.array_equal(np_pixels[y, x - 1,:], state[1]):
                count+=1
            if np.array_equal(np_pixels[y, x + 1,:], state[1]):
                count+=1
            if count%2 == 0:
                p[x][y] = state[0]
            else:
                p[x][y] = state[1]

def transition():
    global p
    for x in range(width):
        for y in range(height):
            np_pixels[x,y,1] = p[x][y][1]
            np_pixels[x,y,2] = p[x][y][2]
            np_pixels[x,y,3] = p[x][y][3]
    update_np_pixels()
    
def draw():
    evaluate_neighbors()
    transition()

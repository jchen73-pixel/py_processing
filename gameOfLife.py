import numpy as np
state = [[255, 0, 0, 0], [255, 0, 255, 0]]
def setup_pixels():
    for x in range(width):
        row = []
        for y in range(height):
            chosen = random(1)
            if chosen < 0.1:
                np_pixels[y, x] = state[1]
                row.append(state[1])
            else:
                row.append(state[0])
        p.append(row)
    update_np_pixels()
    
def setup():
    global p
    size(200, 200)
    frame_rate(10)
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
            if np.array_equal(np_pixels[y - 1, x - 1,:], state[1]):
                count+=1
            if np.array_equal(np_pixels[y, x - 1,:], state[1]):
                count+=1
            if np.array_equal(np_pixels[y + 1, x - 1,:], state[1]):
                count+=1
            if np.array_equal(np_pixels[y + 1, x,:], state[1]):
                count+=1
            if np.array_equal(np_pixels[y - 1, x,:], state[1]):
                count+=1
            if np.array_equal(np_pixels[y - 1, x + 1,:], state[1]):
                count+=1
            if np.array_equal(np_pixels[y, x + 1,:], state[1]):
                count+=1
            if np.array_equal(np_pixels[y + 1, x + 1,:], state[1]):
                count+=1
            if count < 2:
                p[y][x] = state[0]
            elif count == 3:
                p[y][x] = state[1]
            elif count == 2 and p[y][x] == state[1]:
                p[y][x] = state[1]
            else:
                p[y][x] = state[0]
            

def transition():
    global p
    for x in range(width):
        for y in range(height):
            np_pixels[x,y,1] = p[y][x][1]
            np_pixels[x,y,2] = p[y][x][2]
            np_pixels[x,y,3] = p[y][x][3]
    update_np_pixels()
    
def draw():
    evaluate_neighbors()
    transition()
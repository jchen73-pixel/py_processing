import random

grid_size = 4
block_w = 0
block_h = 0
empty_c = grid_size - 1
empty_r = grid_size - 1
selected_c = -1
selected_r = -1

def setup():
    size(400, 400)
    global block_w, block_h, empty_c, empty_r
    block_w = width // grid_size
    block_h = height // grid_size
    
    # Load image
    img = load_image("Classwork/cheese.jpg")
    img.resize(width, height)
    img.load_pixels()
    
    # Initialize the canvas pixels array
    load_pixels()
    
    # Logical shuffle to prevent freezing!
    # Instead of swapping 10,000 pixels 300 times (which takes too long in Python), 
    # we shuffle a virtual board and then draw it to the pixels array ONCE.
    board = []
    for r in range(grid_size):
        row = []
        for c in range(grid_size):
            row.append((c, r))
        board.append(row)
        
    for _ in range(300):
        neighbors = []
        if empty_c > 0: neighbors.append((empty_c - 1, empty_r))
        if empty_c < grid_size - 1: neighbors.append((empty_c + 1, empty_r))
        if empty_r > 0: neighbors.append((empty_c, empty_r - 1))
        if empty_r < grid_size - 1: neighbors.append((empty_c, empty_r + 1))
        
        nc, nr = random.choice(neighbors)
        
        board[empty_r][empty_c], board[nr][nc] = board[nr][nc], board[empty_r][empty_c]
        
        empty_c = nc
        empty_r = nr

    # Now apply the logically shuffled board to the canvas pixels
    black_color = color(0)
    for r in range(grid_size):
        for c in range(grid_size):
            orig_c, orig_r = board[r][c]
            
            # If this is the missing corner piece (originally at bottom-right)
            if orig_c == grid_size - 1 and orig_r == grid_size - 1:
                for y in range(block_h):
                    for x in range(block_w):
                        dest_idx = (c * block_w + x) + (r * block_h + y) * width
                        pixels[dest_idx] = black_color
            else:
                for y in range(block_h):
                    for x in range(block_w):
                        src_idx = (orig_c * block_w + x) + (orig_r * block_h + y) * width
                        dest_idx = (c * block_w + x) + (r * block_h + y) * width
                        pixels[dest_idx] = img.pixels[src_idx]
                        
    update_pixels()

def mouse_pressed():
    global empty_c, empty_r, selected_c, selected_r
    
    # Safe bounds checking to prevent edge-case crashes
    clicked_c = max(0, min(mouse_x // block_w, grid_size - 1))
    clicked_r = max(0, min(mouse_y // block_h, grid_size - 1))
    
    # If a block is currently selected
    if selected_c != -1 and selected_r != -1:
        # Check if the user clicked the black box
        if clicked_c == empty_c and clicked_r == empty_r:
            # Check if the selected block is adjacent to the black box
            if (abs(selected_c - empty_c) == 1 and selected_r == empty_r) or \
               (abs(selected_r - empty_r) == 1 and selected_c == empty_c):
                
                # Transfer happens! Swap pixels
                for y in range(block_h):
                    for x in range(block_w):
                        idx1 = (selected_c * block_w + x) + (selected_r * block_h + y) * width
                        idx2 = (empty_c * block_w + x) + (empty_r * block_h + y) * width
                        
                        temp = pixels[idx1]
                        pixels[idx1] = pixels[idx2]
                        pixels[idx2] = temp
                
                # Update the new empty block position to where the selected block was
                empty_c = selected_c
                empty_r = selected_r
                
        # Deselect in all scenarios after the second click
        selected_c = -1
        selected_r = -1
    else:
        # First click: Select it if it's not the black box.
        if not (clicked_c == empty_c and clicked_r == empty_r):
            selected_c = clicked_c
            selected_r = clicked_r

def draw():
    # Calling update_pixels restores the canvas from the pixels array,
    # effectively erasing the border from the previous frame.
    update_pixels()
    
    # Draw grid lines for better visibility of the puzzle blocks
    stroke(0)
    stroke_weight(1)
    for i in range(1, grid_size):
        line(i * block_w, 0, i * block_w, height)
        line(0, i * block_h, width, i * block_h)
    
    # Highlight the selected block
    if selected_c != -1:
        no_fill()
        stroke(255, 0, 0) # Red border
        stroke_weight(4)
        rect(selected_c * block_w, selected_r * block_h, block_w, block_h)

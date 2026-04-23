import random

grid_size = 4
block_widths = 0
block_heights = 0
empty_column = grid_size - 1
empty_row = grid_size - 1
selected_column = -1
selected_row = -1

def setup():
    size(400, 400)
    global block_widths, block_heights, empty_column, empty_row
    block_widths = width // grid_size
    block_heights = height // grid_size
    img = load_image("Classwork/cheese.jpg")
    img.resize(width, height)
    img.load_pixels()
    load_pixels()
    board = []
    for r in range(grid_size):
        row = []
        for c in range(grid_size):
            row.append((c, r))
        board.append(row)
        
    for i in range(300):
        neighbors = []
        if empty_column > 0: neighbors.append((empty_column - 1, empty_row))
        if empty_column < grid_size - 1: neighbors.append((empty_column + 1, empty_row))
        if empty_row > 0: neighbors.append((empty_column, empty_row - 1))
        if empty_row < grid_size - 1: neighbors.append((empty_column, empty_row + 1))
        nc, nr = random.choice(neighbors)
        board[empty_row][empty_column], board[nr][nc] = board[nr][nc], board[empty_row][empty_column]
        empty_column = nc
        empty_row = nr
    black_color = color(0)
    for r in range(grid_size):
        for c in range(grid_size):
            orig_c, orig_r = board[r][c]
            if orig_c == grid_size - 1 and orig_r == grid_size - 1:
                for y in range(block_heights):
                    for x in range(block_widths):
                        dest_idx = (c * block_widths + x) + (r * block_heights + y) * width
                        pixels[dest_idx] = black_color
            else:
                for y in range(block_heights):
                    for x in range(block_widths):
                        src_idx = (orig_c * block_widths + x) + (orig_r * block_heights + y) * width
                        dest_idx = (c * block_widths + x) + (r * block_heights + y) * width
                        pixels[dest_idx] = img.pixels[src_idx]
    update_pixels()

def mouse_pressed():
    global empty_column, empty_row, selected_column, selected_row
    clicked_c = max(0, min(mouse_x // block_widths, grid_size - 1))
    clicked_r = max(0, min(mouse_y // block_heights, grid_size - 1))
    if selected_column != -1 and selected_row != -1:
        if clicked_c == empty_column and clicked_r == empty_row:
            if (abs(selected_column - empty_column) == 1 and selected_row == empty_row) or \
               (abs(selected_row - empty_row) == 1 and selected_column == empty_column):
                for y in range(block_heights):
                    for x in range(block_widths):
                        idx1 = (selected_column * block_widths + x) + (selected_row * block_heights + y) * width
                        idx2 = (empty_column * block_widths + x) + (empty_row * block_heights + y) * width
                        temp = pixels[idx1]
                        pixels[idx1] = pixels[idx2]
                        pixels[idx2] = temp
                empty_column = selected_column
                empty_row = selected_row
        selected_column = -1
        selected_row = -1
    else:
        if not (clicked_c == empty_column and clicked_r == empty_row):
            selected_column = clicked_c
            selected_row = clicked_r

def draw():
    update_pixels()
    stroke(0)
    stroke_weight(1)
    for i in range(1, grid_size):
        line(i * block_widths, 0, i * block_widths, height)
        line(0, i * block_heights, width, i * block_heights)
    if selected_column != -1:
        no_fill()
        stroke(255, 0, 0)
        stroke_weight(4)
        rect(selected_column * block_widths, selected_row * block_heights, block_widths, block_heights)
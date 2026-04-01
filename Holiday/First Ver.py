from Tile import *

falling_tiles = []
tile_delay = 0
tile_timer = 0

GREEN = color(106, 170, 100)
YELLOW = color(201, 180, 88)
WORDLE_GRAY = color(120, 124, 126)
DARK_GRAY = color(58, 58, 60)
LIGHT_GRAY = color(211, 214, 218)
WHITE = color(255, 255, 255)
BG_COLOR = color(18, 18, 19)

def setup():
    size(600, 750)
    text_align(CENTER, CENTER)
    try:
        font = create_font("Helvetica", 48)
        text_font(font)
    except:
        pass

def draw():
    global tile_timer, tile_delay, message_timer
    background(BG_COLOR)
    if len(falling_tiles) < 120:
        if tile_timer < tile_delay:
            tile_timer += 1
        else:
            tile_timer = 0
            tile_delay = random(20, 45)
            genTile()
    for tile in falling_tiles:
        if tile.checkDead():
            falling_tiles.remove(tile)
        else:
            tile.checkHover(mouse_x, mouse_y)
            tile.display()
    # dark layer between tiles and wordle to look nicer
    no_stroke()
    fill(18, 18, 19, 180)
    rect(0, 0, width, height)
    drawTitle()
    drawWordleGrid()
    drawKeyboard()

def drawTitle():
    text_size(36)
    title = "GLOBAL WORD GAMES DAY"
    max_width = text_width(title)
    charX = (width - max_width) / 2.0
    color_cycle = [GREEN, YELLOW, WHITE, GREEN, YELLOW]
    text_align(LEFT, CENTER)
    for i in range(len(title)):
        char = title[i]
        colr = color_cycle[i % len(color_cycle)]
        fill(colr)
        text(char, charX, 100)
        charX += text_width(char)
    text_align(CENTER, CENTER)

def drawWordleGrid():
    no_stroke()
    stroke(DARK_GRAY)
    stroke_weight(2)
    no_fill()
    for row in range(6):
        for col in range(5):
            x = 173 + 52 * col
            y = 170 + 52 * row
            rect(x, y, 46, 46, 5)

keyboard = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
key_colors = {}

def drawKeyboard():
    for r in range(len(keyboard)):
        row_str = keyboard[r]
        row_width = len(row_str) * 34 + (len(row_str) - 1) * 4
        if r == 2:
            row_width += 76
        start_x = (width - row_width) / 2.0
        y = 500 + 46 * r
        letter_start = start_x
        if r == 2:
            letter_start += 38
        for i in range(len(row_str)):
            char = row_str[i]
            key_x = letter_start + i * 38
            if char in key_colors:
                colr = key_colors[char]
            else:
                colr = DARK_GRAY
            fill(colr)
            no_stroke()
            rect(key_x, y, 34, 42, 5)
            fill(255, 255, 255, 230)
            text_size(14)
            text_align(CENTER, CENTER)
            text(char, key_x + 17, y + 21)

def genTile():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char = letters[int(random(0, 26))]
    direction = ["left", "right"]
    falling_tiles.append(Tile(random(0, width), -50, direction[int(random(0, 2))], 0, char))

def mouse_pressed():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char = letters[int(random(0, 26))]
    direction = ["left", "right"]
    falling_tiles.append(Tile(mouse_x, mouse_y, direction[int(random(0, 2))], 0, char))
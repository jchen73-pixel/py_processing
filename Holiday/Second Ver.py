from Tile import *

falling_tiles = []
tile_delay = 0
tile_timer = 0

wordle_words = []
target_word = ""
guesses = []
guess_results = []
current_guess = ""
game_over = False
game_won = False
message = ""
message_timer = 0

# i don't use color() here because i sometimes use alpha and sometimes not
GREEN = (106, 170, 100)
YELLOW = (201, 180, 88)
WORDLE_GRAY = (120, 124, 126)
DARK_GRAY = (58, 58, 60)
LIGHT_GRAY = (211, 214, 218)
WHITE = (255, 255, 255)
BG_COLOR = (18, 18, 19)

def setup():
    global wordle_words, target_word
    size(600, 750)
    text_align(CENTER, CENTER)
    try:
        font = create_font("Helvetica", 48)
        text_font(font)
    except:
        pass
    with open("words.txt", "r") as file:
        content = file.read()
        wordle_words = content.split("\n")
    for i in range(len(wordle_words)):
        wordle_words[i] = wordle_words[i].upper()
    target_word = wordle_words[int(random(0, len(wordle_words)))]

def draw():
    global tile_timer, tile_delay, message_timer
    background(BG_COLOR[0], BG_COLOR[1], BG_COLOR[2])
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
    if message_timer > 0:
        message_timer -= 1
        drawMessage()

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
        fill(colr[0], colr[1], colr[2], 240)
        text(char, charX, 100)
        charX += text_width(char)
    text_align(CENTER, CENTER)

def drawWordleGrid():
    for row in range(6):
        for col in range(5):
            x = 173 + 52 * col
            y = 170 + 52 * row
            if row < len(guesses): # prior guesses
                result = guess_results[row][col]
                if result == "green":
                    colr = GREEN
                elif result == "yellow":
                    colr = YELLOW
                else:
                    colr = WORDLE_GRAY
                fill(colr[0], colr[1], colr[2])
                no_stroke()
                rect(x, y, 46, 46, 5)
                fill(255, 255, 255)
                text_size(26)
                text_align(CENTER, CENTER)
                text(guesses[row][col], x + 23, y + 21)

            elif row == len(guesses): # currently typing
                if col < len(current_guess):
                    stroke(LIGHT_GRAY[0], LIGHT_GRAY[1], LIGHT_GRAY[2])
                    stroke_weight(2)
                    fill(40, 40, 42)
                    rect(x, y, 46, 46, 5)
                    no_stroke()
                    fill(255, 255, 255)
                    text_size(26)
                    text_align(CENTER, CENTER)
                    text(current_guess[col], x + 23, y + 21)
                else:
                    stroke(DARK_GRAY[0], DARK_GRAY[1], DARK_GRAY[2])
                    stroke_weight(2)
                    no_fill()
                    rect(x, y, 46, 46, 5)
                    no_stroke()

            else: # empty future rows
                stroke(DARK_GRAY[0], DARK_GRAY[1], DARK_GRAY[2])
                stroke_weight(2)
                no_fill()
                rect(x, y, 46, 46, 5)
                no_stroke()

keyboard = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
key_colors = {}

def drawKeyboard():
    for r in range(len(keyboard)):
        row_str = keyboard[r]
        row_width = len(row_str) * 34 + (len(row_str) - 1) * 4
        if r == 2:
            row_width += 76 # extra space for enter and backspace
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
            fill(colr[0], colr[1], colr[2])
            no_stroke()
            rect(key_x, y, 34, 42, 5)
            fill(255, 255, 255, 230)
            text_size(14)
            text_align(CENTER, CENTER)
            text(char, key_x + 17, y + 21)

def drawMessage():
    fill(255, 255, 255, 230)
    no_stroke()
    message_width = text_width(message) + 30
    rect(width / 2 - message_width / 2, 145, message_width, 36, 6)
    fill(18, 18, 19)
    text_size(14)
    text_align(CENTER, CENTER)
    text(message, width / 2, 163)

def evaluateGuess(guess, target):
    result = ["gray", "gray", "gray", "gray", "gray"]
    target_chars = list(target)
    for i in range(5):
        if guess[i] == target[i]:
            result[i] = "green"
            target_chars[i] = None
    for i in range(5):
        if result[i] == "green":
            continue
        if guess[i] in target_chars:
            result[i] = "yellow"
            target_chars[target_chars.index(guess[i])] = None
    return result

def updateKeyColors(guess, result):
    priority = {"green": 3, "yellow": 2, "gray": 1}
    for i in range(len(guess)):
        char = guess[i]
        new_color_name = result[i]
        if new_color_name == "green":
            c = GREEN
        elif new_color_name == "yellow":
            c = YELLOW
        else:
            c = WORDLE_GRAY
        # Only upgrade color (green > yellow > gray)
        if char in key_colors:
            old_name = "gray"
            if key_colors[char] == GREEN:
                old_name = "green"
            elif key_colors[char] == YELLOW:
                old_name = "yellow"
            if priority[new_color_name] > priority[old_name]:
                key_colors[char] = c
        else:
            key_colors[char] = c

def key_pressed():
    global current_guess, game_over, game_won
    global message, message_timer, target_word
    if game_over:
        if key == ENTER:
            resetGame()
        return
    k = key
    if k == BACKSPACE:
        if len(current_guess) > 0:
            current_guess = current_guess[:-1]
    elif k == ENTER:
        submitGuess()
    elif k.isalpha() and len(current_guess) < 5:
        current_guess += k.upper()


def submitGuess():
    global current_guess, game_over, game_won
    global message, message_timer
    if len(current_guess) < 5:
        message = "Not enough letters"
        message_timer = 90
        return
    guess = current_guess.upper()
    if guess not in wordle_words:
        message = "Not in word list"
        message_timer = 90
        return
    result = evaluateGuess(guess, target_word)
    guesses.append(guess)
    guess_results.append(result)
    updateKeyColors(guess, result)
    current_guess = ""
    if guess == target_word:
        game_won = True
        game_over = True
        message = "Genius!"
        message_timer = 500
    elif len(guesses) >= 6:
        game_over = True
        message = "The word was: " + target_word
        message_timer = 500

def resetGame():
    global target_word, guesses, guess_results, current_guess
    global game_over, game_won, message, message_timer, key_colors
    target_word = wordle_words[int(random(0, len(wordle_words)))]
    guesses = []
    guess_results = []
    current_guess = ""
    game_over = False
    game_won = False
    message = ""
    message_timer = 0
    key_colors.clear()

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
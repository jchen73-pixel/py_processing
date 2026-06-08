# Skill 1 Drawing Functions - line 164
# Skill 2 Controlling Color State - line 304
# Skill 3 Using Colors - line 301
# Skill 4 Working with setup and draw - line 63
# Skill 5 Events - line 371
# Skill 9 Moving shapes - waived
# Skill 10 Creating and using classes - line 86
# Skill 11 Using transformations - line 141
# Skill 12 Using pixels - line 217

from math import hypot

WIDTH, HEIGHT = 800, 1000 # window size in pixels
BALL_RADIUS = 14 # radius of the player orb
GRAVITY = 0.42 # downward speed added every frame
JUMP_VELOCITY = -8.5 # upward speed on a tap (negative is up)
SPACING = 620 # vertical distance between obstacles

BAR_WIDTH = 460
BAR_HEIGHT = 38
BAR_SPEED = 2.7 # how fast the bar slides sideways
BAR_LEFT_LIMIT = 225 # leftmost center the bar reaches
BAR_RIGHT_LIMIT = 575 # rightmost center the bar reaches

RING_DIAMETER = 260
RING_STROKE_WEIGHT = 18

CROSS_ARM_INNER = 90 # arm starts this far from the center
CROSS_ARM_OUTER = 175 # arm ends this far from the center
CROSS_ARM_WIDTH = 26

DOUBLECROSS_OFFSET = 130 # how far each cross sits from center
DC_ARM_INNER = 30
DC_ARM_OUTER = 185
DC_ARM_WIDTH = 24

SQUARE_HALF_SIDE = 125 # half the square's edge length
SQUARE_STROKE_WEIGHT = 16

CHANGER_RADIUS = 20 # size of the color pickup

CAMERA_OFFSET = 640 # how far below the view top the orb stays
SPAWN_AHEAD = 300 # spawn obstacles this far above the view
DESPAWN_MARGIN = 260 # delete obstacles this far below the view
DEATH_MARGIN = 90 # orb dies once this far below the view
INITIAL_SPAWN_Y = -540 # world-y of the first obstacle

state = "start" # "start", "play", or "over"
score = 0
high_score = 0

player_x = WIDTH / 2
player_y = 0.0
player_vy = 0.0 # vertical velocity, positive is down
player_color = 0 # index into GAME_COLORS

camera_y = 0.0 # world-y of the top of the view
spawn_y = 0.0 # world-y where the next obstacle spawns

obstacles = []
changers = []

# Skill 4 Working with setup and draw
def setup():
    global CYAN, YELLOW, PURPLE, PINK, GAME_COLORS
    size(WIDTH, HEIGHT)
    color_mode(RGB, 255)
    CYAN = color(0, 231, 231)
    YELLOW = color(255, 210, 0)
    PURPLE = color(170, 70, 235)
    PINK = color(255, 75, 160)
    GAME_COLORS = [CYAN, YELLOW, PURPLE, PINK] # the four colors
    text_align(CENTER, CENTER)
    reset_game()

def draw():
    if state == "start":
        draw_start()
    elif state == "play":
        update_play()
        draw_play()
    else:
        draw_over()

# Skill 10 Creating and using classes
class ColorChanger:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = CHANGER_RADIUS
        self.used = False # True once collected
        self.color_index = int(random(len(GAME_COLORS))) # color the orb will become

    def try_trigger(self, ball_x, ball_y):
        global player_color, score
        if self.used:
            return
        if hypot(ball_x - self.x, ball_y - self.y) < self.radius + BALL_RADIUS: # orb overlaps pickup
            self.used = True
            score += 1
            player_color = self.color_index # recolor the orb

    def display(self):
        if self.used: # collected pickups vanish
            return
        no_stroke()
        fill(GAME_COLORS[self.color_index])
        square(self.x - self.radius, self.y - self.radius, self.radius * 2)

class Obstacle:
    KINDS = ["ring", "cross", "doublecross", "bar", "square"]
    SPIN_SPEED = {
        "ring": 0.020,
        "cross": 0.024,
        "doublecross": 0.03,
        "bar": 0.0,
        "square": 0.02,
    }

    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.kind = kind
        self.rotation = random(TWO_PI) # random starting spin angle
        self.center_x = WIDTH / 2 # bar's current x (only the bar moves)
        self.direction = 1 # bar slide direction: 1 right, -1 left

    def update(self, difficulty):
        self.rotation += self.SPIN_SPEED[self.kind] * difficulty # spin faster as score climbs
        if self.kind == "bar":
            self.center_x += self.direction * BAR_SPEED * difficulty
            if self.center_x < BAR_LEFT_LIMIT: # hit left edge, turn around
                self.center_x = BAR_LEFT_LIMIT
                self.direction = 1
            elif self.center_x > BAR_RIGHT_LIMIT: # hit right edge, turn around
                self.center_x = BAR_RIGHT_LIMIT
                self.direction = -1

    def display(self):
        # Skill 11 Using transformations
        push_matrix()
        if self.kind == "bar":
            translate(self.center_x, self.y)
            self.draw_bar()
        else:
            translate(self.x, self.y)
            if self.kind == "ring":
                self.draw_ring()
            elif self.kind == "cross":
                self.draw_cross()
            elif self.kind == "doublecross":
                self.draw_doublecross()
            elif self.kind == "square":
                self.draw_square()
        pop_matrix()

    def draw_ring(self):
        rotate(self.rotation)
        no_fill()
        stroke_weight(RING_STROKE_WEIGHT)
        for segment_index in range(len(GAME_COLORS)): # one quarter-arc per color
            stroke(GAME_COLORS[segment_index])
            # Skill 1 Drawing Functions
            arc(0, 0, RING_DIAMETER, RING_DIAMETER, segment_index * HALF_PI, (segment_index + 1) * HALF_PI)

    def draw_cross(self):
        rotate(self.rotation)
        no_stroke()
        for arm_index in range(len(GAME_COLORS)): # four arms, 90 degrees apart
            push_matrix()
            rotate(arm_index * HALF_PI)
            fill(GAME_COLORS[arm_index])
            rect(CROSS_ARM_INNER, -CROSS_ARM_WIDTH / 2, CROSS_ARM_OUTER - CROSS_ARM_INNER, CROSS_ARM_WIDTH)
            pop_matrix()

    def draw_doublecross(self):
        color_sequence = [0, 1, 2, 3]
        mirror_colors = [color_sequence[2], color_sequence[1], color_sequence[0], color_sequence[3]] # reversed order
        self.draw_one_cross(-DOUBLECROSS_OFFSET, -self.rotation, color_sequence) # left cross, spins one way
        self.draw_one_cross(DOUBLECROSS_OFFSET, self.rotation, mirror_colors) # right cross, spins the other

    def draw_one_cross(self, x_offset, rotation, color_map):
        push_matrix()
        translate(x_offset, 0) # shift this cross left or right
        rotate(rotation)
        no_stroke()
        for arm_index in range(len(GAME_COLORS)):
            push_matrix()
            rotate(arm_index * HALF_PI)
            fill(GAME_COLORS[color_map[arm_index]])
            rect(DC_ARM_INNER, -DC_ARM_WIDTH / 2, DC_ARM_OUTER - DC_ARM_INNER, DC_ARM_WIDTH)
            pop_matrix()
        pop_matrix()

    def draw_bar(self):
        segment_width = BAR_WIDTH / len(GAME_COLORS) # width of each colored segment
        no_stroke()
        for segment_index in range(len(GAME_COLORS)):
            fill(GAME_COLORS[segment_index])
            rect(-BAR_WIDTH / 2 + segment_index * segment_width, -BAR_HEIGHT / 2, segment_width, BAR_HEIGHT)

    def draw_square(self):
        rotate(self.rotation)
        half_side = SQUARE_HALF_SIDE
        stroke_weight(SQUARE_STROKE_WEIGHT)
        stroke(PINK)
        line(-half_side, -half_side, half_side, -half_side) # top edge
        stroke(CYAN)
        line(half_side, -half_side, half_side, half_side) # right edge
        stroke(YELLOW)
        line(half_side, half_side, -half_side, half_side) # bottom edge
        stroke(PURPLE)
        line(-half_side, half_side, -half_side, -half_side) # left edge

def orb_hits_obstacle():
    # Skill 12 Using pixels
    load_np_pixels()
    pixels_copy = np_pixels.copy() # snapshot of the screen (obstacles only)
    pixel_h, pixel_w = pixels_copy.shape[0], pixels_copy.shape[1]
    density = pixel_h // height # np_pixels is bigger than the window on high-DPI displays
    center_x = int(player_x * density)
    center_y = int((player_y - camera_y) * density) # orb's on-screen position
    radius = BALL_RADIUS * density
    orb_color = GAME_COLORS[player_color]
    orb_r = int(red(orb_color)) # pull the orb's r/g/b back out of the color
    orb_g = int(green(orb_color))
    orb_b = int(blue(orb_color))
    for y in range(center_y - radius, center_y + radius + 1):
        if y < 0 or y >= pixel_h: # skip rows off the screen
            continue
        for x in range(center_x - radius, center_x + radius + 1):
            if x < 0 or x >= pixel_w: # skip columns off the screen
                continue
            if (x - center_x) ** 2 + (y - center_y) ** 2 > radius ** 2: # only the round orb area
                continue
            r = int(pixels_copy[y, x, 1]) # np_pixels is ARGB, so 1,2,3 are r,g,b
            g = int(pixels_copy[y, x, 2])
            b = int(pixels_copy[y, x, 3])
            if (r, g, b) != (0, 0, 0) and (r, g, b) != (orb_r, orb_g, orb_b): # not background, not orb color
                return True
    return False

def make_obstacle(y):
    kind = Obstacle.KINDS[int(random(len(Obstacle.KINDS)))] # pick a random shape
    obstacles.append(Obstacle(WIDTH / 2, y, kind))

def fill_world():
    global spawn_y
    while spawn_y > camera_y - SPAWN_AHEAD: # keep filling until far enough above the view
        make_obstacle(spawn_y)
        changers.append(ColorChanger(WIDTH / 2, spawn_y + SPACING / 2)) # pickup halfway below
        spawn_y -= SPACING # next obstacle goes higher up

def reset_game():
    global player_x, player_y, player_vy, player_color, camera_y, score, spawn_y, obstacles, changers
    player_x = WIDTH / 2
    player_y = 0.0
    player_vy = 0.0
    player_color = int(random(len(GAME_COLORS))) # random starting color
    camera_y = player_y - CAMERA_OFFSET
    score = 0
    obstacles = []
    changers = []
    spawn_y = INITIAL_SPAWN_Y
    fill_world()

def start_game():
    global state
    reset_game()
    state = "play"

def die():
    global state, high_score
    if state != "play":
        return
    state = "over"
    high_score = max(high_score, score) # keep the best score

def do_jump():
    global player_vy
    player_vy = JUMP_VELOCITY # fixed upward push

def draw_player():
    no_stroke()
    fill(GAME_COLORS[player_color])
    circle(player_x, player_y, 2 * BALL_RADIUS) # orb is just a colored circle now

def draw_hud():
    fill(255)
    text_size(26)
    text_align(LEFT, TOP)
    text("Score: " + str(score), 18, 16) # current score, top-left
    text("High: " + str(high_score), 18, 48) # best score below it

def draw_title(center_x, center_y):
    label = "COLOR JUMP"
    text_size(76)
    total_text_width = 0
    for character in label:
        total_text_width += text_width(character) # measure so we can center it
    current_x = center_x - total_text_width / 2
    text_align(LEFT, CENTER)
    # Skill 3 Using Colors
    color_mode(HSB, 360, 100, 100) # switch to hue-based color
    for char_index, character in enumerate(label):
        # Skill 2 Controlling Color State
        fill(char_index * 360 / len(label), 85, 100) # each letter a different hue
        text(character, current_x, center_y)
        current_x += text_width(character) # advance past this letter
    color_mode(RGB, 255) # back to normal color mode

def draw_start():
    background(0)
    draw_title(WIDTH / 2, HEIGHT / 2 - 50)
    text_align(CENTER, CENTER)
    fill(255)
    text_size(30)
    text("Press SPACE to Start", WIDTH / 2, HEIGHT / 2 + 40)

def draw_over():
    background(0)
    text_align(CENTER, CENTER)
    fill(255, 80, 80)
    text_size(74)
    text("GAME OVER", WIDTH / 2, 330)
    fill(255)
    text_size(36)
    text("Score: " + str(score), WIDTH / 2, 440)
    text("High Score: " + str(high_score), WIDTH / 2, 490)
    text_size(26)
    text("Press R to Restart", WIDTH / 2, 580)

def keep_visible(items, despawn_y):
    kept = []
    for item in items:
        if item.y < despawn_y: # drop anything past the bottom margin
            kept.append(item)
    return kept

def update_play():
    global player_vy, player_y, camera_y, obstacles, changers
    player_vy += GRAVITY # gravity speeds up the fall
    player_y += player_vy
    camera_y = min(camera_y, player_y - CAMERA_OFFSET) # view only ever rises with the orb
    fill_world() # top up obstacles above the view
    despawn_y = camera_y + HEIGHT + DESPAWN_MARGIN
    obstacles = keep_visible(obstacles, despawn_y)
    changers = keep_visible(changers, despawn_y)
    for obstacle in obstacles:
        obstacle.update(1 + score * 0.07) # speed ramps up with score
    for changer in changers:
        changer.try_trigger(player_x, player_y) # collect any touched pickup
    if player_y - camera_y > HEIGHT + DEATH_MARGIN: # fell off the bottom
        die()

def draw_play():
    background(0)
    push_matrix()
    translate(0, -camera_y) # shift world so the camera follows the orb
    for obstacle in obstacles:
        obstacle.display()
    pop_matrix()
    if orb_hits_obstacle(): # check pixels before drawing orb/pickups
        die()
    push_matrix()
    translate(0, -camera_y)
    for changer in changers:
        changer.display()
    draw_player()
    pop_matrix()
    draw_hud() # HUD drawn last, unshifted by the camera

# Skill 5 Events
def key_pressed():
    if state == "start" and key == ' ': # SPACE begins the game
        start_game()
    elif state == "play" and key == ' ': # SPACE jumps while playing
        do_jump()
    elif state == "over" and (key == 'r' or key == 'R'): # R restarts after dying
        start_game()

def mouse_pressed():
    if state == "play":
        do_jump() # click also jumps
    else:
        start_game() # click starts/restarts
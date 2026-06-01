import numpy as np
from math import sin, cos, hypot, atan2

WIDTH, HEIGHT = 800, 1000
BALL_RADIUS = 14
GRAVITY = 0.42
JUMP_VELOCITY = -8.5
SPACING = 620

CYAN, YELLOW, PURPLE, PINK = (0, 231, 231), (255, 210, 0), (170, 70, 235), (255, 75, 160)
GAME_COLORS = [CYAN, YELLOW, PURPLE, PINK]

BAR_WIDTH, BAR_HEIGHT, BAR_SPEED, BAR_LOW, BAR_HIGH = 460, 38, 2.7, 250, 550
RING_SAMPLE_COUNT = 24
RING_SAMPLE_RADIUS = BALL_RADIUS - 2
SAME_COLOR_THRESHOLD_SQ = 5000

state = "start"
score = high_score = 0
difficulty_multiplier = 1.0
player_x, player_y, player_vy, player_color = WIDTH / 2, 0.0, 0.0, 0
camera_y = spawn_y = 0.0
obstacles, changers = [], []
ball_img = None


def random_other_color(c):
    n = int(random(4))
    while n == c:
        n = int(random(4))
    return n

# Skill 12 pixels
def point_segment_distance(px, py, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0 and dy == 0:
        return hypot(px - x1, py - y1)
    t = max(0, min(1, ((px - x1) * dx + (py - y1) * dy) / float(dx * dx + dy * dy)))
    cx = x1 + t * dx
    cy = y1 + t * dy
    return hypot(px - cx, py - cy)

def orb_hits_obstacle():
    px, py = player_x, player_y
    for o in obstacles:
        if o.kind == "ring":
            d = hypot(px - o.x, py - o.y)
            if 121 - BALL_RADIUS <= d <= 139 + BALL_RADIUS:
                ang = (atan2(py - o.y, px - o.x) - o.rot) % TWO_PI
                col = int(ang / HALF_PI) % 4
                if col != player_color:
                    return True

        elif o.kind == "wheel":
            d = hypot(px - o.x, py - o.y)
            if 75 - BALL_RADIUS <= d <= 130 + BALL_RADIUS:
                ang = (atan2(py - o.y, px - o.x) - o.rot) % TWO_PI
                col = int(ang / HALF_PI) % 4
                if col != player_color:
                    return True

        elif o.kind == "bar":
            left = o.center_x - BAR_WIDTH / 2
            top = o.y - BAR_HEIGHT / 2
            if left - BALL_RADIUS <= px <= left + BAR_WIDTH + BALL_RADIUS and top - BALL_RADIUS <= py <= top + BAR_HEIGHT + BALL_RADIUS:
                seg = int((px - left) / (BAR_WIDTH / 4))
                seg = max(0, min(3, seg))
                if seg != player_color:
                    return True

        elif o.kind == "square":
            a = -o.rot
            rx = (px - o.x) * cos(a) - (py - o.y) * sin(a)
            ry = (px - o.x) * sin(a) + (py - o.y) * cos(a)
            sides = [
                ((-125, -125), (125, -125), 3),
                ((125, -125), (125, 125), 0),
                ((125, 125), (-125, 125), 1),
                ((-125, 125), (-125, -125), 2),
            ]
            for p1, p2, col in sides:
                if point_segment_distance(rx, ry, p1[0], p1[1], p2[0], p2[1]) <= BALL_RADIUS + 8:
                    if col != player_color:
                        return True

        elif o.kind == "cross":
            a = -o.rot
            rx = (px - o.x) * cos(a) - (py - o.y) * sin(a)
            ry = (px - o.x) * sin(a) + (py - o.y) * cos(a)
            for i in range(4):
                ang = -i * HALF_PI
                lx = rx * cos(ang) - ry * sin(ang)
                ly = rx * sin(ang) + ry * cos(ang)
                if 90 - BALL_RADIUS <= lx <= 175 + BALL_RADIUS and abs(ly) <= 13 + BALL_RADIUS:
                    if i != player_color:
                        return True

        elif o.kind == "doublecross":
            cols = [0, 1, 2, 3]
            mirror = [2, 1, 0, 3]
            for cx, rot, cmap in ((o.x - 130, -o.rot, cols), (o.x + 130, o.rot, mirror)):
                a = -rot
                rx = (px - cx) * cos(a) - (py - o.y) * sin(a)
                ry = (px - cx) * sin(a) + (py - o.y) * cos(a)
                for i in range(4):
                    ang = -i * HALF_PI
                    lx = rx * cos(ang) - ry * sin(ang)
                    ly = rx * sin(ang) + ry * cos(ang)
                    if 30 - BALL_RADIUS <= lx <= 185 + BALL_RADIUS and abs(ly) <= 12 + BALL_RADIUS:
                        if cmap[i] != player_color:
                            return True
    return False

# Skill 10 Classes
class ColorChanger:
    def __init__(self, x, y):
        self.x, self.y, self.radius, self.used = x, y, 20, False

    def offset(self):
        angle = frame_count * 0.05 + self.y * 0.01
        return cos(angle) * 20, sin(angle) * 10

    def try_trigger(self, pos_x, pos_y):
        global player_color, score
        if self.used:
            return
        offset_x, offset_y = self.offset()
        if hypot(pos_x - (self.x + offset_x), pos_y - (self.y + offset_y)) < self.radius + BALL_RADIUS:
            self.used = True
            score += 1
            player_color = random_other_color(player_color)

    # Skill 11 Transformations
    def display(self):
        if self.used:
            return
        offset_x, offset_y = self.offset()
        tile_size = self.radius
        push_matrix()
        translate(self.x + offset_x, self.y + offset_y)
        no_stroke()
        fill(*CYAN)
        square(-tile_size, -tile_size, tile_size)
        fill(*YELLOW)
        square(0, -tile_size, tile_size)
        fill(*PURPLE)
        square(-tile_size, 0, tile_size)
        fill(*PINK)
        square(0, 0, tile_size)
        stroke(255)
        stroke_weight(4)
        point(0, 0)
        pop_matrix()

class Obstacle:
    KINDS = ["ring", "cross", "doublecross", "wheel", "bar", "square"]
    SPIN = {"ring": 0.020, "cross": 0.024, "doublecross": 0.030,
            "wheel": 0.020, "bar": 0.0, "square": 0.020}

    def __init__(self, x, y, kind):
        self.x, self.y, self.kind = x, y, kind
        self.rot = random(TWO_PI)
        self.center_x, self.direction = WIDTH / 2, 1

    def update(self, difficulty):
        self.rot += self.SPIN[self.kind] * difficulty
        if self.kind == "bar":
            # Skill 9 Moving shapes
            self.center_x += self.direction * BAR_SPEED * difficulty
            if self.center_x < BAR_LOW:
                self.center_x, self.direction = BAR_LOW, 1
            elif self.center_x > BAR_HIGH:
                self.center_x, self.direction = BAR_HIGH, -1

    def display(self):
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
            elif self.kind == "wheel":
                self.draw_wheel()
            elif self.kind == "square":
                self.draw_square()
        pop_matrix()

    def draw_ring(self):
        rotate(self.rot)
        no_fill()
        stroke_weight(18)
        for i in range(4):
            stroke(*GAME_COLORS[i])
            arc(0, 0, 260, 260, i * HALF_PI, (i + 1) * HALF_PI)

    def _one_cross(self, dx, rot, cols):
        push_matrix()
        translate(dx, 0)
        rotate(rot)
        no_stroke()
        arm_inner, arm_length, arm_width = 30, 185, 24
        for i in range(4):
            push_matrix()
            rotate(i * HALF_PI)
            fill(*GAME_COLORS[cols[i]])
            rect(arm_inner, -arm_width / 2, arm_length - arm_inner, arm_width)
            pop_matrix()
        pop_matrix()

    def draw_cross(self):
        rotate(self.rot)
        no_stroke()
        arm_inner, arm_length, arm_width = 90, 175, 26
        for i in range(4):
            push_matrix()
            rotate(i * HALF_PI)
            fill(*GAME_COLORS[i])
            rect(arm_inner, -arm_width / 2, arm_length - arm_inner, arm_width)
            pop_matrix()

    def draw_doublecross(self):
        cols = [0, 1, 2, 3]
        mirror = [cols[2], cols[1], cols[0], cols[3]]
        self._one_cross(-130, -self.rot, cols)
        self._one_cross(130, self.rot, mirror)

    def draw_wheel(self):
        rotate(self.rot)
        no_stroke()
        for i in range(4):
            fill(*GAME_COLORS[i])
            arc(0, 0, 260, 260, i * HALF_PI, (i + 1) * HALF_PI, PIE)
        fill(0)
        circle(0, 0, 150)

    def draw_bar(self):
        segment_width = BAR_WIDTH / 4
        no_stroke()
        for i in range(4):
            fill(*GAME_COLORS[i])
            rect(-BAR_WIDTH / 2 + i * segment_width, -BAR_HEIGHT / 2, segment_width, BAR_HEIGHT)

    def draw_square(self):
        rotate(self.rot)
        half_length = 125
        stroke_weight(16)
        stroke(*PINK)
        line(-half_length, -half_length, half_length, -half_length)
        stroke(*CYAN)
        line(half_length, -half_length, half_length, half_length)
        stroke(*YELLOW)
        line(half_length, half_length, -half_length, half_length)
        stroke(*PURPLE)
        line(-half_length, half_length, -half_length, -half_length)

def make_obstacle(y):
    kind = Obstacle.KINDS[int(random(len(Obstacle.KINDS)))]
    obstacles.append(Obstacle(WIDTH / 2, y, kind))

def reset_game():
    global player_x, player_y, player_vy, player_color, camera_y
    global score, difficulty_multiplier, spawn_y, obstacles, changers
    player_x, player_y, player_vy = WIDTH / 2, 0.0, 0.0
    player_color = int(random(4))
    camera_y = player_y - 640
    score, difficulty_multiplier = 0, 1.0
    obstacles, changers = [], []
    spawn_y = -540
    fill_world()

def fill_world():
    global spawn_y
    while spawn_y > camera_y - 300:
        make_obstacle(spawn_y)
        changers.append(ColorChanger(WIDTH / 2, spawn_y + SPACING / 2))
        spawn_y -= SPACING

def start_game():
    global state
    reset_game()
    state = "play"

def die():
    global state, high_score
    if state != "play":
        return
    state = "over"
    high_score = max(high_score, score)

def do_jump():
    global player_vy
    player_vy = JUMP_VELOCITY

def make_ball_image():
    diameter = 2 * BALL_RADIUS
    img = create_image(diameter, diameter, ARGB)
    img.load_np_pixels()
    y_indices, x_indices = np.mgrid[0:diameter, 0:diameter]
    inside = (x_indices - BALL_RADIUS) ** 2 + (y_indices - BALL_RADIUS) ** 2 <= BALL_RADIUS ** 2
    img.np_pixels[:, :, 0] = np.where(inside, 255, 0).astype(np.uint8)
    img.np_pixels[:, :, 1:] = 255
    img.update_np_pixels()
    return img


# Skill 8 using images
def draw_player():
    tint(*GAME_COLORS[player_color])
    diameter = 2 * BALL_RADIUS
    image(ball_img, player_x - BALL_RADIUS, player_y - BALL_RADIUS, diameter, diameter)
    no_tint()


def draw_hud():
    fill(255)
    text_size(26)
    text_align(LEFT, TOP)
    text("Score: " + str(score), 18, 16)
    text("High: " + str(high_score), 18, 48)
    no_stroke()
    fill(*GAME_COLORS[player_color])
    ellipse(WIDTH - 42, 36, 34, 34)


def draw_title(center_x, center_y):
    label = "COLOR JUMP"
    text_size(76)
    total = 0
    for ch in label:
        total += text_width(ch)
    x = center_x - total / 2
    text_align(LEFT, CENTER)
    color_mode(HSB, 360, 100, 100) # Skill 3 using colors
    for i, ch in enumerate(label):
        fill(i * 360 / len(label), 85, 100)
        text(ch, x, center_y)
        x += text_width(ch)
    color_mode(RGB, 255)

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

def update_play():
    global player_vy, player_y, camera_y, difficulty_multiplier, obstacles, changers
    player_vy += GRAVITY
    player_y += player_vy
    if player_y - 640 < camera_y:
        camera_y = player_y - 640
    fill_world()
    bottom = camera_y + HEIGHT + 260
    new_obstacles = []
    for o in obstacles:
        if o.y < bottom:
            new_obstacles.append(o)
    obstacles = new_obstacles
    new_changers = []
    for c in changers:
        if c.y < bottom:
            new_changers.append(c)
    changers = new_changers
    for o in obstacles:
        o.update(difficulty_multiplier)
    difficulty_multiplier = 1.0 + min(score // 10, 8) * 0.07
    for c in changers:
        c.try_trigger(player_x, player_y)
    if player_y - camera_y > HEIGHT + 90:
        die()


def draw_play():
    background(0)
    push_matrix()
    translate(0, -camera_y)
    for o in obstacles:
        o.display()
    pop_matrix()
    if orb_hits_obstacle():
        die()
    push_matrix()
    translate(0, -camera_y)
    for c in changers:
        c.display()
    draw_player()
    pop_matrix()
    draw_hud()


# Skill 4 working with setup and draw
def setup():
    global ball_img
    size(WIDTH, HEIGHT)
    color_mode(RGB, 255)
    text_align(CENTER, CENTER)
    ball_img = make_ball_image()
    reset_game()


def draw():
    if state == "start":
        draw_start()
    elif state == "play":
        update_play()
        draw_play()
    else:
        draw_over()

# Skill 5 mouse events
def key_pressed():
    if state == "start" and key == ' ':
        start_game()
    elif state == "play" and key == ' ':
        do_jump()
    elif state == "over" and (key == 'r' or key == 'R'):
        start_game()


def mouse_pressed():
    if state == "play":
        do_jump()
    else:
        start_game()

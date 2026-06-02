import numpy as np
from math import sin, cos, hypot, atan2

WIDTH, HEIGHT = 800, 1000
BALL_RADIUS = 14
GRAVITY = 0.42
JUMP_VELOCITY = -8.5
SPACING = 620 # between obstacles

CYAN   = (0, 231, 231)
YELLOW = (255, 210, 0)
PURPLE = (170, 70, 235)
PINK   = (255, 75, 160)
GAME_COLORS = [CYAN, YELLOW, PURPLE, PINK]

BAR_WIDTH = 460
BAR_HEIGHT = 38
BAR_SPEED = 2.7
BAR_LEFT_LIMIT = 250 # leftmost center-x the bar can reach
BAR_RIGHT_LIMIT = 550 # rightmost center-x the bar can reach

RING_SAMPLE_COUNT = 24
RING_SAMPLE_RADIUS = BALL_RADIUS - 2
SAME_COLOR_THRESHOLD_SQ = 5000

state = "start"
score = 0
high_score = 0
difficulty_multiplier = 1.0

player_x = WIDTH / 2
player_y = 0.0
player_vy = 0.0 # vertical velocity. positive is down
player_color = 0 # index for GAME_COLORS

camera_y = 0.0 # world-y of the top of the visible area
spawn_y  = 0.0 # world-y where the next obstacle will be placed

obstacles = []
changers  = []
ball_img  = None

# return random color index that is different from current color
def random_other_color(current_color):
    new_color = int(random(4))
    while new_color == current_color:
        new_color = int(random(4))
    return new_color

class ColorChanger:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.used = False # True if collected
        
    # check touched
    def try_trigger(self, ball_x, ball_y):
        global player_color, score
        if self.used:
            return
        if hypot(ball_x - self.x, ball_y - self.y) < self.radius + BALL_RADIUS:
            self.used = True
            score += 1
            player_color = random_other_color(player_color)

    # draw 2x2 color grid with center white dot
    def display(self):
        if self.used:
            return
        tile_size = self.radius
        push_matrix()
        translate(self.x, self.y)
        no_stroke()
        red, green, blue = CYAN
        fill(red, green, blue)
        square(-tile_size, -tile_size, tile_size)
        red, green, blue = YELLOW
        fill(red, green, blue)
        square(0, -tile_size, tile_size)
        red, green, blue = PURPLE
        fill(red, green, blue)
        square(-tile_size, 0, tile_size)
        red, green, blue = PINK
        fill(red, green, blue)
        square(0, 0, tile_size)
        stroke(255)
        stroke_weight(4)
        point(0, 0)
        pop_matrix()

# class to hold all obstacle types
class Obstacle:
    KINDS = ["ring", "cross", "doublecross", "bar", "square"]

    # how fast each obstacle type spins
    SPIN_SPEED = {
        "ring": 0.020,
        "cross": 0.024,
        "doublecross": 0.030,
        "bar": 0.0,
        "square": 0.020,
    }

    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.kind = kind
        self.rotation = random(TWO_PI) # random angle at start
        self.center_x = WIDTH / 2 # bar's current horizontal position
        self.direction = 1 # bar slide direction: +1 right, -1 left

    def update(self, difficulty):
        # increment rotation and bar movement
        self.rotation += self.SPIN_SPEED[self.kind] * difficulty
        if self.kind == "bar":
            # slide left right and reverse directions
            self.center_x += self.direction * BAR_SPEED * difficulty
            if self.center_x < BAR_LEFT_LIMIT:
                self.center_x  = BAR_LEFT_LIMIT
                self.direction = 1
            elif self.center_x > BAR_RIGHT_LIMIT:
                self.center_x  = BAR_RIGHT_LIMIT
                self.direction = -1

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
        rotate(self.rotation)
        no_fill()
        stroke_weight(18)
        for segment_index in range(4):
            red, green, blue = GAME_COLORS[segment_index]
            stroke(red, green, blue)
            arc(0, 0, 260, 260, segment_index * HALF_PI, (segment_index + 1) * HALF_PI) # quarter circle arcs of different color

    def draw_cross(self):
        rotate(self.rotation)
        no_stroke()
        arm_inner_radius = 90
        arm_outer_radius = 175
        arm_width        = 26
        for arm_index in range(4):
            push_matrix()
            rotate(arm_index * HALF_PI)
            red, green, blue = GAME_COLORS[arm_index]
            fill(red, green, blue)
            rect(arm_inner_radius, -arm_width / 2, arm_outer_radius - arm_inner_radius, arm_width)
            pop_matrix()

    def draw_doublecross(self):
        color_sequence  = [0, 1, 2, 3]
        mirrored_colors = [color_sequence[2], color_sequence[1], color_sequence[0], color_sequence[3]]
        self.draw_one_cross(-130, -self.rotation, color_sequence)
        self.draw_one_cross( 130,  self.rotation, mirrored_colors)
        
    def draw_one_cross(self, x_offset, rotation, color_map):
        # used by doublecross
        push_matrix()
        translate(x_offset, 0)
        rotate(rotation)
        no_stroke()
        arm_inner_radius = 30
        arm_outer_radius = 185
        arm_width = 24
        for arm_index in range(4):
            push_matrix()
            rotate(arm_index * HALF_PI)
            red, green, blue = GAME_COLORS[color_map[arm_index]]
            fill(red, green, blue)
            rect(arm_inner_radius, -arm_width / 2, arm_outer_radius - arm_inner_radius, arm_width)
            pop_matrix()
        pop_matrix()

    def draw_bar(self):
        segment_width = BAR_WIDTH / 4
        no_stroke()
        for segment_index in range(4):
            red, green, blue = GAME_COLORS[segment_index]
            fill(red, green, blue)
            rect(-BAR_WIDTH / 2 + segment_index * segment_width, -BAR_HEIGHT / 2, segment_width, BAR_HEIGHT)

    def draw_square(self):
        rotate(self.rotation)
        half_side = 125
        stroke_weight(16)
        red, green, blue = PINK
        stroke(red, green, blue)
        line(-half_side, -half_side, half_side, -half_side) # top
        red, green, blue = CYAN
        stroke(red, green, blue)
        line(half_side, -half_side, half_side, half_side) # right
        red, green, blue = YELLOW
        stroke(red, green, blue)
        line(half_side, half_side, -half_side, half_side) # bottom
        red, green, blue = PURPLE
        stroke(red, green, blue)
        line(-half_side, half_side, -half_side, -half_side) # left

# return the shortest distance from a point to a line segment
def point_segment_distance(point_x, point_y, seg_x1, seg_y1, seg_x2, seg_y2):
    delta_x = seg_x2 - seg_x1
    delta_y = seg_y2 - seg_y1
    if delta_x == 0 and delta_y == 0: # horizontal or vertical line
        return hypot(point_x - seg_x1, point_y - seg_y1)
    # Project point onto the segment and clamp to [0, 1] so we stay on it
    projection = max(0, min(1, ((point_x - seg_x1) * delta_x + (point_y - seg_y1) * delta_y)
                               / float(delta_x * delta_x + delta_y * delta_y)))
    nearest_x = seg_x1 + projection * delta_x
    nearest_y = seg_y1 + projection * delta_y
    return hypot(point_x - nearest_x, point_y - nearest_y)

# return true if touching different color
def orb_hits_obstacle():
    ball_x = player_x
    ball_y = player_y

    for obstacle in obstacles:
        if obstacle.kind == "ring":
            distance = hypot(ball_x - obstacle.x, ball_y - obstacle.y)
            if 121 - BALL_RADIUS <= distance <= 139 + BALL_RADIUS:
                angle = (atan2(ball_y - obstacle.y, ball_x - obstacle.x) - obstacle.rotation) % TWO_PI
                color_index = int(angle / HALF_PI) % 4
                if color_index != player_color:
                    return True

        elif obstacle.kind == "bar":
            bar_left = obstacle.center_x - BAR_WIDTH / 2
            bar_top = obstacle.y - BAR_HEIGHT / 2
            in_x_range = bar_left - BALL_RADIUS <= ball_x <= bar_left + BAR_WIDTH  + BALL_RADIUS
            in_y_range = bar_top  - BALL_RADIUS <= ball_y <= bar_top  + BAR_HEIGHT + BALL_RADIUS
            if in_x_range and in_y_range:
                segment_index = int((ball_x - bar_left) / (BAR_WIDTH / 4))
                segment_index = max(0, min(3, segment_index))
                if segment_index != player_color:
                    return True
                
        elif obstacle.kind == "square":
            # rotate ball into square plane
            neg_rotation = -obstacle.rotation
            local_x = (ball_x - obstacle.x) * cos(neg_rotation) - (ball_y - obstacle.y) * sin(neg_rotation)
            local_y = (ball_x - obstacle.x) * sin(neg_rotation) + (ball_y - obstacle.y) * cos(neg_rotation)
            square_sides = [
                ((-125, -125), ( 125, -125), 3),   # top    → pink
                (( 125, -125), ( 125,  125), 0),   # right  → cyan
                (( 125,  125), (-125,  125), 1),   # bottom → yellow
                ((-125,  125), (-125, -125), 2),   # left   → purple
            ]
            for side_start, side_end, side_color_index in square_sides:
                distance = point_segment_distance(local_x, local_y,
                                                  side_start[0], side_start[1],
                                                  side_end[0],   side_end[1])
                if distance <= BALL_RADIUS + 8:
                    if side_color_index != player_color:
                        return True

        elif obstacle.kind == "cross":
            # Rotate into the cross's local frame, then test each arm separately
            neg_rotation = -obstacle.rotation
            local_x = (ball_x - obstacle.x) * cos(neg_rotation) - (ball_y - obstacle.y) * sin(neg_rotation)
            local_y = (ball_x - obstacle.x) * sin(neg_rotation) + (ball_y - obstacle.y) * cos(neg_rotation)
            for arm_index in range(4):
                arm_angle   = -arm_index * HALF_PI
                arm_local_x = local_x * cos(arm_angle) - local_y * sin(arm_angle)
                arm_local_y = local_x * sin(arm_angle) + local_y * cos(arm_angle)
                if 90 - BALL_RADIUS <= arm_local_x <= 175 + BALL_RADIUS and abs(arm_local_y) <= 13 + BALL_RADIUS:
                    if arm_index != player_color:
                        return True

        elif obstacle.kind == "doublecross":
            color_sequence  = [0, 1, 2, 3]
            mirrored_colors = [2, 1, 0, 3]
            # The doublecross is two crosses side by side; check each one
            cross_configs = (
                (obstacle.x - 130, -obstacle.rotation, color_sequence),
                (obstacle.x + 130,  obstacle.rotation, mirrored_colors),
            )
            for cross_center_x, cross_rotation, color_map in cross_configs:
                neg_rotation = -cross_rotation
                local_x = (ball_x - cross_center_x) * cos(neg_rotation) - (ball_y - obstacle.y) * sin(neg_rotation)
                local_y = (ball_x - cross_center_x) * sin(neg_rotation) + (ball_y - obstacle.y) * cos(neg_rotation)
                for arm_index in range(4):
                    arm_angle   = -arm_index * HALF_PI
                    arm_local_x = local_x * cos(arm_angle) - local_y * sin(arm_angle)
                    arm_local_y = local_x * sin(arm_angle) + local_y * cos(arm_angle)
                    if 30 - BALL_RADIUS <= arm_local_x <= 185 + BALL_RADIUS and abs(arm_local_y) <= 12 + BALL_RADIUS:
                        if color_map[arm_index] != player_color:
                            return True

    return False

def make_obstacle(y):
    kind = Obstacle.KINDS[int(random(len(Obstacle.KINDS)))]
    obstacles.append(Obstacle(WIDTH / 2, y, kind))


def fill_world():
    # spawns obstacles on screen
    global spawn_y
    while spawn_y > camera_y - 300:
        make_obstacle(spawn_y)
        changers.append(ColorChanger(WIDTH / 2, spawn_y + SPACING / 2))
        spawn_y -= SPACING

def reset_game():
    global player_x, player_y, player_vy, player_color, camera_y
    global score, difficulty_multiplier, spawn_y, obstacles, changers
    player_x = WIDTH / 2
    player_y = 0.0
    player_vy = 0.0
    player_color = int(random(4))
    camera_y = player_y - 640
    score  = 0
    difficulty_multiplier = 1.0
    obstacles = []
    changers = []
    spawn_y = -540
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
    high_score = max(high_score, score)


def do_jump():
    global player_vy
    player_vy = JUMP_VELOCITY

def make_ball_image():
    diameter = 2 * BALL_RADIUS
    img = create_image(diameter, diameter, ARGB)
    img.load_np_pixels()

    radius_squared = BALL_RADIUS * BALL_RADIUS

    # Loop over every pixel and set alpha to 255 if inside the circle, 0 if outside
    for row in range(diameter):
        for col in range(diameter):
            dist_from_center_sq = (col - BALL_RADIUS) * (col - BALL_RADIUS) + \
                                  (row - BALL_RADIUS) * (row - BALL_RADIUS)
            if dist_from_center_sq <= radius_squared:
                img.np_pixels[row, col, 0] = 255 # alpha
            else:
                img.np_pixels[row, col, 0] = 0
            img.np_pixels[row, col, 1] = 255  # red
            img.np_pixels[row, col, 2] = 255  # green
            img.np_pixels[row, col, 3] = 255  # blue

    img.update_np_pixels()
    return img


def draw_player():
    red, green, blue = GAME_COLORS[player_color]
    tint(red, green, blue)
    diameter = 2 * BALL_RADIUS
    image(ball_img, player_x - BALL_RADIUS, player_y - BALL_RADIUS, diameter, diameter)
    no_tint()

def draw_hud():
    fill(255)
    text_size(26)
    text_align(LEFT, TOP)
    text("Score: " + str(score), 18, 16)
    text("High: "  + str(high_score), 18, 48)
    no_stroke()
    red, green, blue = GAME_COLORS[player_color]
    fill(red, green, blue)
    ellipse(WIDTH - 42, 36, 34, 34)


def draw_title(center_x, center_y):
    label = "COLOR JUMP"
    text_size(76)
    total_text_width = 0
    for character in label:
        total_text_width += text_width(character)
    current_x = center_x - total_text_width / 2
    text_align(LEFT, CENTER)
    color_mode(HSB, 360, 100, 100)    # Skill 3 using colors
    for char_index, character in enumerate(label):
        fill(char_index * 360 / len(label), 85, 100)
        text(character, current_x, center_y)
        current_x += text_width(character)
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
    text("Score: "      + str(score),      WIDTH / 2, 440)
    text("High Score: " + str(high_score), WIDTH / 2, 490)
    text_size(26)
    text("Press R to Restart", WIDTH / 2, 580)

def update_play():
    global player_vy, player_y, camera_y, difficulty_multiplier, obstacles, changers

    # gravity
    player_vy += GRAVITY
    player_y  += player_vy

    # move screen up
    if player_y - 640 < camera_y:
        camera_y = player_y - 640

    fill_world()

    # remove obstacles
    despawn_y = camera_y + HEIGHT + 260
    new_obstacles = []
    for obstacle in obstacles:
        if obstacle.y < despawn_y:
            new_obstacles.append(obstacle)
    obstacles = new_obstacles

    new_changers = []
    for changer in changers:
        if changer.y < despawn_y:
            new_changers.append(changer)
    changers = new_changers

    # animate obstacles
    for obstacle in obstacles:
        obstacle.update(difficulty_multiplier)

    # increase difficulty per score
    difficulty_multiplier = 1.0 + min(score // 10, 8) * 0.07

    for changer in changers:
        changer.try_trigger(player_x, player_y)
        
    if player_y - camera_y > HEIGHT + 90:
        die()


def draw_play():
    background(0)

    # draw obstacles
    push_matrix()
    translate(0, -camera_y)
    for obstacle in obstacles:
        obstacle.display()
    pop_matrix()

    # collisions
    if orb_hits_obstacle():
        die()

    # color change
    push_matrix()
    translate(0, -camera_y)
    for changer in changers:
        changer.display()
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

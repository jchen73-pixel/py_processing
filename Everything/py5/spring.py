# PY5 IMPORTED MODE CODE
def draw_sun(x, y, size):
    """
    Draw a bright spring sun with rays
    x, y: center position
    size: diameter of the sun
    """
    # Soft glow
    no_stroke()
    fill(255, 255, 150, 60)
    ellipse(x, y, size + 40, size + 40)

    # Rays
    stroke(255, 220, 50)
    stroke_weight(3)
    for i in range(12):
        angle = i * TWO_PI / 12
        ray_start = size / 2 + 5
        ray_end = size / 2 + 20
        line(x + cos(angle) * ray_start, y + sin(angle) * ray_start,
             x + cos(angle) * ray_end,   y + sin(angle) * ray_end)

    # Main disc
    no_stroke()
    fill(255, 230, 50)
    ellipse(x, y, size, size)


def draw_clouds():
    """
    Draw a few fluffy spring clouds across the sky
    """
    fill(255, 255, 255, 200)
    no_stroke()
    for cx, cy in [(130, 100), (350, 70), (600, 110)]:
        ellipse(cx,       cy,       80, 50)
        ellipse(cx - 30,  cy + 10,  60, 40)
        ellipse(cx + 30,  cy + 10,  60, 40)
        ellipse(cx - 10,  cy - 15,  55, 40)


def draw_rolling_hill(x, y, w, h, hill_color):
    """
    Draw a gently rolling grassy hill
    x, y: top-left anchor
    w, h: width and height of the hill region
    hill_color: fill color for the grass
    """
    fill(hill_color)
    no_stroke()
    begin_shape()
    vertex(x, y + h)
    vertex(x, y + h * 0.4)
    bezier_vertex(x + w * 0.25, y - h * 0.1,
                 x + w * 0.75, y - h * 0.1,
                 x + w, y + h * 0.4)
    vertex(x + w, y + h)
    end_shape(CLOSE)


def draw_tree(x, y, size):
    """
    Draw a blooming spring tree with pink blossoms
    x, y: base of the trunk
    size: overall height of the tree
    """
    trunk_h = size * 0.4
    trunk_w = size * 0.12

    # Trunk
    fill(120, 80, 40)
    stroke(90, 60, 30)
    stroke_weight(1)
    rect(x - trunk_w / 2, y - trunk_h, trunk_w, trunk_h)

    # Blossom canopy layers
    no_stroke()
    for dx, dy, r in [( 0, -trunk_h - size*0.3, size*0.45),
                      (-size*0.18, -trunk_h - size*0.15, size*0.35),
                      ( size*0.18, -trunk_h - size*0.15, size*0.35)]:
        fill(255, 180, 200, 200)
        ellipse(x + dx, y + dy, r * 2, r * 1.8)

    # Small blossom dots
    fill(255, 220, 230)
    no_stroke()
    for dx, dy in [(-20, -trunk_h - size*0.4), (15, -trunk_h - size*0.38),
                   (-5, -trunk_h - size*0.48), (20, -trunk_h - size*0.2),
                   (-18, -trunk_h - size*0.18)]:
        ellipse(x + dx, y + dy, 10, 10)


def draw_flower(x, y, petal_color):
    """
    Draw a simple wildflower with petals and a yellow center
    x, y: base of the stem
    petal_color: color of the petals
    """
    stem_h = 30

    # Stem
    stroke(60, 160, 60)
    stroke_weight(2)
    line(x, y, x, y - stem_h)

    # Petals
    no_stroke()
    fill(petal_color)
    for i in range(6):
        angle = i * TWO_PI / 6
        px = x + cos(angle) * 9
        py = (y - stem_h) + sin(angle) * 9
        ellipse(px, py, 10, 10)

    # Center
    fill(255, 230, 50)
    ellipse(x, y - stem_h, 9, 9)


def draw_butterfly(x, y, wing_color):
    """
    Draw a delicate butterfly
    x, y: body center position
    wing_color: primary wing color
    """
    no_stroke()

    # Wings (upper)
    fill(wing_color)
    ellipse(x - 18, y - 8, 32, 22)
    ellipse(x + 18, y - 8, 32, 22)

    # Wings (lower, smaller)
    fill(red(wing_color), green(wing_color), blue(wing_color), 180)
    ellipse(x - 14, y + 10, 22, 16)
    ellipse(x + 14, y + 10, 22, 16)

    # Wing pattern dots
    fill(255, 255, 255, 180)
    ellipse(x - 18, y - 8, 8, 8)
    ellipse(x + 18, y - 8, 8, 8)

    # Body
    fill(60, 40, 20)
    ellipse(x, y, 6, 20)

    # Antennae
    stroke(60, 40, 20)
    stroke_weight(1)
    line(x, y - 10, x - 10, y - 22)
    line(x, y - 10, x + 10, y - 22)
    no_stroke()
    fill(60, 40, 20)
    ellipse(x - 10, y - 22, 4, 4)
    ellipse(x + 10, y - 22, 4, 4)


def draw_bird(x, y, bird_color):
    """
    Draw a small songbird perched in the air
    x, y: center of the bird body
    bird_color: breast/body color
    """
    # Body
    fill(bird_color)
    no_stroke()
    ellipse(x, y, 22, 14)

    # Head
    fill(bird_color)
    ellipse(x + 10, y - 6, 14, 12)

    # Wing
    fill(red(bird_color) - 40, green(bird_color) - 40, blue(bird_color) - 40)
    ellipse(x - 4, y, 18, 8)

    # Eye
    fill(0)
    ellipse(x + 13, y - 7, 3, 3)

    # Beak
    fill(255, 200, 50)
    triangle(x + 16, y - 6, x + 24, y - 5, x + 16, y - 3)

    # Tail
    fill(red(bird_color) - 30, green(bird_color) - 30, blue(bird_color) - 30)
    triangle(x - 10, y - 2, x - 10, y + 4, x - 20, y + 2)


def draw_pond(x, y, size):
    """
    Draw a small reflective pond with lily pads
    x, y: center of the pond
    size: width of the pond
    """
    # Water
    fill(80, 160, 220, 180)
    no_stroke()
    ellipse(x, y, size, size * 0.5)

    # Reflection shimmer
    stroke(180, 220, 255, 120)
    stroke_weight(1)
    line(x - size * 0.25, y - 4, x + size * 0.1, y - 4)
    line(x - size * 0.1,  y + 2, x + size * 0.25, y + 2)

    # Lily pads
    no_stroke()
    fill(60, 160, 60, 200)
    ellipse(x - size * 0.2, y + 3,  18, 12)
    ellipse(x + size * 0.2, y - 2,  14, 9)

    # Lily pad notch
    fill(80, 160, 220, 180)
    triangle(x - size * 0.2, y + 3,
             x - size * 0.2 - 5, y - 3,
             x - size * 0.2 + 5, y - 3)


def draw_garden_path(x, y, length):
    """
    Draw a simple stepping-stone garden path
    x, y: starting point
    length: how long the path runs
    """
    fill(200, 180, 150)
    stroke(160, 140, 110)
    stroke_weight(1)
    step = length / 5
    for i in range(5):
        stone_x = x + i * step + random(-4, 4)
        stone_y = y + random(-4, 4)
        ellipse(stone_x, stone_y, 28, 18)


def draw_fence(x, y, length):
    """
    Draw a white picket fence
    x, y: left start of the fence base
    length: total width of the fence
    """
    stroke(240, 240, 240)
    stroke_weight(2)
    fill(250, 250, 250)
    picket_w = 12
    spacing  = 20
    count = int(length / spacing)

    # Rails
    line(x, y - 20, x + length, y - 20)
    line(x, y - 5,  x + length, y - 5)

    # Pickets
    no_stroke()
    for i in range(count):
        px = x + i * spacing
        rect(px, y - 38, picket_w, 35)
        triangle(px,               y - 38,
                 px + picket_w,    y - 38,
                 px + picket_w/2,  y - 50)


def draw_rain_boots(x, y):
    """
    Draw a pair of colorful rain boots
    x, y: center base position
    """
    fill(200, 50, 50)
    stroke(160, 30, 30)
    stroke_weight(1)

    # Left boot
    rect(x - 22, y - 30, 16, 24)
    rect(x - 26, y - 10, 22, 12)

    # Right boot
    rect(x + 6,  y - 30, 16, 24)
    rect(x + 4,  y - 10, 22, 12)

    # Cuff stripe
    fill(255, 255, 255)
    no_stroke()
    rect(x - 22, y - 30, 16, 5)
    rect(x + 6,  y - 30, 16, 5)


def draw_watering_can(x, y):
    """
    Draw a classic gardening watering can
    x, y: center base position
    """
    fill(100, 180, 100)
    stroke(70, 140, 70)
    stroke_weight(1)

    # Body
    ellipse(x, y - 15, 36, 28)

    # Spout
    line(x + 16, y - 20, x + 38, y - 8)
    line(x + 36, y - 8,  x + 42, y - 16)

    # Handle arc
    noFill()
    stroke(70, 140, 70)
    arc(x, y - 28, 28, 22, PI + HALF_PI, TWO_PI)
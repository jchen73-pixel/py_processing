# PY5 IMPORTED MODE CODE
class Tile:
    def __init__(self, x, y, direction, angle, letter):
        self.x = x
        self.y = y
        self.dir = direction
        self.angle = angle
        self.letter = letter
        self.opacity = 60
        self.hovered = False

    def checkDead(self):
        if self.y > height + 50:
            return True
        return False

    def checkHover(self, x, y):
        if abs(x - self.x) < 25 and abs(y - self.y) < 25:
            self.hovered = True
            self.opacity = 230
        else:
            self.hovered = False
            self.opacity += (60 - self.opacity) * 0.15

    def display(self):
        self.angle -= 1
        self.y += 1
        push_style()
        rect_mode(CENTER)
        text_align(CENTER, CENTER)
        push_matrix()
        translate(self.x, self.y)
        if self.dir == "left":
            rotate(radians(self.angle))
        elif self.dir == "right":
            rotate(-radians(self.angle))
        no_stroke()

        if self.hovered:
            fill(92, 79, 63, self.opacity)
            rect(-3, 3, 50, 50, 10)
        
        stroke(253, 217, 169, self.opacity)
        fill(253, 217, 169, self.opacity)
        rect(0, 0, 50, 50, 10)
        fill(0, 0, 0, self.opacity)
        text_size(30)
        text(self.letter, 0, -2)
        pop_matrix()
        pop_style()
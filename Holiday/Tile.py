# PY5 IMPORTED MODE CODE
class Tile:
    def __init__(self, x, y, scal, direction, angle, letter):
        rect_mode(CENTER)
        self.x = x
        self.y = y
        self.scal = scal
        self.dir = direction
        self.angle = angle
        self.letter = letter
        self.opacity = 200
    def checkDead(self):
        if self.y > height + 50:
            return True
        return False
    def display(self):
        self.angle -= 1
        self.y += 1
        push_matrix()
        translate(self.x, self.y)
        if self.dir == "left":
            rotate(radians(self.angle))
        elif self.dir == "right":
            rotate(-radians(self.angle))
        no_stroke()
        fill(92, 79, 63, self.opacity) #shadow color
        rect(-3, 3, 50, 50, 10)
        stroke(253, 217, 169)
        fill(253, 217, 169, self.opacity) #scrabble wood color
        rect(0, 0, 50, 50, 10)
        fill(0, 0, 0, self.opacity)
        text_size(30)
        text(self.letter, -8, 10)
        pop_matrix()
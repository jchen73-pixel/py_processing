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
    def display(self):
        push_matrix()
        translate(self.x, self.y)
        if self.dir == 0:
            rotate(radians(self.angle))
        elif self.dir == 1:
            rotate(-radians(self.angle))
        fill(92, 79, 63) #shadow color
        rect(-3, 3, 50, 50, 10)
        fill(253, 217, 169) #scrabble wood color
        rect(0, 0, 50, 50, 10)
        fill(0)
        text_size(30)
        text(self.letter, -8, 10)
        pop_matrix()
    def animate(self):
        self.angle -= 1
        self.y += 1
        self.display()
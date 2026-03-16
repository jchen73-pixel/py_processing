class Brush:
    def __init__(self, px, py, x, y, bSize, bColor):
        self.px = px
        self.py = py
        self.x = x
        self.y = y
        self.size = bSize
        self.color = bColor
    def paint(self):
        fill(self.color)
        stroke(self.color)
        size(self.size)
        line(self.px, self.py, self.x, self.y)
# PY5 IMPORTED MODE CODE
# to do
# name, x pos, y pos, direction, speed, size, color, health, hunger, level
# sleep boolean, movement frames, inner rectangle and outer shell of tamogatchi
class Tamogatchi:
    def __init__(self, name, x, y, petSize, petColor, health="100", hunger="0", xSpd=3, ySpd=3):
        self.name = name
        self.x = x
        self.y = y
        self.size = petSize
        self.color = petColor
        self.health = health
        self.hunger = hunger
        self.xSpd = xSpd
        self.ySpd = ySpd
    def display(self):
        im = load_image("temp.png")
        image(im, self.x, self.y)
    def move(self):
        self.x += self.xSpd
        self.y += self.ySpd
    def bounceOnEdge(self):
        if self.x > width or self.x < 0:
            self.xSpd*=-1
        if self.y > height or self.y < 0:
            self.ySpd*=-1
    def animate(self):
      self.display()
      self.move()
      self.bounceOnEdge()
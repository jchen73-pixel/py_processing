# PY5 IMPORTED MODE CODE
from spring import *

class Wiggler:
    def __init__(self, w, h):
        self.x = random(width-w) 			#will appear anywhere on canvas
        self.y = random(height-h) 		#will appear anywhere on canvas
        self.w = w
        self.h = h
        self.xSpd = random(-5, 5) 	#create random movement
        self.ySpd = random(-5, 5) 	#create random movement
        self.color = color(random(255),random(255),random(255))

    def display(self):
        #rect(self.x, self.y, self.w, self.h)
        # draw_butterfly(x, y, wing_color):
        draw_butterfly(self.x,self.y, self.color)
        
    def move(self):
        self.x += self.xSpd
        self.xSpd = random(-5, 5) #pick a new speed so it looks 'wiggly'
        self.y += self.ySpd
        self.ySpd = random(-5, 5) #pick a new speed so it looks 'wiggly'
        
    def bounceOnEdge(self):
      if self.x > width-self.w or self.x < 0:
        self.xSpd*=-1
      if self.y > height-self.h or self.y < 0:
        self.ySpd*=-1

    def animate(self):
      #fill(self.color)
      self.display()
      self.move()
      self.bounceOnEdge()



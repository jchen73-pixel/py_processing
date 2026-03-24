# PY5 IMPORTED MODE CODE
class Bubble:
    def __init__(self, diam):
        self.x = random(width-diam) 		#will appear anywhere on canvas
        self.y = random(height-diam) 		#will appear anywhere on canvas
        self.w = diam
        self.xSpd = random(-5, 5) 	#create random movement
        self.ySpd = random(-5, 5) 	#create random movement
        self.color = color(random(255),random(255),random(255),random(55,70))
        self.stroke = color(random(255),random(255),random(255),50)
        
        if random(2) < 1:
            self.innerX = self.x + self.w/random(5,7)
        else:
            self.innerX = self.x - self.w/random(5,7)
        if random(2) < 1:
            self.innerY = self.y + self.w/random(5,7)
        else:
            self.innerY = self.y - self.w/random(5,7)
        self.innerW = self.w/random(3,5)
        self.innerFill = color(random(255),random(255),random(255),50)
        self.innerStroke = color(random(255),random(255),random(255),50)
        
#         for i in range(0,360,5):
#             stroke(random(255),random(255),random(255))
#             arc(self.x,self.y,self.w,self.w,radians(i),radians(i+10),OPEN)

    def display(self):
        fill(self.color)
        stroke(self.stroke)
        circle(self.x, self.y, self.w)
        fill(self.innerFill)
        stroke(self.innerStroke)
        circle(self.innerX, self.innerY, self.innerW)
        
    def move(self):
        self.x += self.xSpd
        self.innerX += self.xSpd
        #self.xSpd = random(-5, 5) #pick a new speed so it looks 'wiggly'
        self.y += self.ySpd
        self.innerY += self.ySpd
        #self.ySpd = random(-5, 5) #pick a new speed so it looks 'wiggly'
        
    def bounceOnEdge(self):
      if self.x > width-self.w or self.x < 0:
        self.xSpd*=-1
      if self.y > height-self.w or self.y < 0:
        self.ySpd*=-1

    def animate(self):
      self.display()
      self.move()
      self.bounceOnEdge()
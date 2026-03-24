def setup():
  size(510,350)
  rect_mode(CENTER)

angle = 0
def draw():
  global angle
  background(220)
  
  #2. move the origin to the pivot point (what you want to rotate around)
  translate(width/2, height/2)
  
  #3. then rotate the grid around the pivot point using the variable you created
  push_matrix()
  rotate(radians(angle))
  rect(50,50,100,20)
  pop_matrix()
  
  #4. Increment your rotation variable to make the rotation animated
  angle+=1
  
  push_matrix()
  rotate(radians(-angle))
  fill(0)
  rect(0, 0, 100, 100)
  pop_matrix()
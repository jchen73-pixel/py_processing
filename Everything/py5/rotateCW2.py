def setup():
  size(510,350)

def draw():
  background(220)
  
  #2. move the origin to the pivot point (what you want to rotate around)
  translate()
  
  #3. then rotate the grid around the pivot point using the variable you created
  rect(50,50,100,20)
  
  #4. Increment your rotation variable to make the rotation animated
  
  fill(0)
  rect(0, 0, 100, 100)
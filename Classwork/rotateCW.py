def setup():
  size(510,350)

def draw():
  background(220)
  push_matrix()
  translate(width/2, height/2)
  angle = remap(mouse_x, 0, width, 0, 360)
  rotate(radians(angle))
  rect(-40,-20,80,40)
  pop_matrix()

#COMPLETE THE FOLLOWING AND LEAVE YOUR ANSWERS AS COMMENTS:

#1. Play with the values for rotation (keep them below 6.28 for now - that's 2 pi!)

#2. What happens if you move the rectangle to (0, 0)?
# The rectangle rotates about the origin.

#3. What happens if you add a translation before the rotation? (Try changing where it translates to!)
# The rectangle rotates about the new origin.

#4. What if you make the rortation the center of the page with a translation?


#5. What if the rotation is controlled by mouseX or mouseY?
# The rectangle would spin depending on where your mouse is.

#6. What if you plug in radians(50) to rotate()?
# It still rotates the rectangle, at 50 degrees.
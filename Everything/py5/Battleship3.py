from gridNdot import *
'''
Use the following program to play the THIRD round of transformation Battle Ship!

1. You may ONLY CHANGE the values in translate().
2. Now the translate for each shape is between a push() and pop()- this pushes a
transformation through, and pops the origin back to (0,0) so the next translation
can start fresh. You can adjust the code to decide what is included in each push()
and pop()
3. Once you've changed the translate values, hit play and let your partner know
you're ready.
4. Take turns guessing coordinates where you think the vertex of the shape
(or center of an ellipse) is on your partner's canvas.
5. If you guess a point from your partner, hold the shift key and click the
coordinate to leave a blue dot so you remember the point you found.
6. If your partner guesses correctly, say HIT. If they guess
incorrectly, say MISS. If they are on the shape but not on a vertex, tell them
they're close!
7. If you click a point, it will leave a red dot so you know they
found it.
'''

def setup():
    size(400,400)
    background(220)

def draw():
    no_stroke()
    text(str(mouse_x) + ", " + str(mouse_y), 20, 20)
    
    draw_grid()
    draw_dot()
    
  
    no_fill()
    stroke(0)
    stroke_weight(3)
    
    push_style()
    translate(0,0);
    ellipse(60,60,60,60)
    pop_style()
    
    push_style()
    translate(0,0);
    rect(140,50,80,40)
    pop_style()
    
    push_style()
    translate(0,0);
    rect(180,160,120,120)
    pop_style()
    
    push_style()
    translate(0,0);
    triangle(100,180,40,240,140,220)
    pop_style()
    
    push_style()
    translate(0,0);
    quad(260,120,280,80,340,80,342,140)
    pop_style()
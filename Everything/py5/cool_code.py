# credit to Run Chen
angle = 15

def setup():
    size(400,400)
    fill(0)
    frame_rate(200000)
def draw():
    global angle
    sin_value = remap(sin(radians(angle)),-1,1,100,300)
    cos_value = remap(cos(radians(angle)),-1,1,100,300)
    #print(sin_value)
   
    angle +=0.5
    for i in range(1):  #
        t=i
        push_matrix()  #
        translate(sin_value, cos_value)
        rotate(radians(angle*PI)+t)
        circle(70,70,1)
        pop_matrix()
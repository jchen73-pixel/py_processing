size(200,200)

fill(0,0,255) #first one is blue
#push_matrix() #this pushes through a translation of (50,50) for the first ellipse)
translate(50, 50)
ellipse(0,0,50,50)
#pop_matrix() #this removes the translation for future shapes

fill(255,0,0) # second one is red
#push_matrix() #this pushes through a translation of (20, 20) for the second ellipse
translate(20,20)
ellipse(0,0,50,50)
#pop_matrix() #this removes the translation for future shapes
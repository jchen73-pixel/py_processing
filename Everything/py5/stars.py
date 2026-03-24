num_stars = 200
stars = []

def setup():
  global stars
  size(400,400)
  background(0)
  # HSB (Hue, Saturation, Brightness) 
  color_mode(HSB, 360, 100, 100)
  for i in range(num_stars):
    stars.append(
      {"theColor": color(random(0,50),random(25),random(50)),
      "x": round(random(1,width)),
      "y": round(random(1,height)), 
      } )

      
def draw():
    background(0)
    for i in range(len(stars)):
        fill( stars[i]["theColor"] )
        circle( stars[i]["x"], stars[i]["y"], random(1,8))

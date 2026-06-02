import numpy as np
def setup():
  size(400, 400)
  img = load_image("moran.jpg")
  img.resize(width, height)
  image(img, 0, 0)

def draw():
  load_np_pixels()
  previous = np_pixels.copy()  # prevents copying already overwritten pixels
  for x in range(width):
    for y in range(height):
      if y == 0:   # case of the newest layer on top
        np_pixels[y, x, 1] = 0   # red
        np_pixels[y, x, 2] = 255    # green
        np_pixels[y, x, 3] = 0     # blue
      else:
        np_pixels[y, x, :] = previous[y - 1, x, :]    # copy entire argb of pixel above from copy
  update_np_pixels()
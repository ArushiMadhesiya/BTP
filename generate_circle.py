import numpy as np
from skimage.draw import disk

# Image parameters
img_size = (100, 100)
center_x, center_y = 50, 50  # Circle center
radius = 20  # Radius of the circle

# Create an empty image and generate the filled circle
image = np.zeros(img_size, dtype=np.uint8)
rr, cc = disk((center_y, center_x), radius, shape=img_size)
image[rr, cc] = 1

# Save coordinates to a file
circle_coords = np.column_stack((cc, rr))
with open("circle.txt", "w") as f:
    for x, y in circle_coords:
        f.write(f"{x},{y}\n")

import numpy as np
from skimage.draw import polygon

# Image parameters
img_size = (100, 100)
center_x, center_y = 50, 50
side_length = 40  # Length of each side of the equilateral triangle

# Calculate vertices of an equilateral triangle centered at (center_x, center_y)
height = np.sqrt(3) / 2 * side_length
vertex1 = (center_x, center_y - 2 * height / 3)
vertex2 = (center_x - side_length / 2, center_y + height / 3)
vertex3 = (center_x + side_length / 2, center_y + height / 3)

# Extract x and y coordinates of vertices
x_coords = np.array([vertex1[0], vertex2[0], vertex3[0]])
y_coords = np.array([vertex1[1], vertex2[1], vertex3[1]])

# Use skimage to create the filled triangle image
image = np.zeros(img_size, dtype=np.uint8)
rr, cc = polygon(y_coords, x_coords, image.shape)
image[rr, cc] = 1

# Save coordinates to a file
triangle_coords = np.column_stack((cc, rr))
with open("triangle.txt", "w") as f:
    for x, y in triangle_coords:
        f.write(f"{x},{y}\n")

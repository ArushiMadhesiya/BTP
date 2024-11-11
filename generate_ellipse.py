import numpy as np

# Ellipse parameters
center_x, center_y = 50, 50   # Center of the ellipse in the image
semi_major = 20               # Semi-major axis (horizontal radius)
semi_minor = 10               # Semi-minor axis (vertical radius)
img_size = (100, 100)         # Size of the output image

# Generate coordinates for a filled ellipse
coords = []

# Loop over a bounding box around the ellipse
for y in range(center_y - semi_minor, center_y + semi_minor + 1):
    for x in range(center_x - semi_major, center_x + semi_major + 1):
        # Check if the point (x, y) is within the ellipse equation
        if ((x - center_x)**2) / (semi_major**2) + ((y - center_y)**2) / (semi_minor**2) <= 1:
            coords.append((x, y))

# Save coordinates to a .txt file
with open('ellipse.txt', 'w') as f:
    for x, y in coords:
        f.write(f"{x},{y}\n")

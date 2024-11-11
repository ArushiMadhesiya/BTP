import numpy as np

def generate_ellipse_coordinates(x_center, y_center, a, b, num_points, filename):
    coordinates = []

    # Generate ellipse points using parametric equations
    for theta in np.linspace(0, 2 * np.pi, num_points):
        x = int(x_center + a * np.cos(theta))
        y = int(y_center + b * np.sin(theta))
        coordinates.append((x, y))

    # Remove duplicates in case of rounding to integers
    coordinates = list(set(coordinates))

    # Write the coordinates to a file
    with open(filename, 'w') as f:
        for coord in coordinates:
            f.write(f"{coord[0]},{coord[1]}\n")

# Parameters for the ellipse
x_center = 250  # x-coordinate of the center
y_center = 250  # y-coordinate of the center
a = 100         # Semi-major axis (horizontal radius)
b = 50          # Semi-minor axis (vertical radius)
num_points = 500  # Number of points to generate along the ellipse

# Generate and save the ellipse coordinates to a .txt file
generate_ellipse_coordinates(x_center, y_center, a, b, num_points, 'ellipse.txt')

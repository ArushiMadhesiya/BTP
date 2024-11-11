import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import polygon
from skimage.morphology import medial_axis

def load_coordinates(file_path):
    """
    Load x, y coordinates from a file.
    
    Parameters:
    - file_path: path to the .txt file containing x, y coordinates (one pair per line, comma-separated).
    
    Returns:
    - x_coords, y_coords: lists of x and y coordinates.
    """
    x_coords, y_coords = [], []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split(','))
            x_coords.append(x)
            y_coords.append(y)
    return x_coords, y_coords

def generate_shape_from_coordinates(x, y, img_size=(100, 100)):
    """
    Create a filled binary image from the given x, y coordinates.
    
    Parameters:
    - x, y: lists of x and y coordinates of the shape.
    - img_size: size of the output image.
    
    Returns:
    - A binary image with the shape filled in.
    """
    # Initialize a binary image
    image = np.zeros(img_size, dtype=np.uint8)

    # Use polygon to fill the area enclosed by the given coordinates
    rr, cc = polygon(y, x, image.shape)
    image[rr, cc] = 1  # Fill the area inside the shape with white (1)

    return image

def compute_and_display_medial_axis(binary_image):
    """
    Compute and display the medial axis of a binary image.
    """
    skeleton, distance = medial_axis(binary_image, return_distance=True)
    distance_on_skeleton = distance * skeleton

    # Extract (x, y) coordinates where skeleton is True (medial axis points)
    y_coords, x_coords = np.where(skeleton)
    medial_axis_coords = list(zip(x_coords, y_coords))

    # Save coordinates to a file
    with open("medial_axis_coordinates_rect.txt", "w") as f:
        for x, y in medial_axis_coords:
            f.write(f"{x},{y}\n")

    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    ax = axes.ravel()

    ax[0].imshow(binary_image, cmap=plt.cm.gray)
    ax[0].set_title('Binary Image')
    
    ax[1].imshow(skeleton, cmap=plt.cm.gray)
    ax[1].set_title('Medial Axis Skeleton')
    
    ax[2].imshow(distance_on_skeleton, cmap=plt.cm.inferno)
    ax[2].set_title('Distance on Skeleton')

    for a in ax:
        a.axis('off')

    plt.tight_layout()
    plt.show()

# Load coordinates from the .txt file
# Full pipeline from loading coordinates to generating the binary image


file_path = 'rectangle.txt'  # Change this to the path of your coordinates file
x_coords, y_coords = load_coordinates(file_path)
binary_image = generate_shape_from_coordinates(x_coords, y_coords)

# Compute and display the Medial Axis Transform
compute_and_display_medial_axis(binary_image)
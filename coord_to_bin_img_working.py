import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import polygon

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

# Full pipeline from loading coordinates to generating the binary image
file_path = 'rectangle.txt'  # Change this to the path of your coordinates file
x_coords, y_coords = load_coordinates(file_path)
binary_image = generate_shape_from_coordinates(x_coords, y_coords)

# Display the binary image
plt.imshow(binary_image, cmap="gray")
plt.title("Binary Image from Coordinates (Filled Shape)")
plt.axis("off")
plt.show()

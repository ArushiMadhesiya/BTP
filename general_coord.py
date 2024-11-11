import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import polygon
from skimage.morphology import medial_axis

def load_coordinates_from_file(filename):
    """
    Load coordinates from a .txt file.
    
    Parameters:
    - filename: the path to the .txt file with coordinates.
    
    Returns:
    - Two arrays: x and y coordinates.
    """
    coordinates = np.loadtxt(filename, delimiter=',')
    x, y = coordinates[:, 0], coordinates[:, 1]
    return x, y

def generate_shape_from_coordinates(x, y, img_size=(100, 100)):
    """
    Create a binary image from the given x, y coordinates.
    
    Parameters:
    - x, y: arrays of x and y coordinates of the shape.
    - img_size: size of the output image.
    
    Returns:
    - A binary image with the shape filled in.
    """
    image = np.zeros(img_size, dtype=np.uint8)
    rr, cc = polygon(y, x, image.shape)
    image[rr, cc] = 1
    return image

def compute_and_display_medial_axis(binary_image):
    """
    Compute and display the medial axis of a binary image.
    """
    skeleton, distance = medial_axis(binary_image, return_distance=True)
    distance_on_skeleton = distance * skeleton

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
x, y = load_coordinates_from_file('rectangle.txt')

# Generate binary image
binary_image = generate_shape_from_coordinates(x, y, img_size=(100, 100))

# Compute and display the Medial Axis Transform
compute_and_display_medial_axis(binary_image)

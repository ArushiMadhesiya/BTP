import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, filters
from skimage.morphology import binary_closing, disk
from skimage.measure import find_contours

def extract_boundary_coordinates_from_image(image_path, threshold=0.5):
    """
    Extract boundary coordinates of white areas in a binary image.

    Parameters:
    - image_path: Path to the input image.
    - threshold: Threshold to binarize the image; default is 0.5.

    Returns:
    - List of (x, y) coordinates for the boundary.
    """
    # Load the image
    image = io.imread(image_path)
    
    # Convert to grayscale if the image is colored
    if image.ndim == 3:
        image = color.rgb2gray(image)
    
    # Binarize the image (assuming white areas are the regions of interest)
    binary_image = image > threshold

    # Optional: close small gaps in the binary image
    binary_image = binary_closing(binary_image, disk(2))
    
    # Find contours (boundaries) of the white areas
    contours = find_contours(binary_image, level=0.5)

    # Combine all contour points into a single list of coordinates
    boundary_coords = []
    for contour in contours:
        for y, x in contour:
            boundary_coords.append((int(x), int(y)))  # Convert to integer coordinates
    
    # Save coordinates to a file
    with open("boundary_coordinates_rect.txt", "w") as f:
        for x, y in boundary_coords:
            f.write(f"{x},{y}\n")
    
    # Plot the original binary image with boundaries
    fig, ax = plt.subplots()
    ax.imshow(binary_image, cmap=plt.cm.gray)
    
    for contour in contours:
        ax.plot(contour[:, 1], contour[:, 0], linewidth=2, color="cyan")
    
    ax.set_title("Boundary of White Area")
    plt.show()

    return boundary_coords

# Example usage
image_path = 'rect1.png'  # Update with your actual image path
boundary_coordinates = extract_boundary_coordinates_from_image(image_path)

import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
from skimage.morphology import medial_axis
from skimage.filters import threshold_otsu
from skimage.measure import label, regionprops

def process_image(image_path):
    """
    Process an input image to find the medial axis of the shape in the image.
    
    Parameters:
    - image_path: Path to the image file.
    
    Returns:
    - None (Displays the original image, binary image, medial axis, and distance).
    """
    # Step 1: Load the image
    image = io.imread(image_path)

    # Convert to grayscale
    grayscale_image = color.rgb2gray(image)
    
    # Step 2: Thresholding to create a binary image (black and white)
    thresh = threshold_otsu(grayscale_image)
    binary_image = grayscale_image > thresh

    # Step 3: Compute the Medial Axis Transform (MAT)
    skeleton, distance = medial_axis(binary_image, return_distance=True)

    # Medial Axis Transform distance
    distance_on_skeleton = distance * skeleton

    # Step 4: Plot the results
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    ax = axes.ravel()

    ax[0].imshow(image)
    ax[0].set_title('Original Image')
    
    ax[1].imshow(binary_image, cmap=plt.cm.gray)
    ax[1].set_title('Binary Image')

    ax[2].imshow(skeleton, cmap=plt.cm.gray)
    ax[2].set_title('Medial Axis Skeleton')

    ax[3].imshow(distance_on_skeleton, cmap=plt.cm.inferno)
    ax[3].set_title('Distance on Skeleton')

    for a in ax:
        a.axis('off')

    plt.tight_layout()
    plt.show()

# Example: Load an image containing a shape (e.g., ellipse, rectangle)
image_path = 'india.png'  # Replace with your image path
process_image(image_path)

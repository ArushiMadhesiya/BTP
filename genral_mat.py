import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import medial_axis

def generate_rectangle_image(width, height, img_size=(100, 100)):
    """
    Generate a binary image with a white rectangle on a black background.
    
    Parameters:
    - width, height: dimensions of the rectangle.
    - img_size: dimensions of the output image.
    
    Returns:
    - Binary image with a rectangle in the center.
    """
    image = np.zeros(img_size, dtype=np.uint8)
    start_x = (img_size[0] - width) // 2
    start_y = (img_size[1] - height) // 2
    image[start_y:start_y + height, start_x:start_x + width] = 1
    return image

def compute_and_display_medial_axis(binary_image):
    """
    Compute and display the medial axis of a binary image.
    
    Parameters:
    - binary_image: binary image with the shape.
    """
    # Compute the Medial Axis Transform (MAT)
    skeleton, distance = medial_axis(binary_image, return_distance=True)

    # Medial Axis Transform distance
    distance_on_skeleton = distance * skeleton

    # Plot original binary image, medial axis skeleton, and distance on skeleton
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

# Generate a binary image with a centered rectangle
# binary_image = generate_rectangle_image(width=20, height=20, img_size=(100, 100))

# # Compute and display the Medial Axis Transform
# compute_and_display_medial_axis(binary_image)

from skimage.draw import ellipse

def generate_ellipse_image(semi_major_axis, semi_minor_axis, img_size=(100, 100)):
    """
    Generate a binary image with a white ellipse on a black background.
    
    Parameters:
    - semi_major_axis, semi_minor_axis: semi-major and semi-minor axes of the ellipse.
    - img_size: dimensions of the output image.
    
    Returns:
    - Binary image with an ellipse in the center.
    """
    image = np.zeros(img_size, dtype=np.uint8)
    
    # Generate ellipse in the center of the image
    rr, cc = ellipse(img_size[0] // 2, img_size[1] // 2, semi_major_axis, semi_minor_axis)
    
    # Ensure that the ellipse is within the image boundaries
    rr = np.clip(rr, 0, img_size[0] - 1)
    cc = np.clip(cc, 0, img_size[1] - 1)
    
    # Set the pixels inside the ellipse to 1 (white)
    image[rr, cc] = 1
    return image

# Generate a binary image with a centered ellipse
binary_image_ellipse = generate_ellipse_image(semi_major_axis=30, semi_minor_axis=20, img_size=(100, 100))

# Compute and display the Medial Axis Transform for the ellipse
compute_and_display_medial_axis(binary_image_ellipse)

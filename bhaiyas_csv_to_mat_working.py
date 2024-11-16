import numpy as np
import matplotlib.pyplot as plt
from skimage.draw import polygon
from skimage.morphology import medial_axis
from scipy.interpolate import splprep, splev


def load_coordinates_from_csv(file_path):
    """
    Load x, y coordinates from a CSV file.
    
    Parameters:
    - file_path: path to the .csv file containing X, Y coordinates.
    
    Returns:
    - x_coords, y_coords: numpy arrays of x and y coordinates.
    """
    data = np.genfromtxt(file_path, delimiter=',', skip_header=1, names=["X", "Y"])
    return data["X"], data["Y"]


def interpolate_curve(x, y, num_points=500):
    """
    Interpolate the curve to generate a smoother representation.
    
    Parameters:
    - x, y: x and y coordinates of the curve.
    - num_points: number of interpolated points.
    
    Returns:
    - interpolated_x, interpolated_y: numpy arrays of interpolated x and y coordinates.
    """
    tck, _ = splprep([x, y], s=0.5)  # Spline fitting
    u = np.linspace(0, 1, num_points)  # Generate parameter values
    interpolated_x, interpolated_y = splev(u, tck)
    return interpolated_x, interpolated_y


def generate_shape_from_coordinates(x, y, img_size=(500, 500)):
    """
    Create a filled binary image from the given x, y coordinates.
    
    Parameters:
    - x, y: lists or arrays of x and y coordinates of the shape.
    - img_size: size of the output image.
    
    Returns:
    - A binary image with the shape filled in.
    """
    # Normalize coordinates to fit the image size
    x = np.interp(x, (np.min(x), np.max(x)), (0, img_size[1] - 1))
    y = np.interp(y, (np.min(y), np.max(y)), (0, img_size[0] - 1))

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
    with open("medial_axis_coordinates_curve_bhaiya_fig2.txt", "w") as f:
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


# Load coordinates from the .csv file
file_path = 'curve.csv'  # Update this to the path of your curve.csv file
x_coords, y_coords = load_coordinates_from_csv(file_path)

# Interpolate the curve for smoothness
interpolated_x, interpolated_y = interpolate_curve(x_coords, y_coords)

# Generate the binary image from the interpolated coordinates
binary_image = generate_shape_from_coordinates(interpolated_x, interpolated_y)

# Compute and display the Medial Axis Transform
compute_and_display_medial_axis(binary_image)

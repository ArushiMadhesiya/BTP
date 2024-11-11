import cv2
import numpy as np

# Read coordinates from the .txt file and create a binary image
def read_coordinates(filename):
    with open(filename, 'r') as f:
        coordinates = [tuple(map(int, line.strip().split(','))) for line in f]
    return coordinates

def create_binary_image(coordinates, img_size):
    img = np.zeros(img_size, np.uint8)  # Create a blank binary image
    for coord in coordinates:
        img[coord[1], coord[0]] = 255   # Mark the pixel corresponding to the shape
    return img

# Read coordinates from .txt file (e.g., 'shape.txt')
coordinates = read_coordinates('rectangle.txt')

# Define image size (based on shape bounds or predefined size)
img_size = (500, 500)  # Adjust the size as needed
binary_img = create_binary_image(coordinates, img_size)

# Invert the binary image (if necessary, depends on how the coordinates define the shape)
binary_img_inv = cv2.bitwise_not(binary_img)

# Perform skeletonization using morphological operations
skel = np.zeros(binary_img_inv.shape, np.uint8)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

done = False
while not done:
    eroded = cv2.erode(binary_img_inv, element)
    dilated = cv2.dilate(eroded, element)
    temp = cv2.subtract(binary_img_inv, dilated)
    skel = cv2.bitwise_or(skel, temp)
    binary_img_inv = eroded.copy()
    done = cv2.countNonZero(binary_img_inv) == 0

# Invert the skeleton image (if required)
skel = cv2.bitwise_not(skel)

# Extract the coordinates of the medial axis (skeleton)
skeleton_coords = np.column_stack(np.where(skel == 255))


# Show the result
cv2.imshow("Skeleton", skel)
cv2.waitKey(0)
cv2.destroyAllWindows()

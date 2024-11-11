import cv2
import numpy as np

# Function to read coordinates from a file
def read_coordinates(filename):
    with open(filename, 'r') as f:
        coordinates = [tuple(map(int, line.strip().split(','))) for line in f]
    return coordinates

# Function to create a binary image from coordinates
def create_binary_image(coordinates, img_size):
    img = np.zeros(img_size, np.uint8)
    for x, y in coordinates:
        img[y, x] = 255
    return img

# Function to save coordinates of white pixels in an image
def save_coordinates(image, output_filename):
    white_pixels = np.column_stack(np.where(image == 255))
    with open(output_filename, 'w') as f:
        for y, x in white_pixels:
            f.write(f"{x},{y}\n")

# Load coordinates and create the binary image
coordinates = read_coordinates('rectangle.txt')
img_size = (500, 500)
binary_img = create_binary_image(coordinates, img_size)

# Invert the binary image to prepare for skeletonization
binary_img_inv = cv2.bitwise_not(binary_img)

# Initialize an empty image to store the skeleton
skel = np.zeros(binary_img_inv.shape, np.uint8)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

# Skeletonization loop
done = False
while not done:
    eroded = cv2.erode(binary_img_inv, element)
    dilated = cv2.dilate(eroded, element)
    temp = cv2.subtract(binary_img_inv, dilated)
    skel = cv2.bitwise_or(skel, temp)
    binary_img_inv = eroded.copy()
    done = cv2.countNonZero(binary_img_inv) == 0

# Invert the skeleton to match the final result format
skel = cv2.bitwise_not(skel)

# Save the skeleton coordinates to a file
save_coordinates(skel, 'skeleton_coordinates1.txt')

# Display the final skeletonized image
cv2.imshow("Skeleton", skel)
cv2.waitKey(0)
cv2.destroyAllWindows()

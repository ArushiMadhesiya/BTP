import cv2
import numpy as np

def create_image_from_coordinates(filename, img_size):
    # Initialize a blank black image
    img = np.zeros(img_size, np.uint8)
    
    # Read the coordinates from the file and plot them
    with open(filename, 'r') as f:
        for line in f:
            x, y = map(int, line.strip().split(','))
            img[y, x] = 255  # Set the pixel to white at the specified coordinates
    
    return img

# Set the desired image size
img_size = (500, 500)  # Adjust based on your expected image size

# Create the image from the coordinates file
img_from_coordinates = create_image_from_coordinates('medial_axis_coordinates_rect.txt', img_size)

# Display the resulting image
cv2.imshow("Image from Coordinates", img_from_coordinates)
cv2.waitKey(0)
cv2.destroyAllWindows()

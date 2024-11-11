import cv2
import numpy as np

img = cv2.imread('rect.png', 0)

_, bin_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

bin_img_inv = cv2.bitwise_not(bin_img)

skel = np.zeros(bin_img_inv.shape, np.uint8)

element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

done = False
while not done:
    eroded = cv2.erode(bin_img_inv, element)

    dilated = cv2.dilate(eroded, element)
    
    temp = cv2.subtract(bin_img_inv, dilated)
    
    skel = cv2.bitwise_or(skel, temp)
    
    bin_img_inv = eroded.copy()

    done = cv2.countNonZero(bin_img_inv) == 0

skel = cv2.bitwise_not(skel)

cv2.imshow("Skeleton", skel)
cv2.waitKey(0)
cv2.destroyAllWindows()

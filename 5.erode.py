import cv2
import numpy as np

# Step 1: Read the image in grayscale
image = cv2.imread('image.jpg', 0)

# Step 2: Define the kernel (a matrix for erosion)
kernel = np.ones((5, 5), np.uint8)  # You can change size to (3,3), (7,7), etc.

# Step 3: Apply erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Step 4: Display original and eroded images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

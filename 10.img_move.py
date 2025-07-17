import cv2
import numpy as np

# Step 1: Read the image
image = cv2.imread('image.jpg')

# Step 2: Define the translation matrix
# Move the image 100 pixels right and 50 pixels down
translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])

# Step 3: Apply the translation
moved_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

# Step 4: Display the original and moved images
cv2.imshow("Original Image", image)
cv2.imshow("Moved Image", moved_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

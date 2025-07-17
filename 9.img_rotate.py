import cv2

# Step 1: Read the image
image = cv2.imread('image.jpg')

# Get the height and width of the image
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

# Step 2: Rotate 90 degrees clockwise
matrix_clockwise = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated_clockwise = cv2.warpAffine(image, matrix_clockwise, (w, h))

# Step 3: Rotate 90 degrees counterclockwise
matrix_counter = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated_counter = cv2.warpAffine(image, matrix_counter, (w, h))

# Step 4: Display the results
cv2.imshow("Original", image)
cv2.imshow("Rotated Clockwise", rotated_clockwise)
cv2.imshow("Rotated Counterclockwise", rotated_counter)

cv2.waitKey(0)
cv2.destroyAllWindows()

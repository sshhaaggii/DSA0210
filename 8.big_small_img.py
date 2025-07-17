import cv2

# Step 1: Read the image
image = cv2.imread('image.jpg')

# Step 2: Scale image to double the size (bigger)
bigger = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)

# Step 3: Scale image to half the size (smaller)
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Step 4: Display all images
cv2.imshow('Original Image', image)
cv2.imshow('Bigger Image (2x)', bigger)
cv2.imshow('Smaller Image (0.5x)', smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# Step 1: Read the image
image = cv2.imread('image.jpg')

# Step 2: Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Gaussian Blur (optional but recommended before Canny)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 4: Apply Canny edge detection
edges = cv2.Canny(blur, 100, 200)  # You can adjust thresholds (100, 200)

# Step 5: Display the result
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

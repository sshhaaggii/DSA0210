import cv2
import time

# Open the webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Choose the mode
print("Choose mode: \n1. Normal Speed \n2. Slow Motion \n3. Fast Motion")
mode = input("Enter choice (1/2/3): ")

# Set the delay between frames based on mode
if mode == '1':
    delay = 1       # Normal
elif mode == '2':
    delay = 100     # Slow motion (higher delay)
elif mode == '3':
    delay = 1       # Fast motion (process more frames quickly)
else:
    print("Invalid choice. Defaulting to normal speed.")
    delay = 1

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read frame.")
        break

    # Resize frame for faster processing (optional)
    frame = cv2.resize(frame, (640, 480))

    # Display the video frame
    cv2.imshow('Webcam Video', frame)

    # Add delay
    if mode == '2':  # Slow Motion
        time.sleep(0.05)  # 50 ms extra delay

    # Break on pressing 'q'
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

# Release the webcam and destroy windows
cap.release()
cv2.destroyAllWindows()

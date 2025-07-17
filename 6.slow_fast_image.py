import cv2

# Step 1: Load the video file
cap = cv2.VideoCapture("video.mp4")  # Replace with your video filename

# Step 2: Display video in slow motion
print("Playing in Slow Motion (press 'q' to skip)...")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Slow Motion", frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):  # 100 ms delay = slow motion
        break

cap.release()
cv2.destroyAllWindows()

# Step 3: Reload video for fast motion
cap = cv2.VideoCapture("video.mp4")

# Step 4: Display video in fast motion
print("Playing in Fast Motion (press 'q' to quit)...")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Fast Motion", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):  # 10 ms delay = fast motion
        break

cap.release()
cv2.destroyAllWindows()

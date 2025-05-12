import cv2
import numpy as np

# Initialize video capture
video_path = r"c:\Users\niviy\Downloads\archery.mp4"
 # Replace with your video path
cap = cv2.VideoCapture(video_path)

# Check if video loaded successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Create background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break  # End of video

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Filter the mask to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    # Find contours of the objects in the mask
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Filter out small objects
        if cv2.contourArea(contour) < 500:
            continue

        # Get bounding box for each object
        x, y, w, h = cv2.boundingRect(contour)
        # Draw bounding box on original frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show the frame with bounding boxes
    cv2.imshow('Sports Performance Analysis', frame)
    cv2.imshow('Foreground Mask', fgmask)

    # Exit on pressing 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()
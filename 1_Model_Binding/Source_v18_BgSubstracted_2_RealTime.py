import cv2
import numpy as np

# Create a background subtractor object
backSub = cv2.createBackgroundSubtractorMOG2()

# Create a VideoCapture object to capture webcam feed (index 0)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Main loop to read frames from the webcam
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # If the frame was not read correctly, break the loop
    if not ret:
        break

    # Apply the background subtraction
    fgMask = backSub.apply(frame)

    # Show the original frame
    cv2.imshow('Original', frame)

    # Show the background subtracted frame
    cv2.imshow('Background Subtracted', fgMask)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()

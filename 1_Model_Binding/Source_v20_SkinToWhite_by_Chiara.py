import cv2
import numpy as np

# Function to perform skin detection
def detect_skin(frame):
    # Convert the frame to the YCbCr color space
    ycbcr_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)

    # Define skin color range in YCbCr
    lower_skin = np.array([0, 133, 77], dtype=np.uint8)
    upper_skin = np.array([255, 173, 127], dtype=np.uint8)

    # Create a mask using the skin color range
    skin_mask = cv2.inRange(ycbcr_frame, lower_skin, upper_skin)

    # Set all pixels within the skin mask to white
    skin_detected = np.zeros_like(frame)
    skin_detected[skin_mask == 255] = (255, 255, 255)

    return skin_detected

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame")
        break

    # Perform skin detection
    skin_detected = detect_skin(frame)

    # Display the result
    cv2.imshow('Skin Detection', skin_detected)

    # Check for the 'q' key to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()

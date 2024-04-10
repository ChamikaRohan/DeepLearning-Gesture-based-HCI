import cv2
import numpy as np


# Function to create a binary mask of the hand
def create_hand_mask(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a blur to the grayscale image
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    # Use adaptive thresholding to get a binary image
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Invert the binary image
    thresh = cv2.bitwise_not(thresh)

    return thresh


# Function to get the hand area in the frame
def get_hand_area(frame, hand_mask):
    # Create a mask with the same dimensions as the frame
    mask = np.zeros_like(frame)

    # Copy the hand area from the frame using the hand mask
    mask[hand_mask == 255] = frame[hand_mask == 255]

    return mask


# Main function to capture frames from webcam
def capture_frames():
    # Open webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Get the hand mask
        hand_mask = create_hand_mask(frame)

        # Get the hand area
        hand_area = get_hand_area(frame, hand_mask)

        # Show the hand area
        cv2.imshow('Hand Area', hand_area)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close all windows
    cap.release()
    cv2.destroyAllWindows()


# Call the main function to start capturing frames
capture_frames()

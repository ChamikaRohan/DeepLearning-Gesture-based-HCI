import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)

# Initialize MediaPipe Hands Segmentation
mp_hands_segmentation = mp.solutions.hands_segmentation
hands_segmentation = mp_hands_segmentation.HandsSegmentation(static_image_mode=False, max_num_hands=1)

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Create separate windows for displaying the hand, hand with background removed, and hand segmentation
cv2.namedWindow('Hand', cv2.WINDOW_NORMAL)
cv2.namedWindow('Hand with Background Removed', cv2.WINDOW_NORMAL)
cv2.namedWindow('Hand Segmentation', cv2.WINDOW_NORMAL)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the BGR image to RGB
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(rgb_image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw the hand landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the bounding box coordinates for the hand
            x_min, y_min, x_max, y_max = float('inf'), float('inf'), float('-inf'), float('-inf')
            for landmark in hand_landmarks.landmark:
                x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                x_min = min(x_min, x)
                y_min = min(y_min, y)
                x_max = max(x_max, x)
                y_max = max(y_max, y)

            # Add some additional space around the bounding box
            padding = 20
            x_min = max(0, x_min - padding)
            y_min = max(0, y_min - padding)
            x_max = min(frame.shape[1], x_max + padding)
            y_max = min(frame.shape[0], y_max + padding)

            # Check if the bounding box coordinates are valid
            if x_min < x_max and y_min < y_max:
                # Extract the hand region with additional space
                hand_with_padding = frame[y_min:y_max, x_min:x_max]

                # Get hand segmentation mask
                segmentation_results = hands_segmentation.process(rgb_image)
                segmentation_mask = segmentation_results.segmentation_mask[:, :, np.newaxis]

                # Apply segmentation mask to the hand region
                hand_with_background_removed = hand_with_padding * segmentation_mask

                # Display the hand with padding and hand with background removed in separate windows
                cv2.imshow('Hand', hand_with_padding)
                cv2.imshow('Hand with Background Removed', hand_with_background_removed)
                cv2.imshow('Hand Segmentation', segmentation_mask)

    # Display the frame with hand landmarks
    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

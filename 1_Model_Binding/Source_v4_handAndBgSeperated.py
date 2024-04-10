import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Create windows for displaying the images
cv2.namedWindow('Hand Tracking', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Hand Tracking', 800, 600)

cv2.namedWindow('Cropped Hand Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Cropped Hand Image', 400, 400)

cv2.namedWindow('Binary Hand Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Binary Hand Image', 400, 400)

# Padding size around the hand (change as needed)
padding = 50

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
            # Get the bounding box coordinates for the hand
            x_min, y_min, x_max, y_max = float('inf'), float('inf'), float('-inf'), float('-inf')
            for landmark in hand_landmarks.landmark:
                x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                x_min = min(x_min, x)
                y_min = min(y_min, y)
                x_max = max(x_max, x)
                y_max = max(y_max, y)

            # Check if the bounding box coordinates are valid
            if x_min < x_max and y_min < y_max:
                # Add padding to the bounding box coordinates
                x_min -= padding
                y_min -= padding
                x_max += padding
                y_max += padding

                # Ensure coordinates are within frame boundaries
                x_min = max(0, x_min)
                y_min = max(0, y_min)
                x_max = min(frame.shape[1], x_max)
                y_max = min(frame.shape[0], y_max)

                # Crop the hand from the frame
                cropped_hand = frame[y_min:y_max, x_min:x_max]

                # Check if the cropped hand image is not empty
                if cropped_hand.size != 0:
                    # Resize the cropped hand image for display
                    cropped_hand_display = cv2.resize(cropped_hand, (400, 400))

                    # Display the cropped hand image in the separate window
                    cv2.imshow('Cropped Hand Image', cropped_hand_display)

                    # Convert the cropped hand image to grayscale
                    gray_hand = cv2.cvtColor(cropped_hand, cv2.COLOR_BGR2GRAY)

                    # Apply threshold to create a binary image
                    _, binary_hand = cv2.threshold(gray_hand, 100, 255, cv2.THRESH_BINARY)

                    # Display the binary hand image in the separate window
                    cv2.imshow('Binary Hand Image', binary_hand)

    # Display the frame with hand landmarks
    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

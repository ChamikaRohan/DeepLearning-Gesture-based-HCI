import cv2
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import mediapipe as mp

# Function for hand tracking
def hand_tracking(frame):
    # Initialize MediaPipe hands module
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

    # Convert the image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame
    results = hands.process(rgb_frame)

    cropped_frames = []

    # If hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract hand region
            hand_pts = []
            for lm in hand_landmarks.landmark:
                h, w, _ = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                hand_pts.append([cx, cy])

            # Create a mask for the hand region
            mask = np.zeros(frame.shape[:2], dtype=np.uint8)
            cv2.fillPoly(mask, [np.array(hand_pts)], 255)

            # Apply Gaussian blur to the mask to make the edges smooth
            blur_radius = 25  # Increase blur radius for smoother edges
            mask = cv2.GaussianBlur(mask, (blur_radius, blur_radius), 0)

            # Use morphological operations to further refine the mask
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)  # Increase iterations for better closing
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)  # Increase iterations for better opening

            # Dilate the mask to create more separation between fingers
            dilation_kernel = np.ones((25, 25), np.uint8)  # Increase kernel size for more dilation
            mask = cv2.dilate(mask, dilation_kernel, iterations=2)  # Increase iterations for more dilation

            # Bitwise AND to extract hand region
            hand_only = cv2.bitwise_and(frame, frame, mask=mask)

            # Connect all hand landmarks with lines
            connections = [(0, 1), (1, 2), (2, 3), (3, 4),  # Thumb
                           (0, 5), (5, 6), (6, 7), (7, 8),  # Index finger
                           (0, 9), (9, 10), (10, 11), (11, 12),  # Middle finger
                           (0, 13), (13, 14), (14, 15), (15, 16),  # Ring finger
                           (0, 17), (17, 18), (18, 19), (19, 20),  # Pinky finger
                           (0, 5), (0, 9), (0, 13), (0, 17)]  # Connect to palm

            for connection in connections:
                idx1, idx2 = connection
                point1 = tuple(hand_pts[idx1])
                point2 = tuple(hand_pts[idx2])
                cv2.line(hand_only, point1, point2, (255, 255, 255), 2)

            # Append the cropped hand region to the list
            cropped_frames.append(hand_only)

    return cropped_frames

# Input
cap = cv2.VideoCapture(0)

# Load the trained model
model = load_model("Media/5_gesture_model_8thattempt.h5")

_, first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (first_frame.shape[1], first_frame.shape[0]))

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    difference = cv2.absdiff(first_gray, gray_frame)
    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)

    # Call hand tracking function on the difference frame
    cropped_frames = hand_tracking(difference)

    for cropped_frame in cropped_frames:
        cv2.imshow("Hand Tracking", cropped_frame)

        resized_img = cv2.resize(cropped_frame, (64, 64))

        # Convert grayscale to RGB by repeating the single channel
        img_rgb = cv2.cvtColor(resized_img, cv2.COLOR_GRAY2RGB)

        # Expand dimensions to create a batch of 1 image
        img_array = np.expand_dims(img_rgb, axis=0)
        img_array = img_array.astype('float32') / 255.0  # Normalize to [0, 1]

        # Make predictions
        predictions = model.predict(img_array)

        # Get the predicted class label
        predicted_class = np.argmax(predictions)

        # Map class indices to gesture names
        gesture_names = {
            0: 'Gesture palm',
            1: 'Gesture thumbs up',
            2: 'Gesture rock',
            3: 'Gesture thumbs left',
            4: 'Gesture V'
        }

        # Print the predicted gesture
        print("Predicted Gesture:", gesture_names[predicted_class])

    cv2.imshow("First frame", first_frame)
    cv2.imshow("Frame", frame)
    cv2.imshow("Difference", difference)

    # Check for key press and break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

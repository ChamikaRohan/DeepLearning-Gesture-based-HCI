import cv2
import mediapipe as mp
import numpy as np

def hand_shape_crop_func(frame):
    # Initialize mediapipe hands module
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

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

# Example of how to use this function with a video file or camera stream
if __name__ == "__main__":
    # Read frames from a video file or camera stream
    cap = cv2.VideoCapture(0)  # Change to your video file path or camera index

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Call the hand tracking function with the current frame
        cropped_frames = hand_shape_crop_func(frame)

        # Display the resulting frame
        cv2.imshow('Hand Tracking', frame)

        # Display the cropped frames containing only the hand regions
        if cropped_frames:
            for i, cropped_frame in enumerate(cropped_frames):
                cv2.imshow(f'Hand {i+1} Only', cropped_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up
    cap.release()
    cv2.destroyAllWindows()

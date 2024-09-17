import cv2
import mediapipe as mp
import os
import numpy as np

def hand_skeleton_and_crop(cap, padding=20, window_size=(640, 480), save_frames=True):
    # Initialize MediaPipe Hands model
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(model_complexity=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)
    mp_drawing = mp.solutions.drawing_utils

    # Create a directory to save images
    if save_frames:
        if not os.path.exists('hands'):
            os.makedirs('hands')
        frame_count = 0

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Convert the BGR image to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image and get hand landmarks
        results = hands.process(image_rgb)

        # Convert RGB image back to BGR for OpenCV
        image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
        h, w, _ = image_bgr.shape

        # Create a fixed-size window
        window_width, window_height = window_size
        canvas = 255 * np.ones((window_height, window_width, 3), dtype=np.uint8)

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                # Calculate bounding box around hand landmarks
                x_min, x_max = w, 0
                y_min, y_max = h, 0

                for landmark in landmarks.landmark:
                    x = int(landmark.x * w)
                    y = int(landmark.y * h)

                    x_min = min(x_min, x)
                    x_max = max(x_max, x)
                    y_min = min(y_min, y)
                    y_max = max(y_max, y)

                # Add padding
                x_min = max(x_min - padding, 0)
                x_max = min(x_max + padding, w)
                y_min = max(y_min - padding, 0)
                y_max = min(y_max + padding, h)

                # Draw hand skeleton on the original image
                mp_drawing.draw_landmarks(image_bgr, landmarks, mp_hands.HAND_CONNECTIONS)

                # Crop the hand area from the image with padding
                hand_crop = image_bgr[y_min:y_max, x_min:x_max]

                # Resize the cropped hand area to fit the fixed-size window
                hand_crop_resized = cv2.resize(hand_crop, (window_width, window_height))

                # Place the resized cropped hand area onto the canvas
                canvas[0:hand_crop_resized.shape[0], 0:hand_crop_resized.shape[1]] = hand_crop_resized

        # Display the image with hand skeleton
        cv2.imshow('Hand Skeleton', canvas)

        # Save the frame if saving is enabled
        if save_frames:
            frame_file = f'hands/frame_{frame_count:04d}.png'
            cv2.imwrite(frame_file, canvas)
            frame_count += 1

        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Open a video capture object
    cap = cv2.VideoCapture(0)  # 0 for default camera, or replace with video file path

    # Call the function with padding, fixed window size, and save frames enabled
    hand_skeleton_and_crop(cap, padding=20, window_size=(75, 75), save_frames=True)

import cv2
import mediapipe as mp
import numpy as np

def main():
    # Initialize mediapipe hands module
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Convert the image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame
        results = hands.process(rgb_frame)

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
                blur_radius = 15
                mask = cv2.GaussianBlur(mask, (blur_radius, blur_radius), 0)

                # Use morphological operations to add roundness
                kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

                # Dilate the mask to create more separation between fingers
                dilation_kernel = np.ones((20, 20), np.uint8)
                mask = cv2.dilate(mask, dilation_kernel, iterations=1)

                # Bitwise AND to extract hand region
                hand_only = cv2.bitwise_and(frame, frame, mask=mask)

                # Skin color detection for darker skin
                hsv = cv2.cvtColor(hand_only, cv2.COLOR_BGR2HSV)
                lower_skin = np.array([0, 48, 20], dtype=np.uint8)
                upper_skin = np.array([20, 255, 255], dtype=np.uint8)
                skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)

                # Bitwise AND to extract skin region
                skin = cv2.bitwise_and(hand_only, hand_only, mask=skin_mask)

                # Convert everything inside the hand region to white
                skin[skin != 0] = 255  # Set non-black pixels to white

                # Apply morphological operations to remove noise
                kernel_noise_removal = np.ones((10, 10), np.uint8)  # Larger kernel for more noise removal
                skin = cv2.erode(skin, kernel_noise_removal, iterations=1)
                skin = cv2.dilate(skin, kernel_noise_removal, iterations=1)

                # Convert skin to grayscale
                skin_gray = cv2.cvtColor(skin, cv2.COLOR_BGR2GRAY)

                # Find contours to get a sharper hand border
                contours, _ = cv2.findContours(skin_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                if len(contours) > 0:
                    # Get the largest contour
                    hand_contour = max(contours, key=cv2.contourArea)
                    # Create a mask from the contour
                    hand_mask = np.zeros_like(skin_gray)
                    cv2.drawContours(hand_mask, [hand_contour], -1, 255, -1)
                    # Bitwise AND with the original skin region
                    skin = cv2.bitwise_and(skin, skin, mask=hand_mask)

                # Display the skin region
                cv2.imshow('Skin Detection', skin)

        # Display the resulting frame
        cv2.imshow('Hand Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

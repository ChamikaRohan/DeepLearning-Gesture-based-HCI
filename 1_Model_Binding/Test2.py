import cv2
import os
import numpy as np
import mediapipe as mp
import sys

sys.path.append('../1_Model_Binding')

from Utils.First_frame_getter import first_frame_getter

def save_image(image, folder_path, image_name):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Construct the full path to save the image
    image_path = os.path.join(folder_path, image_name)

    # Save the image
    cv2.imwrite(image_path, image)
    print(f"Image saved to {image_path}")


# Example usage within the predict_gesture function:
def predict_gesture(cap, save_folder='hands/Attempt_2'):

    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
    mp_drawing = mp.solutions.drawing_utils

    gesture = None
    image_count = 1650
    first_gray = first_frame_getter(cap)

    while True:
        success, frame = cap.read()
        if not success:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        difference = cv2.absdiff(first_gray, gray_frame)
        _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
        # Find hand landmarks using MediaPipe
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Extract hand region coordinates
                x_min, y_min = frame.shape[1], frame.shape[0]
                x_max, y_max = 0, 0
                for landmark in hand_landmarks.landmark:
                    x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                    x_min = min(x_min, x)
                    x_max = max(x_max, x)
                    y_min = min(y_min, y)
                    y_max = max(y_max, y)

                # Draw hand landmarks on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Create a blank image to draw the skeleton (hand landmarks only)
                skeleton_image = np.zeros_like(frame)

                # Draw landmarks on the blank image (skeleton image)
                mp_drawing.draw_landmarks(skeleton_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Crop hand region from the frame with some padding
                padding = 20  # Adjust the padding as needed
                hand_crop = frame[max(0, y_min - padding):min(y_max + padding, frame.shape[0]),
                            max(0, x_min - padding):min(x_max + padding, frame.shape[1])]

                skeleton_image = skeleton_image[max(0, y_min - padding):min(y_max + padding, frame.shape[0]),
                                 max(0, x_min - padding):min(x_max + padding, frame.shape[1])]

                resized_img = cv2.resize(skeleton_image, (75, 75))

                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Create a blank image to draw the skeleton (hand landmarks only)
                skeleton_image_2 = np.zeros_like(frame)

                # Draw landmarks on the blank image (skeleton image)
                img_rgb = cv2.cvtColor(difference, cv2.COLOR_GRAY2RGB)
                mp_drawing.draw_landmarks(img_rgb, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                hand_crop = img_rgb[max(0, y_min - padding):min(y_max + padding, frame.shape[0]),
                            max(0, x_min - padding):min(x_max + padding, frame.shape[1])]
                resized_img_2 = cv2.resize(hand_crop, (75, 75))


                # Save the resized image
                save_image(resized_img_2, save_folder, f"{image_count}.png")
                image_count += 1

                # Display the resized image in a feedback window
                cv2.imshow("Resized Hand Image", resized_img_2)

        # Break loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    # Initialize video capture from the default camera (0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return

    # Define the folder where images will be saved
    save_folder = 'hands/1_1'

    # Call the predict_gesture function
    predict_gesture(cap, save_folder)


if __name__ == "__main__":
    main()

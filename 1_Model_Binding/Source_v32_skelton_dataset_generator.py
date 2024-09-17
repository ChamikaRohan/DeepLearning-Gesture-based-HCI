import cv2
import os
import mediapipe as mp

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
    image_count = 0

    while True:
        success, frame = cap.read()
        if not success:
            break

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

                # Crop hand region from the frame with some padding
                padding = 20  # Adjust the padding as needed
                hand_crop = frame[max(0, y_min - padding):min(y_max + padding, frame.shape[0]),
                            max(0, x_min - padding):min(x_max + padding, frame.shape[1])]

                resized_img = cv2.resize(hand_crop, (75, 75))

                # Save the resized image
                save_image(resized_img, save_folder, f"{image_count}.png")
                image_count += 1


    cap.release()
    cv2.destroyAllWindows()


import cv2


def main():
    # Initialize video capture from the default camera (0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return

    # Define the folder where images will be saved
    save_folder = 'hands/5'

    # Call the predict_gesture function
    predict_gesture(cap, save_folder)


if __name__ == "__main__":
    main()

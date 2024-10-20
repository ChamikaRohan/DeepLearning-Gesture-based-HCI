import cv2
import numpy as np
from tensorflow.keras.models import load_model
import mediapipe as mp
from pynput.mouse import Controller as MouseController
import pyautogui

# Set the cursor speed factor and smoothing factor
CURSOR_SPEED_FACTOR = 5
SMOOTHING_FACTOR = 0.7

def move_cursor(x, y):
    global prev_x, prev_y
    # Smooth the hand coordinates
    scaled_x = x * CURSOR_SPEED_FACTOR
    scaled_y = y * CURSOR_SPEED_FACTOR

    # Apply smoothing
    smoothed_x = int(prev_x * (1 - SMOOTHING_FACTOR) + scaled_x * SMOOTHING_FACTOR)
    smoothed_y = int(prev_y * (1 - SMOOTHING_FACTOR) + scaled_y * SMOOTHING_FACTOR) - 600

    # Move the cursor based on smoothed hand coordinates
    mouse.position = (smoothed_x, smoothed_y)
    print("Cursor moved to ({}, {})".format(smoothed_x, smoothed_y))

    prev_x, prev_y = smoothed_x, smoothed_y

def left_click():
    pyautogui.click()

# Function to perform a right click
def right_click():
    pyautogui.rightClick()
def predict_gesture(cap, model_path):
    model = load_model(model_path)

    _, first_frame = cap.read()
    first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.1, min_tracking_confidence=0.1)

    while True:
        _, frame = cap.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        difference = cv2.absdiff(first_gray, gray_frame)
        _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)

        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                x_min, y_min = frame.shape[1], frame.shape[0]
                x_max, y_max = 0, 0
                for landmark in hand_landmarks.landmark:
                    x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                    if x < x_min:
                        x_min = x
                    if x > x_max:
                        x_max = x
                    if y < y_min:
                        y_min = y
                    if y > y_max:
                        y_max = y

                padding = 30
                hand_crop = difference[max(0, y_min - padding):min(y_max + 10, difference.shape[0]),
                            max(0, x_min - padding):min(x_max + padding, difference.shape[1])]
                cv2.imshow("Hand Crop", hand_crop)

                resized_img = cv2.resize(hand_crop, (75, 75))

                # Convert grayscale to RGB by repeating the single channel
                img_rgb = cv2.cvtColor(resized_img, cv2.COLOR_GRAY2RGB)

                # Expand dimensions to create a batch of 1 image
                img_array = np.expand_dims(img_rgb, axis=0)
                img_array = img_array.astype('float32') / 255.0  # Normalize to [0, 1]

                # Make predictions
                predictions = model.predict(img_array)
                # print(predictions)
                # Get the predicted class label
                predicted_class = np.argmax(predictions)
                if predicted_class==0:
                    move_cursor(x_min + (x_max - x_min) / 2, y_min + (y_max - y_min) / 2)
                elif predicted_class==4:
                    left_click()
                elif predicted_class == 2:
                    right_click()

        cv2.imshow("First frame", first_frame)
        cv2.imshow("Frame", frame)
        cv2.imshow("Difference", difference)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Usage example
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    model_path = "Media/6_gesture_model_9th_attempt_part_3_without_pretrained.h5"
    mouse = MouseController()
    prev_x, prev_y = 0, 0
    predict_gesture(cap, model_path)

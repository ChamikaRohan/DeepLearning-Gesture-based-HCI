import cv2
import sys
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import mediapipe as mp

from Utils.First_frame_getter import first_frame_getter

from Utils.Auto_first_frame_setter import auto_first_frame_setter

from collections import deque

sys.path.append('../User_Interface')
from Window_pinner import window_pinner

sys.path.append('../1_Model_Binding')
from Utils.First_frame_getter import first_frame_getter

sys.path.append('../3_Intended_Gesture_Mapping')
from dynamic_intended_gesture_mapping_func import intended_gesture_and_direction_map

import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model

def predict_gesture_and_direction(cap, model_path, first_gray, gesture_type):
    print(model_path)
    model = load_model(model_path)

    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    #hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.7)
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.1, min_tracking_confidence=0.1)
    mp_drawing = mp.solutions.drawing_utils

    gesture = None
    prev_landmarks = None

    while True:
        _, frame = cap.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        difference = cv2.absdiff(first_gray, gray_frame)
        _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)

        # Find hand landmarks using MediaPipe
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            moving = False
            direction = "Static"

            for hand_landmarks in results.multi_hand_landmarks:
                # Gesture prediction
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
                img_rgb = cv2.cvtColor(resized_img, cv2.COLOR_GRAY2RGB)
                img_array = np.expand_dims(img_rgb, axis=0).astype('float32') / 255.0
                predictions = model.predict(img_array)
                predicted_class = np.argmax(predictions)
                predicted_probability = predictions[0][predicted_class]

                if predicted_probability > 0.6:
                    gesture = predicted_class
                else:
                    gesture = None

                # Direction detection
                if prev_landmarks is not None:
                    prev_x = prev_landmarks[0].x
                    prev_y = prev_landmarks[0].y
                    curr_x = hand_landmarks.landmark[0].x
                    curr_y = hand_landmarks.landmark[0].y

                    dx = curr_x - prev_x
                    dy = curr_y - prev_y

                    if abs(dx) > abs(dy):
                        if dx > 0:
                            direction = "Right"
                        else:
                            direction = "Left"
                    else:
                        if dy > 0:
                            direction = "Down"
                        else:
                            direction = "Up"

                    if abs(dx) > 0.02 or abs(dy) > 0.04:
                        direction = direction
                    else:
                        direction = "Static"

                prev_landmarks = hand_landmarks.landmark
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            if gesture_type == 1:
                yield gesture
            else:
                yield gesture, direction

        # else:
        #     if auto_first_frame_setter(difference):
        #         print("Web-cam feed has noise!, resetting first frame automatically.")
        #         first_gray = first_frame_getter(cap)

        cv2.imshow("Frame", frame)
        cv2.imshow("Difference", difference)
        window_pinner("Hand Crop")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            first_gray = first_frame_getter(cap)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            gesture = 's'
            yield gesture, "Static"

"""
cap = cv2.VideoCapture(0)
update_first_frame = False
first_gray = first_frame_getter(cap)
model_path = "Media/10_gesture_model_25th_attempt.h5"
for gesture, direction in predict_gesture_and_direction(cap, model_path, first_gray, 2):
    if gesture is None:
        print("No gesture detected.")
    else:
        print("Predicted Ges3ure:", gesture)
        print("Predicted Direction:", direction)
        # intended_gesture, intended_direction = dynamic_intended_gesture_mapping_func(predicted_class, predicted_direction, gesture_frames, direction_frames)
"""



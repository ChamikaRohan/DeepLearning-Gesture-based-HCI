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
from Intended_gesture_mapping_func import intended_gesture_map
from dynamic_intended_gesture_mapping_func import intended_gesture_and_direction_map

sys.path.append('../8_Dynamic_Gesture_Recognition')
from Dynamic_gesture_extender import combined_gesture_number_finder

sys.path.append('../10_Storage_and_utils')
from Payload import Payload

import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model

def predict_gesture_and_direction(cap, model_path, first_gray, gesture_type):
    model = load_model(model_path)

    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
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

                # Crop hand region from the frame with some padding
                padding = 20

                hand_tracked_image = frame[max(0, y_min - padding):min(y_max + padding, frame.shape[0]),
                                     max(0, x_min - padding):min(x_max + padding, frame.shape[1])]

                resized_hand_tracked_img = cv2.resize(hand_tracked_image, (75, 75))

                # Draw hand landmarks on the frame (original image)
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Create a blank image to draw the skeleton (hand landmarks only)
                skeleton_image = np.zeros_like(frame)

                # Draw landmarks on the blank image (skeleton image)
                mp_drawing.draw_landmarks(skeleton_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                skeleton_image = skeleton_image[max(0, y_min - padding):min(y_max + padding, frame.shape[0]),
                                 max(0, x_min - padding):min(x_max + padding, frame.shape[1])]

                resized_img = cv2.resize(skeleton_image, (75, 75))

                payload = Payload()

                if payload.get_hand_window_status():
                    cv2.imshow("Hand Crop", resized_hand_tracked_img)
                else:
                    cv2.destroyAllWindows()

                # Expand dimensions to create a batch of 1 image
                img_array = np.expand_dims(resized_img, axis=0)
                img_array = img_array.astype('float32') / 255.0  # Normalize to [0, 1]

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

                yield gesture, direction

        else:
            if auto_first_frame_setter(difference):
                print("Web-cam feed has noise!, resetting first frame automatically.")
                first_gray = first_frame_getter(cap)

        payload = Payload()
        if payload.get_hand_window_status():
            window_pinner("Hand Crop")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            first_gray = first_frame_getter(cap)


"""
cap = cv2.VideoCapture(0)
def initiate_payload():
    payload = Payload()
    payload.set_first_gray(first_frame_getter(cap))
    payload.set_gesture_type(1)
    payload.set_mode(2)
    payload.set_model_path("../1_Model_Binding/Media/10_gesture_skelton_model_v13.h5")
    payload.set_gesture_frames({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0})
    payload.set_direction_frames(deque())
    payload.set_custom_config_path( 'C:\\Users\M\Desktop\MotionPilot')
    payload.set_hand_window_status(True)
    payload.set_application(1)
    return payload

payload = initiate_payload()

update_first_frame = False
first_gray = first_frame_getter(cap)
model_path = "Media/10_gesture_skelton_model_v13.h5"
for gesture, direction in predict_gesture_and_direction(cap, payload.get_model_path(),
                                                                    payload.get_first_gray(),
                                                                    payload.get_gesture_type()):

    print("Gesture:", gesture)
    print("Direction:", direction)
    intended_combined_gesture = combined_gesture_number_finder(gesture, direction)
    print(intended_combined_gesture)
"""
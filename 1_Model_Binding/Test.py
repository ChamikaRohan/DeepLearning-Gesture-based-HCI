import cv2
import sys
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import mediapipe as mp

from Utils.First_frame_getter import first_frame_getter

from Utils.Auto_first_frame_setter import auto_first_frame_setter

sys.path.append('../User_Interface')
from Window_pinner import window_pinner

sys.path.append('../1_Model_Binding')
from Utils.First_frame_getter import first_frame_getter

sys.path.append('../10_Storage_and_utils')
from Payload import Payload

from collections import deque

def predict_gesture(cap, model_path, first_gray):
    model = load_model(model_path)

    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.1)
    mp_drawing = mp.solutions.drawing_utils

    gesture = None

    while True:
        _, frame = cap.read()
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
                    if x < x_min:
                        x_min = x
                    if x > x_max:
                        x_max = x
                    if y < y_min:
                        y_min = y
                    if y > y_max:
                        y_max = y

                # Draw hand landmarks on the frame (original image)
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Create a blank image to draw the skeleton (hand landmarks only)
                skeleton_image = np.zeros_like(frame)

                # Draw landmarks on the blank image (skeleton image)
                mp_drawing.draw_landmarks(skeleton_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Crop hand region from the frame with some padding
                padding = 20  # Adjust the padding as needed

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












                payload = Payload()

                if payload.get_hand_window_status():
                    cv2.imshow("Hand Crop", resized_img)
                    cv2.imshow("Hand Crop 2", resized_img_2)
                else:
                    cv2.destroyAllWindows()

                # Expand dimensions to create a batch of 1 image
                img_array = np.expand_dims(resized_img_2, axis=0)
                img_array = img_array.astype('float32') / 255.0  # Normalize to [0, 1]

                # Make predictions
                predictions = model.predict(img_array)
                predicted_class = np.argmax(predictions)
                predicted_probability = predictions[0][predicted_class]

                if predicted_class == 0:
                    if predicted_probability > 0.6:
                        gesture = 0
                    else:
                        gesture = None

                elif predicted_class == 1:
                    if predicted_probability > 0.6:
                        gesture = 1
                    else:
                        gesture = None

                elif predicted_class == 2:
                    if predicted_probability > 0.6:
                        gesture = 2
                    else:
                        gesture = None

                elif predicted_class == 3:
                    if predicted_probability > 0.6:
                        gesture = 3
                    else:
                        gesture = None

                elif predicted_class == 4:
                    if predicted_probability > 0.6:
                        gesture = 4
                    else:
                        gesture = None
                elif predicted_class == 5:
                    if predicted_probability > 0.6:
                        gesture = 5
                    else:
                        gesture = None
                elif predicted_class == 6:
                    if predicted_probability > 0.6:
                        gesture = 6
                    else:
                        gesture = None
                elif predicted_class == 7:
                    if predicted_probability > 0.6:
                        gesture = 7
                    else:
                        gesture = None
                elif predicted_class == 8:
                    if predicted_probability > 0.6:
                        gesture = 8
                    else:
                        gesture = None
                elif predicted_class == 9:
                    if predicted_probability > 0.6:
                        gesture = 9
                    else:
                        gesture = None
                yield gesture
        else:
            if auto_first_frame_setter(difference):
                print("Web-cam feed has noise!, resetting first frame automatically.")
                first_gray = first_frame_getter(cap)

        payload = Payload()
        cv2.imshow("Difference", difference)
        if payload.get_hand_window_status():
            window_pinner("Hand Crop")
            window_pinner("Hand Crop 2")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            first_gray = first_frame_getter(cap)






cap = cv2.VideoCapture(0)
def initiate_payload():
    payload = Payload()
    payload.set_first_gray(first_frame_getter(cap))
    payload.set_gesture_type(1)
    payload.set_mode(2)
    payload.set_model_path("../1_Model_Binding/Media/10_gesture_skelton_model_v13.h5")
    payload.set_gesture_frames({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0})
    payload.set_direction_frames(deque())
    payload.set_custom_config_path('C:\\Users\M\Desktop\MotionPilot')
    payload.set_hand_window_status(True)
    payload.set_application(1)
    return payload

payload = initiate_payload()

update_first_frame = False
first_gray = first_frame_getter(cap)
model_path = "Media/10_gesture_skelton_model_v13.h5"
for gesture in predict_gesture(cap, model_path, first_gray):
    if gesture is None:
        print("No gesture detected.")
    else:
        print("Predicted Gesture:", gesture)






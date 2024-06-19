import cv2
import sys
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import mediapipe as mp

from Utils.First_frame_getter import first_frame_getter

from Utils.Noise_finder import is_noisy

sys.path.append('../User_Interface')
from Window_pinner import window_pinner

sys.path.append('../1_Model_Binding')
from Utils.First_frame_getter import first_frame_getter


def predict_gesture(cap, model_path, first_gray):
    model = load_model(model_path)

    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

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

                # Crop hand region from the difference frame with some padding
                padding = 30  # Adjust the padding as needed
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

                # Get the probability of the predicted class
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
                yield gesture

        if is_noisy(difference):
            print("Web-cam feed has noise!, resetting first frame automatically.")
            first_gray = first_frame_getter(cap)

        cv2.imshow("Frame", frame)
        cv2.imshow("Difference", difference)
        window_pinner("Hand Crop")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            first_gray = first_frame_getter(cap)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            gesture = 's'
            yield gesture


"""
cap = cv2.VideoCapture(0)
update_first_frame = False
first_gray = first_frame_getter(cap)
model_path = "Media/8_gesture_model_19th_attempt.h5"
for gesture in predict_gesture(cap, model_path, first_gray):
    if gesture is None:
        print("No gesture detected.")
    else:
        print("Predicted Gesture:", gesture)

"""



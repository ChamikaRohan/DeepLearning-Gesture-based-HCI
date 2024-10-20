import cv2
import numpy as np
from tensorflow.keras.models import load_model
import mediapipe as mp

def predict_gesture(cap, model_path):
    model = load_model(model_path)

    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
    mp_drawing = mp.solutions.drawing_utils

    gesture = None

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

                img_array = np.expand_dims(resized_img, axis=0)
                img_array = img_array.astype('float32') / 255.0

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

                elif predicted_class == 3:
                    if predicted_probability > 0.6:
                        gesture = 3

                elif predicted_class == 4:
                    if predicted_probability > 0.6:
                        gesture = 4

                elif predicted_class == 5:
                    if predicted_probability > 0.6:
                        gesture = 5

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

                yield predictions
                print(predicted_class)

                # Show the hand crop and resized image
                cv2.imshow("Hand Crop", hand_crop)
                # cv2.imshow("Preprocessed Image", preprocessed_image)

        # Exit condition
        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    model_path = "Media/10_gesture_skelton_model_v8.h5"
    while True:
            for gesture in predict_gesture(cap, model_path):
                print("Predicted Gesture:", gesture)



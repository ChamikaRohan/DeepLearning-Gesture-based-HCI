import cv2
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import mediapipe as mp

# Input
cap = cv2.VideoCapture(0)

# Load the trained model
model = load_model("Media/CombinedWith1and2_model.h5")

_, first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (first_frame.shape[1], first_frame.shape[0]))

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

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
            padding = 60 # Adjust the padding as needed
            hand_crop = difference[max(0, y_min - padding):min(y_max + padding, difference.shape[0]),
                                   max(0, x_min - padding):min(x_max + padding, difference.shape[1])]
            cv2.imshow("Hand Crop", hand_crop)

            resized_img = cv2.resize(hand_crop, (64, 64))

            # Convert grayscale to RGB by repeating the single channel
            img_rgb = cv2.cvtColor(resized_img, cv2.COLOR_GRAY2RGB)

            # Expand dimensions to create a batch of 1 image
            img_array = np.expand_dims(img_rgb, axis=0)
            img_array = img_array.astype('float32') / 255.0  # Normalize to [0, 1]

            # Make predictions
            predictions = model.predict(img_array)

            # Get the predicted class label
            predicted_class = np.argmax(predictions)

            # Map class indices to gesture names
            gesture_names = {
                0: 'Gesture 1 finger',
                1: 'Gesture V sign',
                2: 'Gesture Full hand',
                3: 'Gesture Thumbs up',
                4: 'Gesture _|',
                5: 'Gesture Swag'
            }

            # Print the predicted gesture
            print("Predicted Gesture:", gesture_names[predicted_class])

    cv2.imshow("First frame", first_frame)
    cv2.imshow("Frame", frame)
    cv2.imshow("Difference", difference)


    # Check for key press and break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

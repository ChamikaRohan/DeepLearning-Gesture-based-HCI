import cv2
import sys
import numpy as np
from tensorflow.keras.models import load_model
import mediapipe as mp
from collections import deque
import time

# Add paths for necessary utilities
sys.path.append('../1_Model_Binding')
from Utils.First_frame_getter import first_frame_getter
from Utils.Auto_first_frame_setter import auto_first_frame_setter

sys.path.append('../User_Interface')
from Window_pinner import window_pinner

sys.path.append('../10_Storage_and_utils')
from Payload import Payload

sys.path.append('../1_Model_Binding')
from Gesture_prediction_func import predict_gesture

# Initialize video capture
cap = cv2.VideoCapture(0)

# Function to initialize payload values
def initiate_payload():
    payload = Payload()
    payload.set_first_gray(first_frame_getter(cap))
    payload.set_gesture_type(1)
    payload.set_mode(2)
    payload.set_model_path("../1_Model_Binding/Media/10_gesture_skelton_model_v13.h5")
    payload.set_gesture_frames({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0})
    payload.set_direction_frames(deque())
    payload.set_custom_config_path('C:\\Users\\M\\Desktop\\MotionPilot')
    payload.set_hand_window_status(True)
    payload.set_application(1)
    return payload

# Initialize the payload
payload = initiate_payload()

# Load the first frame for background subtraction
first_gray = first_frame_getter(cap)
model_path = "../1_Model_Binding/Media/10_gesture_skelton_model_v13.h5"

# Variables for accuracy calculation
total_predictions = 0
correct_gesture_predictions = 0
current_gesture = 0  # Default gesture to check accuracy for
frame_limit = 300  # Set the limit for frames per gesture
mid_interval = 150  # Middle of the frame limit for gesture change

# Store accuracy for each gesture
gesture_accuracies = {i: None for i in range(10)}

# Loop through predictions and calculate real-time accuracy
for gesture in predict_gesture(cap, model_path, first_gray):
    # Check if we reached the frame limit for the current gesture
    if total_predictions < frame_limit:
        total_predictions += 1

        # Check if the detected gesture matches the current target gesture
        if gesture == current_gesture:
            correct_gesture_predictions += 1
            print(f"Predicted Gesture: {current_gesture} (Correct)")
        elif gesture is not None:
            print(f"Predicted Gesture: {gesture} (Incorrect)")
        else:
            print("No gesture detected.")

        # Calculate accuracy of the current gesture predictions
        if total_predictions > 0:
            accuracy = (correct_gesture_predictions / total_predictions) * 100
            print(f"Real-time accuracy for gesture {current_gesture}: {accuracy:.2f}% over {total_predictions} frames")

    # Check if 150 frames reached for the mid-interval gesture change
    if total_predictions == mid_interval:
        print(f"Reached {mid_interval} frames for gesture {current_gesture}. You have 2 seconds to change gesture.")
        time.sleep(2)  # 2 seconds freedom to change gesture

    # Check if frame limit reached
    if total_predictions >= frame_limit:
        # Store the accuracy for the current gesture
        gesture_accuracies[current_gesture] = (correct_gesture_predictions / total_predictions) * 100 if total_predictions > 0 else 0
        print(f"Reached {frame_limit} frames for gesture {current_gesture}. You have 2 seconds to change gesture.")
        time.sleep(2)  # 2 seconds freedom to change gesture
        # Reset counts for the next gesture
        total_predictions = 0
        correct_gesture_predictions = 0
        current_gesture += 1  # Move to the next gesture

        # Stop if all gestures have been checked
        if current_gesture >= 10:
            break

    # Press 'q' to change the gesture being checked for accuracy
    if cv2.waitKey(1) & 0xFF == ord('q'):
        try:
            new_gesture = int(input("Enter the gesture number (0-9) for which to check accuracy: "))
            if 0 <= new_gesture <= 9:
                current_gesture = new_gesture
                total_predictions = 0
                correct_gesture_predictions = 0
                print(f"Switched to tracking accuracy for gesture {current_gesture}. Resetting frame count.")
            else:
                print("Invalid gesture number. Please enter a number between 0 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Release the video capture when done
cap.release()
cv2.destroyAllWindows()

# Print the final accuracy for all gestures
print("\nFinal Accuracy for each gesture:")
for gesture_num, accuracy in gesture_accuracies.items():
    if accuracy is not None:
        print(f"Gesture {gesture_num}: {accuracy:.2f}%")
    else:
        print(f"Gesture {gesture_num}: No data collected.")
